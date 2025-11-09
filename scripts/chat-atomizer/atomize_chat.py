#!/usr/bin/env python3
"""
Chat Atomizer v1.0
==================

Transforme les exports bruts de conversations Claude.ai en cartes atomiques Obsidian.

Usage:
    python atomize_chat.py --input export.md --output vault/Chat-Exports/

Author: Moncef
Date: 2025-11-09
"""

import re
import yaml
import argparse
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any, Optional
import json


class Message:
    """Représente un message individuel de la conversation."""
    
    def __init__(self, order: int, role: str, content: str, msg_id: str, 
                 timestamp: Optional[str] = None, attachments: List[Dict] = None):
        self.order = order
        self.role = role
        self.content = content
        self.id = msg_id
        self.timestamp = timestamp
        self.attachments = attachments or []
        self.topics = []
        self.code_blocks = []
        
    def __repr__(self):
        return f"Message(order={self.order}, role={self.role}, id={self.id})"


class ChatExport:
    """Représente un export complet de conversation."""
    
    def __init__(self, filepath: Path):
        self.filepath = filepath
        self.content = filepath.read_text(encoding='utf-8')
        self.frontmatter = {}
        self.messages = []
        self._parse()
        
    def _parse(self):
        """Parse le fichier markdown export."""
        # Extraire le frontmatter YAML
        yaml_match = re.match(r'^---\n(.*?)\n---\n', self.content, re.DOTALL)
        if yaml_match:
            self.frontmatter = yaml.safe_load(yaml_match.group(1))
            # Enlever le frontmatter du contenu
            content_without_frontmatter = self.content[yaml_match.end():]
        else:
            content_without_frontmatter = self.content
        
        print("🔍 Parsing messages...")
        
        # Méthode plus simple : Split sur les headers de messages
        # Pattern pour détecter les headers: ## 👤 Message X - User OU ## 🤖 Message X - Assistant
        header_pattern = r'## (👤|🤖) Message (\d+) - (User|Assistant)'
        
        # Trouver tous les headers et leurs positions
        headers = []
        for match in re.finditer(header_pattern, content_without_frontmatter):
            emoji = match.group(1)
            order = int(match.group(2))
            role = match.group(3).lower()
            start_pos = match.end()
            
            headers.append({
                'emoji': emoji,
                'order': order,
                'role': role,
                'start': start_pos,
                'match': match
            })
        
        print(f"  Found {len(headers)} message headers")
        
        if len(headers) == 0:
            print("❌ No message headers found!")
            print("  Looking for pattern: ## 👤 Message X - User")
            print("  or: ## 🤖 Message X - Assistant")
            # Debug: montrer les premiers headers du fichier
            print("\n  First 5 ## headers in file:")
            for match in re.finditer(r'^## .+$', content_without_frontmatter, re.MULTILINE):
                print(f"    {match.group()}")
                if match.start() > 1000:
                    break
            return
        
        # Pour chaque header, extraire le contenu jusqu'au prochain header ou ---
        for i, header in enumerate(headers):
            # Déterminer la fin du contenu
            if i < len(headers) - 1:
                # Il y a un message suivant
                end_pos = headers[i + 1]['match'].start()
            else:
                # Dernier message, aller jusqu'à la fin
                end_pos = len(content_without_frontmatter)
            
            # Extraire le bloc de contenu
            content_block = content_without_frontmatter[header['start']:end_pos]
            
            # Enlever le dernier --- si présent
            content_block = re.sub(r'\n+---\n*$', '', content_block)
            
            # Parser le contenu
            msg_id = None
            timestamp = None
            attachments = []
            content_lines = []
            
            lines = content_block.split('\n')
            in_content = False
            
            for line in lines:
                line_stripped = line.strip()
                
                # Skip lignes vides au début
                if not in_content and not line_stripped:
                    continue
                
                # Parser ID
                if line_stripped.startswith('**ID:**'):
                    msg_id = line_stripped.replace('**ID:**', '').strip()
                    continue
                
                # Parser Timestamp
                if line_stripped.startswith('**Timestamp:**'):
                    timestamp = line_stripped.replace('**Timestamp:**', '').strip()
                    continue
                
                # Parser Attachments
                if line_stripped.startswith('**Attachments:**'):
                    # Les lignes suivantes sont les attachments
                    continue
                
                if line_stripped.startswith('- 📷') or line_stripped.startswith('- 📎'):
                    # Parser attachment
                    att_match = re.match(r'- (📷|📎) (\w+): `?(.+?)`?$', line_stripped)
                    if att_match:
                        att_emoji, att_type, att_name = att_match.groups()
                        attachments.append({
                            'type': att_type.lower(),
                            'name': att_name
                        })
                    continue
                
                # Tout le reste est du contenu
                in_content = True
                content_lines.append(line)
            
            # Joindre le contenu
            content = '\n'.join(content_lines).strip()
            
            # Skip si pas de contenu (juste des métadonnées)
            if not content:
                continue
            
            # Créer le message
            message = Message(
                order=header['order'],
                role=header['role'],
                content=content,
                msg_id=msg_id or f"msg-{header['order']}",
                timestamp=timestamp,
                attachments=attachments
            )
            
            self.messages.append(message)
        
        print(f"✅ Parsed {len(self.messages)} messages from export")
        
    def get_stats(self) -> Dict[str, Any]:
        """Calcule les statistiques de l'export."""
        user_count = sum(1 for m in self.messages if m.role == 'user')
        assistant_count = sum(1 for m in self.messages if m.role == 'assistant')
        total_attachments = sum(len(m.attachments) for m in self.messages)
        
        # Extraire dates de conversation
        conversation_start = self.frontmatter.get('conversation_start') or \
                           self.frontmatter.get('date_start') or \
                           self.frontmatter.get('created', 'unknown')
        
        conversation_end = self.frontmatter.get('conversation_end') or \
                         self.frontmatter.get('date_end') or \
                         self.frontmatter.get('exported', 'unknown')
        
        # Si timestamps dans messages, les utiliser
        if self.messages:
            if self.messages[0].timestamp:
                conversation_start = self.messages[0].timestamp
            if self.messages[-1].timestamp:
                conversation_end = self.messages[-1].timestamp
        
        return {
            'total_messages': len(self.messages),
            'user_messages': user_count,
            'assistant_messages': assistant_count,
            'total_attachments': total_attachments,
            'chat_id': self.frontmatter.get('chat_id', 'unknown'),
            'title': self.frontmatter.get('title', 'Untitled'),
            'exported': self.frontmatter.get('exported', ''),
            'platform': self.frontmatter.get('platform', 'unknown'),
            'conversation_start': conversation_start,
            'conversation_end': conversation_end
        }


class TopicDetector:
    """Détecte les topics/thèmes dans les messages."""
    
    # Keywords par domaine
    KEYWORDS = {
        'power-bi': ['power bi', 'power pivot', 'dax', 'measures', 'power query'],
        'excel': ['excel', 'xlsx', 'spreadsheet', 'formulas'],
        'python': ['python', 'script', 'def ', 'import ', 'pandas'],
        'obsidian': ['obsidian', 'vault', 'markdown', 'dataview', 'frontmatter'],
        'finance': ['ticket', 'receipt', 'transaction', 'price', 'budget'],
        'data-analysis': ['analyze', 'analysis', 'dataset', 'visualization', 'chart'],
        'receipts': ['leclerc', 'carrefour', 'totalenergies', 'mcdonalds', 'action'],
        'code': ['```', 'function', 'const ', 'let ', 'var '],
        'git': ['git', 'commit', 'branch', 'repository', 'merge'],
        'automation': ['script', 'automate', 'workflow', 'pipeline']
    }
    
    @staticmethod
    def detect(content: str) -> List[str]:
        """Détecte les topics dans un contenu."""
        content_lower = content.lower()
        detected = []
        
        for topic, keywords in TopicDetector.KEYWORDS.items():
            if any(kw in content_lower for kw in keywords):
                detected.append(topic)
        
        return detected


class CodeExtractor:
    """Extrait les blocs de code des messages."""
    
    @staticmethod
    def extract(content: str) -> List[Dict[str, str]]:
        """Extrait tous les code blocks avec leur langage."""
        code_blocks = []
        
        # Pattern: ```lang\ncode\n```
        pattern = r'```(\w+)?\n(.*?)```'
        matches = re.finditer(pattern, content, re.DOTALL)
        
        for idx, match in enumerate(matches, 1):
            lang = match.group(1) or 'text'
            code = match.group(2).strip()
            
            code_blocks.append({
                'id': idx,
                'lang': lang,
                'content': code
            })
        
        return code_blocks


class AtomicCardGenerator:
    """Génère les cartes atomiques Obsidian."""
    
    def __init__(self, export: ChatExport, output_dir: Path):
        self.export = export
        self.output_dir = output_dir
        self.cards_dir = output_dir / 'cards'
        self.cards_dir.mkdir(parents=True, exist_ok=True)
        
    def generate_card(self, message: Message, prev_msg: Optional[Message] = None, 
                     next_msg: Optional[Message] = None) -> Path:
        """Génère une carte atomique pour un message."""
        
        # Détecter topics
        message.topics = TopicDetector.detect(message.content)
        
        # Extraire code
        message.code_blocks = CodeExtractor.extract(message.content)
        
        # Nom du fichier
        role_prefix = "user" if message.role == "user" else "assistant"
        filename = f"{message.order:03d}_{role_prefix}_{message.id}.md"
        filepath = self.cards_dir / filename
        
        # Générer frontmatter
        frontmatter = {
            'type': 'chat-card',
            'parent_export': f"[[{self.export.frontmatter.get('title', 'Export')}]]",
            'order': message.order,
            'role': message.role,
            'created': datetime.now().isoformat() + 'Z',
            'tags': ['chat-card'] + message.topics,
            'attachments_count': len(message.attachments)
        }
        
        if message.timestamp:
            frontmatter['timestamp'] = message.timestamp
            
        # Emoji selon rôle
        emoji = "👤" if message.role == "user" else "🤖"
        role_title = "User" if message.role == "user" else "Assistant"
        
        # Construire le contenu
        card_content = f"""---
{yaml.dump(frontmatter, allow_unicode=True, sort_keys=False)}---

# {emoji} Message {message.order} - {role_title}

**ID:** {message.id}
"""
        
        if message.timestamp:
            card_content += f"**Timestamp:** {message.timestamp}\n"
        
        if message.attachments:
            card_content += f"\n## 📎 Attachments ({len(message.attachments)})\n\n"
            for att in message.attachments:
                att_icon = "📷" if att['type'] == 'image' else "📎"
                card_content += f"- {att_icon} {att['type'].title()}: `{att['name']}`\n"
        
        # Contenu principal
        card_content += f"\n## 💬 Content\n\n{message.content}\n"
        
        # Navigation
        card_content += "\n## 🔗 Navigation\n\n"
        
        if prev_msg:
            prev_filename = f"{prev_msg.order:03d}_{'user' if prev_msg.role == 'user' else 'assistant'}_{prev_msg.id}"
            card_content += f"- ⬆️ Previous: [[{prev_filename}]]\n"
        
        if next_msg:
            next_filename = f"{next_msg.order:03d}_{'user' if next_msg.role == 'user' else 'assistant'}_{next_msg.id}"
            card_content += f"- ⬇️ Next: [[{next_filename}]]\n"
        
        card_content += f"- 📊 MOC: [[_MOC_{self.export.filepath.stem}]]\n"
        
        if message.topics:
            card_content += "\n## 🏷️ Topics\n\n"
            for topic in message.topics:
                card_content += f"- #{topic}\n"
        
        # Sauvegarder
        filepath.write_text(card_content, encoding='utf-8')
        
        return filepath
    
    def generate_all_cards(self) -> List[Path]:
        """Génère toutes les cartes atomiques."""
        cards = []
        total = len(self.export.messages)
        
        print(f"\n🎨 Generating {total} atomic cards...")
        
        for idx, message in enumerate(self.export.messages):
            prev_msg = self.export.messages[idx - 1] if idx > 0 else None
            next_msg = self.export.messages[idx + 1] if idx < total - 1 else None
            
            card_path = self.generate_card(message, prev_msg, next_msg)
            cards.append(card_path)
            
            if (idx + 1) % 10 == 0:
                print(f"  ✓ Generated {idx + 1}/{total} cards")
        
        print(f"✅ All {total} cards generated!\n")
        return cards


class MOCGenerator:
    """Génère le Map Of Content (MOC) de la session."""
    
    def __init__(self, export: ChatExport, output_dir: Path, cards: List[Path]):
        self.export = export
        self.output_dir = output_dir
        self.cards = cards
        
    def generate(self) -> Path:
        """Génère le MOC."""
        stats = self.export.get_stats()
        
        # Nom du fichier MOC
        moc_filename = f"_MOC_{self.export.filepath.stem}.md"
        moc_path = self.output_dir / moc_filename
        
        # Frontmatter
        frontmatter = {
            'type': 'moc',
            'created': datetime.now().isoformat() + 'Z',
            'chat_id': stats['chat_id'],
            'title': stats['title'],
            'platform': stats['platform'],
            'messages_count': stats['total_messages'],
            'cards_generated': len(self.cards),
            'tags': ['moc', 'chat-export', 'session']
        }
        
        # Contenu
        content = f"""---
{yaml.dump(frontmatter, allow_unicode=True, sort_keys=False)}---

# 📊 MOC - {stats['title']}

> **Map of Content** pour cette session de conversation

---

## 📈 Statistiques

| Métrique | Valeur |
|----------|--------|
| 💬 Messages totaux | {stats['total_messages']} |
| 👤 Messages User | {stats['user_messages']} |
| 🤖 Messages Assistant | {stats['assistant_messages']} |
| 📎 Attachments | {stats['total_attachments']} |
| 🎴 Cartes générées | {len(self.cards)} |
| 📅 Début conversation | {stats.get('conversation_start', 'Unknown')} |
| 📅 Fin conversation | {stats.get('conversation_end', 'Unknown')} |
| 📅 Export date | {stats['exported']} |
| 🌐 Platform | {stats['platform']} |

---

## 🗂️ Tous les Messages

```dataview
TABLE WITHOUT ID
  file.link as "Message",
  role as "Rôle",
  order as "N°",
  attachments_count as "📎"
FROM "cards"
WHERE type = "chat-card"
  AND contains(parent_export, "{stats['title']}")
SORT order ASC
```

---

## 👤 Messages User

```dataview
TABLE WITHOUT ID
  file.link as "Message",
  order as "N°",
  topics as "Topics"
FROM "cards"
WHERE type = "chat-card"
  AND role = "user"
  AND contains(parent_export, "{stats['title']}")
SORT order ASC
```

---

## 🤖 Messages Assistant

```dataview
TABLE WITHOUT ID
  file.link as "Message",
  order as "N°",
  topics as "Topics"
FROM "cards"
WHERE type = "chat-card"
  AND role = "assistant"
  AND contains(parent_export, "{stats['title']}")
SORT order ASC
```

---

## 🏷️ Par Topic

```dataview
TABLE WITHOUT ID
  rows.file.link as "Messages",
  count(rows) as "Count"
FROM "cards"
WHERE type = "chat-card"
  AND contains(parent_export, "{stats['title']}")
FLATTEN tags as topic
GROUP BY topic
SORT count(rows) DESC
```

---

## 📎 Avec Attachments

```dataview
LIST
FROM "cards"
WHERE type = "chat-card"
  AND attachments_count > 0
  AND contains(parent_export, "{stats['title']}")
SORT order ASC
```

---

## 🔗 Liens

- **Export brut** : [[{self.export.filepath.stem}]]
- **Platform** : {stats['platform']}
- **Chat ID** : `{stats['chat_id']}`

---

## 🗓️ Timeline

**Début conversation :** {stats.get('date_start', 'Unknown')}  
**Fin conversation :** {stats.get('date_end', 'Unknown')}  
**Export date :** {stats['exported']}

---

**Generated by Chat Atomizer v1.0**  
**Total cards :** {len(self.cards)}  
**Created :** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
        
        # Sauvegarder
        moc_path.write_text(content, encoding='utf-8')
        
        print(f"✅ MOC generated: {moc_path.name}\n")
        
        return moc_path


def main():
    """Point d'entrée principal."""
    parser = argparse.ArgumentParser(
        description='Atomize chat exports into Obsidian cards',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python atomize_chat.py -i export.md -o vault/Chat-Exports/
  python atomize_chat.py --input chat.md --output ./output/ --dry-run
        """
    )
    
    parser.add_argument('-i', '--input', type=Path, required=True,
                       help='Path to the chat export markdown file')
    parser.add_argument('-o', '--output', type=Path, required=True,
                       help='Output directory for atomic cards')
    parser.add_argument('--dry-run', action='store_true',
                       help='Parse only, do not create files')
    
    args = parser.parse_args()
    
    # Vérifier input
    if not args.input.exists():
        print(f"❌ Error: Input file not found: {args.input}")
        return 1
    
    print("=" * 60)
    print("🚀 CHAT ATOMIZER v1.0")
    print("=" * 60)
    print(f"\n📄 Input: {args.input}")
    print(f"📂 Output: {args.output}")
    print(f"🔍 Dry run: {args.dry_run}\n")
    
    # Parser l'export
    print("📖 Parsing export...")
    export = ChatExport(args.input)
    
    # Afficher stats
    stats = export.get_stats()
    print(f"\n📊 Export Statistics:")
    print(f"  Title: {stats['title']}")
    print(f"  Total messages: {stats['total_messages']}")
    print(f"  User: {stats['user_messages']}")
    print(f"  Assistant: {stats['assistant_messages']}")
    print(f"  Attachments: {stats['total_attachments']}")
    
    if args.dry_run:
        print("\n✅ Dry run complete - no files created")
        return 0
    
    # Créer output directory
    session_dir = args.output / args.input.stem
    session_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"\n📁 Creating session directory: {session_dir}")
    
    # Générer cartes atomiques
    card_gen = AtomicCardGenerator(export, session_dir)
    cards = card_gen.generate_all_cards()
    
    # Générer MOC
    print("📊 Generating MOC...")
    moc_gen = MOCGenerator(export, session_dir, cards)
    moc_path = moc_gen.generate()
    
    # Résumé final
    print("=" * 60)
    print("✅ ATOMIZATION COMPLETE!")
    print("=" * 60)
    print(f"\n📊 Results:")
    print(f"  Cards created: {len(cards)}")
    print(f"  MOC created: {moc_path.name}")
    print(f"  Output directory: {session_dir}")
    print(f"\n🎉 All done! Open in Obsidian to explore.\n")
    
    return 0


if __name__ == '__main__':
    exit(main())