#!/usr/bin/env python3
"""
Chat Cards Post-Processor v1.0
================================

Post-traite les cartes générées par atomize_chat.py :
- Génère des titres intelligents
- Renomme les fichiers avec convention claire
- Détecte et élimine doublons
- Génère MOC structuré enrichi

Usage:
    python postprocess_cards.py --input cards_dir/
"""

import re
import argparse
from pathlib import Path
from typing import List, Dict, Tuple
import yaml
from difflib import SequenceMatcher


class Card:
    """Représente une carte atomique."""
    
    def __init__(self, filepath: Path):
        self.filepath = filepath
        self.content = filepath.read_text(encoding='utf-8')
        self.frontmatter = {}
        self.title = ""
        self.body = ""
        self._parse()
        
    def _parse(self):
        """Parse le fichier de carte."""
        # Extraire frontmatter
        yaml_match = re.match(r'^---\n(.*?)\n---\n(.*)$', self.content, re.DOTALL)
        if yaml_match:
            self.frontmatter = yaml.safe_load(yaml_match.group(1))
            self.body = yaml_match.group(2).strip()
            
            # Extraire le titre (première ligne #)
            title_match = re.search(r'^# (.+)$', self.body, re.MULTILINE)
            if title_match:
                self.title = title_match.group(1)
    
    @property
    def order(self) -> int:
        return self.frontmatter.get('order', 0)
    
    @property
    def role(self) -> str:
        return self.frontmatter.get('role', 'unknown')
    
    @property
    def content_text(self) -> str:
        """Contenu principal sans métadonnées."""
        # Extraire section Content
        content_match = re.search(r'## 💬 Content\n\n(.+?)(?=\n## |$)', self.body, re.DOTALL)
        if content_match:
            return content_match.group(1).strip()
        return self.body


class TitleGenerator:
    """Génère des titres intelligents pour les cartes."""
    
    @staticmethod
    def generate(card: Card) -> str:
        """Génère un titre basé sur le contenu."""
        content = card.content_text
        
        # Stratégie 1: Chercher une question explicite
        if card.role == 'user':
            # Détecter questions
            question_patterns = [
                r'(?:comment|pourquoi|quand|où|qui|quoi|est-ce que)\s+(.{10,60})\?',
                r'(.{10,50})\?',
                r'^(.{10,60})$'  # Première ligne courte
            ]
            
            for pattern in question_patterns:
                match = re.search(pattern, content[:200], re.IGNORECASE | re.MULTILINE)
                if match:
                    title = match.group(1).strip()
                    return TitleGenerator._clean_title(title)
        
        # Stratégie 2: Extraire mots-clés principaux
        # Prendre les 5 premiers mots significatifs
        words = re.findall(r'\b[A-Za-zÀ-ÿ]{4,}\b', content[:300])
        if words:
            keywords = ' '.join(words[:5])
            return TitleGenerator._clean_title(keywords)
        
        # Fallback: Premiers mots
        first_words = ' '.join(content.split()[:8])
        return TitleGenerator._clean_title(first_words)
    
    @staticmethod
    def _clean_title(title: str) -> str:
        """Nettoie et formate un titre."""
        # Enlever caractères spéciaux
        title = re.sub(r'[^\w\s\-àâäéèêëïîôùûüÿæœç]', '', title)
        
        # Capitaliser première lettre
        title = title[0].upper() + title[1:] if title else title
        
        # Tronquer si trop long
        if len(title) > 60:
            title = title[:57] + '...'
        
        return title


class DuplicateDetector:
    """Détecte les cartes en doublon."""
    
    @staticmethod
    def similarity(text1: str, text2: str) -> float:
        """Calcule similarité entre deux textes (0-1)."""
        return SequenceMatcher(None, text1, text2).ratio()
    
    @staticmethod
    def find_duplicates(cards: List[Card], threshold: float = 0.85) -> List[Tuple[Card, Card]]:
        """Trouve les paires de cartes similaires."""
        duplicates = []
        
        for i, card1 in enumerate(cards):
            for card2 in cards[i+1:]:
                sim = DuplicateDetector.similarity(
                    card1.content_text,
                    card2.content_text
                )
                
                if sim >= threshold:
                    duplicates.append((card1, card2, sim))
        
        return duplicates


class CardRenamer:
    """Renomme les cartes avec convention intelligente."""
    
    @staticmethod
    def generate_filename(card: Card, title: str, category: str) -> str:
        """
        Génère nom de fichier.
        
        Format: Card-{order:03d}-{category}{num}-{title-slug}.md
        
        Exemples:
        - Card-001-Q001-Extraction-Tickets.md (Question)
        - Card-002-R001-Structure-JSON.md (Réponse)
        - Card-003-Q002-Format-CSV.md (Question)
        """
        order = card.order
        
        # Slugify title
        slug = re.sub(r'[^\w\s\-]', '', title)
        slug = re.sub(r'[\s_]+', '-', slug)
        slug = slug[:40]  # Limiter longueur
        
        # Compter le numéro dans la catégorie
        # (simplifié ici, pourrait être amélioré)
        cat_num = order
        
        filename = f"Card-{order:03d}-{category}{cat_num:03d}-{slug}.md"
        
        return filename
    
    @staticmethod
    def categorize(card: Card) -> str:
        """Détermine catégorie de la carte."""
        if card.role == 'user':
            # Détecter si c'est une question
            content = card.content_text.lower()
            if '?' in content[:100] or any(q in content[:50] for q in ['comment', 'pourquoi', 'quand']):
                return 'Q'  # Question
            else:
                return 'S'  # Statement/Affirmation
        else:
            return 'R'  # Réponse


class EnrichedMOCGenerator:
    """Génère un MOC enrichi structuré."""
    
    @staticmethod
    def generate(cards: List[Card], output_path: Path, session_title: str):
        """Génère MOC enrichi."""
        
        # Grouper par catégorie
        questions = [c for c in cards if CardRenamer.categorize(c) == 'Q']
        responses = [c for c in cards if CardRenamer.categorize(c) == 'R']
        statements = [c for c in cards if CardRenamer.categorize(c) == 'S']
        
        user_count = len([c for c in cards if c.role == 'user'])
        assistant_count = len([c for c in cards if c.role == 'assistant'])
        
        # Construire le MOC
        moc = f"""---
type: moc
created: {cards[0].frontmatter.get('created', '')}
session_title: "{session_title}"
messages_count: {len(cards)}
questions_count: {len(questions)}
responses_count: {len(responses)}
tags: [moc, session, chat-export]
---

# MOC - {session_title}

> Session d'analyse et extraction de tickets de caisse pour Power BI

---

## 📊 Vue d'Ensemble

**Date:** {cards[0].frontmatter.get('created', 'Unknown')[:10]}  
**Messages:** {len(cards)} ({user_count} user, {assistant_count} assistant)  
**Cartes:** {len(cards)}  
**Thème:** {session_title}

---

## 🗂️ Structure de la Session

### Questions / Problèmes

"""
        
        # Ajouter les questions
        for card in questions[:50]:  # Limiter pour lisibilité
            title = TitleGenerator.generate(card)
            filename = CardRenamer.generate_filename(card, title, 'Q')
            
            # Extrait de contenu
            excerpt = card.content_text[:100].replace('\n', ' ')
            
            msg_id = card.frontmatter.get('msg_id', f"msg-{card.order}")
            order_num = card.order
            
            # Créer l'alias
            alias = f"Q{order_num:02d}"
            
            moc += f"- [[{filename}|{alias}]] - **ID:** {msg_id}  {excerpt}...\n"
        
        moc += "\n### Réponses / Analyses\n\n"
        
        # Ajouter les réponses (limité)
        for card in responses[:30]:
            title = TitleGenerator.generate(card)
            filename = CardRenamer.generate_filename(card, title, 'R')
            
            excerpt = card.content_text[:100].replace('\n', ' ')
            msg_id = card.frontmatter.get('msg_id', f"msg-{card.order}")
            order_num = card.order
            alias = f"R{order_num:02d}"
            
            moc += f"- [[{filename}|{alias}]] - **ID:** {msg_id}  {excerpt}...\n"
        
        moc += "\n---\n\n"
        moc += "## 📈 Statistiques\n\n"
        moc += f"- **Total cartes:** {len(cards)}\n"
        moc += f"- **Questions:** {len(questions)}\n"
        moc += f"- **Réponses:** {len(responses)}\n"
        moc += f"- **Statements:** {len(statements)}\n"
        
        # Écrire le MOC
        output_path.write_text(moc, encoding='utf-8')
        
        print(f"✅ MOC enrichi généré: {output_path.name}")


def main():
    """Point d'entrée."""
    parser = argparse.ArgumentParser(description='Post-process atomic cards')
    parser.add_argument('-i', '--input', type=Path, required=True,
                       help='Input cards directory')
    parser.add_argument('--rename', action='store_true',
                       help='Rename cards with intelligent titles')
    parser.add_argument('--detect-duplicates', action='store_true',
                       help='Detect and report duplicates')
    parser.add_argument('--generate-moc', action='store_true',
                       help='Generate enriched MOC')
    parser.add_argument('--similarity-threshold', type=float, default=0.85,
                       help='Duplicate detection threshold (0-1)')
    parser.add_argument('--session-title', type=str, default='Session Chat',
                       help='Session title for MOC')
    
    args = parser.parse_args()
    
    cards_dir = args.input / 'cards' if (args.input / 'cards').exists() else args.input
    
    if not cards_dir.exists():
        print(f"❌ Cards directory not found: {cards_dir}")
        return 1
    
    print("=" * 60)
    print("🔄 CHAT CARDS POST-PROCESSOR")
    print("=" * 60)
    print(f"\n📂 Input: {cards_dir}")
    
    # Charger toutes les cartes
    print("\n📖 Loading cards...")
    card_files = sorted(cards_dir.glob('*.md'))
    cards = [Card(f) for f in card_files if not f.name.startswith('_MOC')]
    
    print(f"✅ Loaded {len(cards)} cards")
    
    # Détection de doublons
    if args.detect_duplicates:
        print(f"\n🔍 Detecting duplicates (threshold: {args.similarity_threshold})...")
        duplicates = DuplicateDetector.find_duplicates(cards, args.similarity_threshold)
        
        if duplicates:
            print(f"\n⚠️  Found {len(duplicates)} potential duplicates:")
            for card1, card2, sim in duplicates:
                print(f"  {card1.filepath.name} ↔ {card2.filepath.name} (similarity: {sim:.2%})")
        else:
            print("✅ No duplicates found")
    
    # Renommage
    if args.rename:
        print("\n✏️  Generating intelligent titles and renaming...")
        
        for card in cards:
            title = TitleGenerator.generate(card)
            category = CardRenamer.categorize(card)
            new_filename = CardRenamer.generate_filename(card, title, category)
            new_path = card.filepath.parent / new_filename
            
            if card.filepath.name != new_filename:
                print(f"  {card.filepath.name} → {new_filename}")
                card.filepath.rename(new_path)
                card.filepath = new_path
        
        print("✅ Renaming complete")
    
    # Génération MOC enrichi
    if args.generate_moc:
        print("\n📊 Generating enriched MOC...")
        moc_path = args.input / f"_MOC_{args.session_title.replace(' ', '-')}.md"
        EnrichedMOCGenerator.generate(cards, moc_path, args.session_title)
    
    print("\n" + "=" * 60)
    print("✅ POST-PROCESSING COMPLETE")
    print("=" * 60 + "\n")
    
    return 0


if __name__ == '__main__':
    exit(main())