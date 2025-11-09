#!/usr/bin/env python3
"""
Générateur de cartes Obsidian atomiques à partir du chat export Power BI / Tickets.
Crée une structure complète avec MOC, cartes atomiques et métadonnées.
"""

import json
import re
from pathlib import Path
from datetime import datetime
from typing import List, Dict

# ============================================================================
# CONFIGURATION
# ============================================================================

# Chemin de base (à ajuster selon ton système)
BASE_PATH = Path("/mnt/c/Users/idsmf/Projects/pkm-system/vault BACKUP/02_Projects/ChatToCards/")
EXPORT_FILE = Path("/mnt/c/Users/idsmf/Projects/pkm-system/export_conv.md")

# Structure cible
PROJECT_NAME = "Chats"
SESSION_NAME = "Ticket receipt data extraction"

# Tags canoniques (selon TAG_REGISTRY.md)
TAGS_CANONICAL = {
    'chat_card': 'chat-card',
    'finance': 'finance',
    'compta': 'compta',
    'receipt': 'receipt',
    'expense': 'expense',
    'python': 'python',
    'concept': 'concept',
    'moc': 'moc',
    'export': 'export',
    'raw': 'raw',
}

# ============================================================================
# FONCTIONS UTILITAIRES
# ============================================================================

def load_chat(file_path: Path) -> str:
    """Charge et déséchape le fichier export."""
    with open(file_path, 'r', encoding='utf-8') as f:
        raw = f.read()
    return json.loads(raw)

def extract_messages(content: str, start_msg: int = 36) -> List[Dict]:
    """Extrait les messages pertinents."""
    messages = []
    lines = content.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        if line.startswith('## ') and 'Message' in line:
            role_match = re.search(r'(User|Assistant)', line)
            num_match = re.search(r'Message (\d+)', line)
            
            if role_match and num_match:
                msg_num = int(num_match.group(1))
                role = role_match.group(1).lower()
                
                if msg_num < start_msg:
                    i += 1
                    continue
                
                # Trouver contenu
                content_start = i + 1
                content_end = i + 1
                
                for j in range(i + 1, len(lines)):
                    if lines[j].startswith('## ') and 'Message' in lines[j]:
                        content_end = j
                        break
                else:
                    content_end = len(lines)
                
                msg_content = '\n'.join(lines[content_start:content_end]).strip()
                
                # ID
                msg_id = ""
                if content_start < len(lines):
                    id_match = re.search(r'\*\*ID:\*\* (msg-\d+)', lines[content_start])
                    if id_match:
                        msg_id = id_match.group(1)
                
                messages.append({
                    'number': msg_num,
                    'role': role,
                    'id': msg_id,
                    'content': msg_content,
                    'length': len(msg_content)
                })
                
                i = content_end
        else:
            i += 1
    
    return messages

def clean_content(content: str) -> str:
    """Nettoie le contenu d'un message."""
    # Retirer les lignes ID et Attachments
    lines = content.split('\n')
    cleaned = []
    
    for line in lines:
        # Skip metadata lines
        if line.startswith('**ID:**') or line.startswith('**Attachments:**'):
            continue
        if line.startswith('- 📷 Image:') or line.startswith('- 📄 Document:'):
            continue
        if line == '---':
            continue
        cleaned.append(line)
    
    return '\n'.join(cleaned).strip()

def extract_attachments(content: str) -> List[str]:
    """Extrait les noms de fichiers attachés."""
    attachments = []
    attachments += re.findall(r'📷 Image: `([^`]+)`', content)
    attachments += re.findall(r'📄 Document: `([^`]+)`', content)
    return attachments

def detect_tags(content: str, role: str) -> List[str]:
    """Détecte automatiquement les tags pertinents."""
    tags = [TAGS_CANONICAL['chat_card']]
    
    content_lower = content.lower()
    
    # Finance / Compta
    if any(word in content_lower for word in ['ticket', 'caisse', 'reçu', 'dépense', 'prix', 'total']):
        tags.append(TAGS_CANONICAL['receipt'])
        tags.append(TAGS_CANONICAL['expense'])
    
    if any(word in content_lower for word in ['comptabilité', 'compta', 'budget', 'finance']):
        tags.append(TAGS_CANONICAL['compta'])
    
    # Python / Code
    if 'python' in content_lower or '```python' in content:
        tags.append(TAGS_CANONICAL['python'])
    
    # JSON / Data
    if 'json' in content_lower or '```json' in content:
        tags.append(TAGS_CANONICAL['export'])
    
    # Power BI
    if any(word in content_lower for word in ['power bi', 'power pivot', 'dax', 'dashboard']):
        tags.append('powerbi')  # Nouveau tag à ajouter au registry
    
    return list(set(tags))  # Déduplicate

def generate_card_title(msg: Dict, index: int) -> str:
    """Génère un titre temporaire pour la carte."""
    role_prefix = "Q" if msg['role'] == 'user' else "R"
    
    # Essayer de trouver un titre intelligent dans le contenu
    content = msg['content'][:500]
    
    # Chercher des patterns
    if msg['role'] == 'user':
        if 'extraction' in content.lower() or 'extraire' in content.lower():
            return f"{role_prefix}{index:03d}-Question-Extraction-Tickets"
        elif 'format' in content.lower() or 'json' in content.lower():
            return f"{role_prefix}{index:03d}-Question-Format-Donnees"
        else:
            return f"{role_prefix}{index:03d}-Question-User"
    else:
        if 'json' in content.lower() or '```json' in content:
            return f"{role_prefix}{index:03d}-Reponse-Structure-JSON"
        elif 'power bi' in content.lower() or 'dashboard' in content.lower():
            return f"{role_prefix}{index:03d}-Reponse-PowerBI-Architecture"
        else:
            return f"{role_prefix}{index:03d}-Reponse-Assistant"

def create_card_metadata(msg: Dict, card_title: str, attachments: List[str], tags: List[str]) -> str:
    """Crée le frontmatter YAML de la carte."""
    now = datetime.now().isoformat()
    
    metadata = [
        "---",
        f"created: {now}",
        f"updated: {now}",
        "type: chat-card",
        f"chat_message_id: {msg['id']}",
        f"chat_message_number: {msg['number']}",
        f"role: {msg['role']}",
        f"session: [[MOC-Session-{SESSION_NAME}]]",
        f"tags: [{', '.join(tags)}]",
    ]
    
    if attachments:
        metadata.append(f"attachments: {len(attachments)}")
    
    metadata.append("---")
    
    return '\n'.join(metadata)

def create_card_content(msg: Dict, card_title: str, index: int, total: int) -> str:
    """Crée le contenu complet de la carte."""
    metadata = create_card_metadata(
        msg, 
        card_title,
        extract_attachments(msg['content']),
        detect_tags(msg['content'], msg['role'])
    )
    
    content = clean_content(msg['content'])
    
    # Navigation
    prev_card = f"[[Card-{index-1:03d}]]" if index > 1 else ""
    next_card = f"[[Card-{index+1:03d}]]" if index < total else ""
    
    nav = []
    if prev_card:
        nav.append(f"← {prev_card}")
    nav.append(f"[[MOC-Session-{SESSION_NAME}|↑ Session]]")
    if next_card:
        nav.append(f"{next_card} →")
    
    navigation = " | ".join(nav)
    
    # Assemblage
    card = [
        metadata,
        "",
        f"# {card_title}",
        "",
        navigation,
        "",
        "---",
        "",
        content,
        "",
        "---",
        "",
        f"**Card {index}/{total}** | Message #{msg['number']} | Role: {msg['role']}",
    ]
    
    return '\n'.join(card)

def create_session_moc(messages: List[Dict], cards: List[str]) -> str:
    """Crée le MOC de session."""
    now = datetime.now().isoformat()
    
    user_count = len([m for m in messages if m['role'] == 'user'])
    assistant_count = len([m for m in messages if m['role'] == 'assistant'])
    
    metadata = [
        "---",
        f"created: {now}",
        f"updated: {now}",
        "type: moc",
        f"session: {SESSION_NAME}",
        "tags: [moc, chat-card, finance, compta, powerbi]",
        "---",
        "",
        f"# 🗺️ MOC - Session PowerBI Tickets de Caisse",
        "",
        f"> Session d'analyse et extraction de tickets de caisse pour Power BI",
        "",
        "---",
        "",
        "## 📊 Vue d'Ensemble",
        "",
        f"**Date:** {datetime.now().strftime('%Y-%m-%d')}  ",
        f"**Messages:** {len(messages)} ({user_count} user, {assistant_count} assistant)  ",
        f"**Cartes:** {len(cards)}  ",
        f"**Thème:** Extraction données tickets → Structure JSON → Architecture Power BI",
        "",
        "---",
        "",
        "## 🗂️ Structure de la Session",
        "",
        "### Questions / Problèmes",
        "",
    ]
    
    # Lister les questions
    for i, card in enumerate(cards, 1):
        msg = messages[i-1]
        if msg['role'] == 'user':
            preview = msg['content'][:80].replace('\n', ' ')
            metadata.append(f"- [[{card}|Q{i:02d}]] - {preview}...")
    
    metadata.extend([
        "",
        "### Réponses / Solutions",
        "",
    ])
    
    # Lister les réponses
    for i, card in enumerate(cards, 1):
        msg = messages[i-1]
        if msg['role'] == 'assistant':
            preview = msg['content'][:80].replace('\n', ' ')
            metadata.append(f"- [[{card}|R{i:02d}]] - {preview}...")
    
    metadata.extend([
        "",
        "---",
        "",
        "## 🔗 Cartes Complètes (ordre chronologique)",
        "",
    ])
    
    # Liste complète
    for i, card in enumerate(cards, 1):
        msg = messages[i-1]
        role_emoji = "👤" if msg['role'] == 'user' else "🤖"
        metadata.append(f"{i}. {role_emoji} [[{card}|Card {i:03d}]] (msg #{msg['number']})")
    
    metadata.extend([
        "",
        "---",
        "",
        "## 📂 Liens Projet",
        "",
        f"- [[MOC-{PROJECT_NAME}|↑ Projet Finance]]",
        "- [[TAG_REGISTRY|🏷️ Tags]]",
        "",
        "---",
        "",
        f"**Session:** `{SESSION_NAME}`  ",
        f"**Export:** Chat Claude.ai  ",
        f"**Parsing:** Script Python automatique",
    ])
    
    return '\n'.join(metadata)

def generate_structure_preview(messages: List[Dict], num_cards: int = 10) -> Dict:
    """Génère un aperçu de la structure qui sera créée."""
    cards = []
    
    for i, msg in enumerate(messages[:num_cards], 1):
        title = generate_card_title(msg, i)
        cards.append({
            'number': i,
            'title': title,
            'message': msg['number'],
            'role': msg['role'],
            'length': msg['length'],
            'tags': detect_tags(msg['content'], msg['role'])
        })
    
    return {
        'session_moc': f"MOC-Session-{SESSION_NAME}.md",
        'cards': cards,
        'total_messages': len(messages),
        'will_create': num_cards,
        'structure': {
            'base': f"02_Projects/{PROJECT_NAME}/",
            'session': f"Sessions/{SESSION_NAME}/",
            'cards_dir': f"Sessions/{SESSION_NAME}/Cards/",
        }
    }

# ============================================================================
# GÉNÉRATION DES FICHIERS
# ============================================================================

def create_all_files(messages: List[Dict], output_dir: Path, num_cards: int = 10, dry_run: bool = True):
    """Crée tous les fichiers (MOC + cartes)."""
    
    if not dry_run:
        # Créer structure
        session_dir = output_dir / "02_Projects" / PROJECT_NAME / "Sessions" / SESSION_NAME
        cards_dir = session_dir / "Cards"
        cards_dir.mkdir(parents=True, exist_ok=True)
    
    # Générer cartes
    card_files = []
    for i, msg in enumerate(messages[:num_cards], 1):
        card_title = generate_card_title(msg, i)
        card_filename = f"Card-{i:03d}-{card_title}.md"
        card_content = create_card_content(msg, card_title, i, num_cards)
        
        card_files.append(card_filename)
        
        if not dry_run:
            card_path = cards_dir / card_filename
            with open(card_path, 'w', encoding='utf-8') as f:
                f.write(card_content)
            print(f"✅ Créé: {card_path}")
    
    # Générer MOC
    moc_content = create_session_moc(messages[:num_cards], card_files)
    moc_filename = f"MOC-Session-{SESSION_NAME}.md"
    
    if not dry_run:
        moc_path = session_dir / moc_filename
        with open(moc_path, 'w', encoding='utf-8') as f:
            f.write(moc_content)
        print(f"✅ Créé: {moc_path}")
    
    return {
        'moc': moc_filename,
        'cards': card_files,
        'session_dir': session_dir if not dry_run else None
    }

# ============================================================================
# MAIN
# ============================================================================

def main():
    print("=" * 80)
    print("🎯 GÉNÉRATEUR DE CARTES OBSIDIAN - Power BI / Tickets")
    print("=" * 80)
    
    # Charger
    print("\n📂 Chargement du chat export...")
    content = load_chat(EXPORT_FILE)
    print(f"✅ Chargé ({len(content)} caractères)")
    
    # Extraire
    print("\n💬 Extraction messages pertinents...")
    messages = extract_messages(content, start_msg=36)
    print(f"✅ {len(messages)} messages extraits")
    
    # Aperçu structure
    print("\n🗂️ APERÇU DE LA STRUCTURE À CRÉER")
    print("-" * 80)
    
    preview = generate_structure_preview(messages, num_cards=10)
    
    print(f"\n📁 Structure:")
    print(f"   {preview['structure']['base']}")
    print(f"   └── {preview['structure']['session']}")
    print(f"       ├── {preview['session_moc']}")
    print(f"       └── Cards/")
    print(f"           ├── {preview['cards'][0]['title']}.md")
    print(f"           ├── {preview['cards'][1]['title']}.md")
    print(f"           └── ... ({len(preview['cards'])} cartes)")
    
    print(f"\n💎 Aperçu des 5 premières cartes:")
    print("-" * 80)
    
    for card in preview['cards'][:5]:
        role_emoji = "👤" if card['role'] == 'user' else "🤖"
        tags_str = ', '.join(card['tags'][:3])
        print(f"\n{card['number']}. {role_emoji} {card['title']}")
        print(f"   Message: #{card['message']} | Longueur: {card['length']} chars")
        print(f"   Tags: {tags_str}")
    
    # Choix utilisateur
    print("\n\n" + "=" * 80)
    print("🎲 OPTIONS")
    print("=" * 80)
    print("\n1. DRY RUN - Aperçu détaillé (pas de création fichiers)")
    print("2. CRÉER 5 premières cartes (test)")
    print("3. CRÉER 10 premières cartes")
    print("4. CRÉER TOUTES les cartes (106 messages)")
    print("5. Annuler")
    
    choice = input("\n👉 Ton choix (1-5): ").strip()
    
    if choice == '1':
        print("\n📋 DRY RUN - Génération aperçu détaillé...")
        detailed = generate_structure_preview(messages, num_cards=10)
        
        print("\n📄 Contenu MOC (aperçu):")
        moc_preview = create_session_moc(messages[:10], [c['title'] for c in detailed['cards']])
        print(moc_preview[:500] + "\n...")
        
        print("\n📄 Première carte (aperçu):")
        card_preview = create_card_content(messages[0], detailed['cards'][0]['title'], 1, 10)
        print(card_preview[:500] + "\n...")
        
    elif choice == '2':
        print("\n🚀 Création de 5 cartes...")
        result = create_all_files(messages, BASE_PATH, num_cards=5, dry_run=False)
        print(f"\n✅ Terminé ! Fichiers dans: {result['session_dir']}")
        
    elif choice == '3':
        print("\n🚀 Création de 10 cartes...")
        result = create_all_files(messages, BASE_PATH, num_cards=10, dry_run=False)
        print(f"\n✅ Terminé ! Fichiers dans: {result['session_dir']}")
        
    elif choice == '4':
        confirm = input("\n⚠️  Créer 106 cartes ? (y/n): ").strip().lower()
        if confirm == 'y':
            print("\n🚀 Création de TOUTES les cartes...")
            result = create_all_files(messages, BASE_PATH, num_cards=len(messages), dry_run=False)
            print(f"\n✅ Terminé ! {len(messages)} cartes créées dans: {result['session_dir']}")
        else:
            print("\n❌ Annulé")
    else:
        print("\n❌ Annulé")
    
    print("\n" + "=" * 80)
    print("✅ FIN DU SCRIPT")
    print("=" * 80)

if __name__ == "__main__":
    main()
