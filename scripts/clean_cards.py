#!/usr/bin/env python3
"""
Card Cleaner v1.0
==================

Nettoie le formatage des cartes générées :
- Enlève caractères parasites dans noms de fichiers
- Remplace \\n\\n littéraux par vrais sauts de ligne
- Corrige autres problèmes de formatage

Usage:
    # Nettoyer un dossier de cartes
    python clean_cards.py --input cards/
    
    # Dry-run (voir ce qui serait changé)
    python clean_cards.py --input cards/ --dry-run
    
    # Utilisé par chat_to_cards.py automatiquement
"""

import re
import argparse
from pathlib import Path
from typing import List, Tuple


class CardCleaner:
    """Nettoie le formatage des cartes."""
    
    def __init__(self, cards_dir: Path, dry_run: bool = False):
        self.cards_dir = cards_dir
        self.dry_run = dry_run
        self.stats = {
            'files_renamed': 0,
            'files_cleaned': 0,
            'total_files': 0
        }
    
    def clean_filename(self, filename: str) -> str:
        """
        Nettoie un nom de fichier.
        
        Problèmes corrigés:
        - Card-001-Q001-NTitre.md → Card-001-Q001-Titre.md
        - Caractères N parasites après le numéro
        """
        # Pattern: Card-XXX-YXXX-NTitre.md
        # Enlever le N juste après le numéro de catégorie
        pattern = r'(Card-\d{3}-[QRS]\d{3}-)N([A-Z].*\.md)'
        
        if re.match(pattern, filename):
            cleaned = re.sub(pattern, r'\1\2', filename)
            return cleaned
        
        return filename
    
    def clean_content(self, content: str) -> str:
        """
        Nettoie le contenu d'une carte.
        
        Problèmes corrigés:
        - \\n\\n littéraux → vrais sauts de ligne
        - \\n littéral → vrai saut de ligne
        - Espaces multiples
        - Lignes vides excessives
        """
        cleaned = content
        
        # 1. Remplacer \n\n littéraux par vrais sauts de ligne
        cleaned = cleaned.replace('\\n\\n', '\n\n')
        
        # 2. Remplacer \n littéraux par vrais sauts de ligne
        cleaned = cleaned.replace('\\n', '\n')
        
        # 3. Supprimer espaces en fin de ligne
        cleaned = re.sub(r' +\n', '\n', cleaned)
        
        # 4. Limiter les lignes vides consécutives (max 2)
        cleaned = re.sub(r'\n{4,}', '\n\n\n', cleaned)
        
        # 5. Supprimer espaces multiples (mais garder indentation)
        # Uniquement dans le contenu, pas dans les code blocks
        lines = cleaned.split('\n')
        cleaned_lines = []
        in_code_block = False
        
        for line in lines:
            # Détecter code blocks
            if line.strip().startswith('```'):
                in_code_block = not in_code_block
            
            # Nettoyer uniquement si pas dans code block
            if not in_code_block:
                # Réduire espaces multiples (garder 1)
                line = re.sub(r'  +', ' ', line)
            
            cleaned_lines.append(line)
        
        cleaned = '\n'.join(cleaned_lines)
        
        return cleaned
    
    def clean_card(self, filepath: Path) -> Tuple[bool, bool]:
        """
        Nettoie une carte (nom + contenu).
        
        Returns:
            (renamed, content_changed)
        """
        renamed = False
        content_changed = False
        
        # 1. Nettoyer nom de fichier
        old_name = filepath.name
        new_name = self.clean_filename(old_name)
        
        if old_name != new_name:
            renamed = True
            new_path = filepath.parent / new_name
            
            if not self.dry_run:
                filepath.rename(new_path)
                filepath = new_path  # Update path for content cleaning
            
            print(f"  📝 Rename: {old_name}")
            print(f"          → {new_name}")
        
        # 2. Nettoyer contenu
        if not self.dry_run or not renamed:
            # Utiliser le bon chemin
            file_to_read = filepath if not renamed or not self.dry_run else filepath.parent / new_name
            
            try:
                original_content = filepath.read_text(encoding='utf-8')
                cleaned_content = self.clean_content(original_content)
                
                if original_content != cleaned_content:
                    content_changed = True
                    
                    if not self.dry_run:
                        filepath.write_text(cleaned_content, encoding='utf-8')
                    
                    # Compter différences
                    literal_newlines = original_content.count('\\n')
                    if literal_newlines > 0:
                        print(f"  ✂️  Clean: {filepath.name} ({literal_newlines} \\n found)")
            except Exception as e:
                print(f"  ❌ Error reading {filepath.name}: {e}")
        
        return renamed, content_changed
    
    def clean_all(self) -> dict:
        """Nettoie toutes les cartes du dossier."""
        
        if not self.cards_dir.exists():
            print(f"❌ Directory not found: {self.cards_dir}")
            return self.stats
        
        card_files = list(self.cards_dir.glob('*.md'))
        self.stats['total_files'] = len(card_files)
        
        if len(card_files) == 0:
            print(f"⚠️  No .md files found in {self.cards_dir}")
            return self.stats
        
        print(f"\n🧹 Cleaning {len(card_files)} cards...")
        if self.dry_run:
            print("   (DRY RUN - no changes will be made)\n")
        else:
            print()
        
        for filepath in card_files:
            renamed, content_changed = self.clean_card(filepath)
            
            if renamed:
                self.stats['files_renamed'] += 1
            if content_changed:
                self.stats['files_cleaned'] += 1
        
        return self.stats
    
    def print_summary(self):
        """Affiche le résumé."""
        print("\n" + "=" * 60)
        print("📊 CLEANING SUMMARY")
        print("=" * 60)
        print(f"\n  Total files: {self.stats['total_files']}")
        print(f"  Files renamed: {self.stats['files_renamed']}")
        print(f"  Content cleaned: {self.stats['files_cleaned']}")
        
        if self.dry_run:
            print("\n  ⚠️  DRY RUN - No actual changes made")
        else:
            print("\n  ✅ Changes applied")
        
        print()


def main():
    """Point d'entrée CLI."""
    parser = argparse.ArgumentParser(
        description='Clean card formatting issues',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Clean cards in directory
  python clean_cards.py --input cards/
  
  # Dry run (preview changes)
  python clean_cards.py --input cards/ --dry-run
  
  # Clean specific session
  python clean_cards.py --input Sessions/2025-11-09-Power-BI/cards/
        """
    )
    
    parser.add_argument('-i', '--input', type=Path, required=True,
                       help='Input cards directory')
    parser.add_argument('--dry-run', action='store_true',
                       help='Show what would be done without doing it')
    
    args = parser.parse_args()
    
    # Vérifier si input est un dossier ou fichier
    if args.input.is_file():
        args.input = args.input.parent
    
    print("=" * 60)
    print("🧹 CARD CLEANER v1.0")
    print("=" * 60)
    print(f"\n📂 Input: {args.input}")
    
    # Nettoyer
    cleaner = CardCleaner(args.input, dry_run=args.dry_run)
    cleaner.clean_all()
    cleaner.print_summary()
    
    return 0


if __name__ == '__main__':
    exit(main())
