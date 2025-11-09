#!/usr/bin/env python3
"""
Chat to Cards - Complete Automation
====================================

Workflow complet : Export → Cartes → Post-processing

Usage:
    # Avec export existant
    python chat_to_cards.py \
      --input export.md \
      --output vault/Chat-Exports/Session-Name \
      --title "Session Title"
    
    # Mode automatique complet
    python chat_to_cards.py \
      --url "https://claude.ai/chat/xxx" \
      --output vault/Chat-Exports/Session-Name \
      --title "Session Title" \
      --auto-remove-duplicates

Author: Moncef
Date: 2025-11-09
"""

import argparse
import sys
from pathlib import Path
import shutil
import subprocess

# Import nos modules
from atomize_chat import ChatExport, AtomicCardGenerator, MOCGenerator
from postprocess_cards import (
    Card, 
    TitleGenerator, 
    CardRenamer, 
    DuplicateDetector,
    EnrichedMOCGenerator
)


class ChatToCardsOrchestrator:
    """Orchestre le workflow complet."""
    
    def __init__(self, args):
        self.args = args
        self.export_path = None
        self.session_dir = None
        self.cards = []
        
    def run(self):
        """Exécute le workflow complet."""
        print("=" * 70)
        print("🚀 CHAT TO CARDS - COMPLETE AUTOMATION")
        print("=" * 70)
        print()
        
        # Step 0: Vérifier input
        if not self._validate_input():
            return 1
        
        # Step 1: Atomisation
        if not self._atomize():
            return 1
        
        # Step 2: Détection doublons
        if not self._detect_duplicates():
            return 1
        
        # Step 3: Suppression doublons (si auto)
        if self.args.auto_remove_duplicates:
            if not self._remove_duplicates():
                return 1
        
        # Step 4: Renommage intelligent
        if not self._rename_cards():
            return 1
        
        # Step 5: Mise à jour liens inter-cartes
        if not self._update_links():
            return 1
        
        # Step 6: Génération MOC enrichi
        if not self._generate_enriched_moc():
            return 1
        
        # Step 7: Résumé final
        self._print_summary()
        
        print("\n" + "=" * 70)
        print("✅ WORKFLOW COMPLETE!")
        print("=" * 70)
        print(f"\n📂 Output: {self.session_dir}")
        print(f"🎉 Open in Obsidian to explore!\n")
        
        return 0
    
    def _validate_input(self) -> bool:
        """Valide les inputs."""
        print("📋 Step 0: Validation")
        print("-" * 70)
        
        # Vérifier input
        if self.args.url:
            print("⚠️  URL mode not yet implemented!")
            print("   Please use --input with exported .md file")
            print("\n   How to export:")
            print("   1. Open chat in browser")
            print("   2. Run chat-exporter-v1.4-FINAL.js in console")
            print("   3. Save to file")
            print("   4. Use --input flag\n")
            return False
        
        if not self.args.input:
            print("❌ No input provided. Use --input or --url")
            return False
        
        self.export_path = Path(self.args.input)
        if not self.export_path.exists():
            print(f"❌ Input file not found: {self.export_path}")
            return False
        
        print(f"✅ Input: {self.export_path}")
        print(f"✅ Output: {self.args.output}")
        print(f"✅ Title: {self.args.title}")
        print()
        
        return True
    
    def _atomize(self) -> bool:
        """Step 1: Atomisation."""
        print("📖 Step 1: Atomization")
        print("-" * 70)
        
        try:
            # Parser l'export
            export = ChatExport(self.export_path)
            
            if len(export.messages) == 0:
                print("❌ No messages found in export!")
                return False
            
            stats = export.get_stats()
            print(f"  Messages: {stats['total_messages']}")
            print(f"  User: {stats['user_messages']}")
            print(f"  Assistant: {stats['assistant_messages']}")
            
            # Extraire date de conversation pour nommer le dossier
            conversation_start = stats.get('conversation_start', '')
            if conversation_start and conversation_start != 'unknown':
                try:
                    from datetime import datetime
                    # Parser ISO format ou autre
                    if 'T' in conversation_start:
                        date_obj = datetime.fromisoformat(conversation_start.replace('Z', '+00:00'))
                    else:
                        date_obj = datetime.now()
                    date_str = date_obj.strftime('%Y-%m-%d')
                    print(f"  Conversation start: {conversation_start}")
                    print(f"  Using date: {date_str}")
                except:
                    date_str = datetime.now().strftime('%Y-%m-%d')
                    print(f"  Could not parse date, using today: {date_str}")
            else:
                from datetime import datetime
                date_str = datetime.now().strftime('%Y-%m-%d')
                print(f"  No conversation date, using today: {date_str}")
            
            # Créer session directory avec date de conversation
            if self.args.output.name.startswith('2025-') or self.args.output.name.startswith('2024-'):
                # L'utilisateur a déjà spécifié un nom avec date
                self.session_dir = Path(self.args.output)
            else:
                # Ajouter la date automatiquement
                session_name = f"{date_str}-{self.args.output.name}"
                self.session_dir = self.args.output.parent / session_name
            
            self.session_dir.mkdir(parents=True, exist_ok=True)
            
            # Générer cartes
            print("\n  Generating atomic cards...")
            card_gen = AtomicCardGenerator(export, self.session_dir)
            card_paths = card_gen.generate_all_cards()
            
            # Générer MOC basique
            print("  Generating basic MOC...")
            moc_gen = MOCGenerator(export, self.session_dir, card_paths)
            moc_gen.generate()
            
            print(f"✅ Atomization complete: {len(card_paths)} cards")
            print(f"   Session: {self.session_dir.name}\n")
            return True
            
        except Exception as e:
            print(f"❌ Atomization failed: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def _detect_duplicates(self) -> bool:
        """Step 2: Détection doublons."""
        print("🔍 Step 2: Duplicate Detection")
        print("-" * 70)
        
        try:
            # Charger cartes
            cards_dir = self.session_dir / 'cards'
            card_files = sorted(cards_dir.glob('*.md'))
            self.cards = [Card(f) for f in card_files]
            
            print(f"  Loaded {len(self.cards)} cards")
            
            # Détecter doublons
            threshold = self.args.duplicate_threshold
            duplicates = DuplicateDetector.find_duplicates(self.cards, threshold)
            
            if duplicates:
                print(f"\n  ⚠️  Found {len(duplicates)} potential duplicates:")
                for card1, card2, sim in duplicates:
                    print(f"    {card1.filepath.name} ↔ {card2.filepath.name} ({sim:.1%})")
                
                if not self.args.auto_remove_duplicates:
                    print("\n  💡 Use --auto-remove-duplicates to remove them automatically")
            else:
                print("  ✅ No duplicates found")
            
            print()
            return True
            
        except Exception as e:
            print(f"❌ Duplicate detection failed: {e}")
            return False
    
    def _remove_duplicates(self) -> bool:
        """Step 3: Suppression doublons."""
        print("🗑️  Step 3: Remove Duplicates")
        print("-" * 70)
        
        try:
            threshold = self.args.duplicate_threshold
            duplicates = DuplicateDetector.find_duplicates(self.cards, threshold)
            
            if not duplicates:
                print("  No duplicates to remove")
                print()
                return True
            
            removed_count = 0
            for card1, card2, sim in duplicates:
                # Garder la carte avec le plus petit ordre (première occurrence)
                if card1.order < card2.order:
                    to_remove = card2
                else:
                    to_remove = card1
                
                print(f"  Removing: {to_remove.filepath.name} (duplicate of order {min(card1.order, card2.order)})")
                to_remove.filepath.unlink()
                
                # Retirer de la liste
                self.cards = [c for c in self.cards if c.filepath != to_remove.filepath]
                removed_count += 1
            
            print(f"\n✅ Removed {removed_count} duplicates")
            print(f"  Remaining cards: {len(self.cards)}\n")
            return True
            
        except Exception as e:
            print(f"❌ Duplicate removal failed: {e}")
            return False
    
    def _rename_cards(self) -> bool:
        """Step 4: Renommage intelligent."""
        print("✏️  Step 4: Intelligent Renaming")
        print("-" * 70)
        
        try:
            renamed_count = 0
            rename_map = {}  # old_name -> new_name pour update liens
            
            for card in self.cards:
                # Générer titre
                title = TitleGenerator.generate(card)
                category = CardRenamer.categorize(card)
                new_filename = CardRenamer.generate_filename(card, title, category)
                
                old_name = card.filepath.name
                
                if old_name != new_filename:
                    new_path = card.filepath.parent / new_filename
                    
                    # Éviter conflits de noms
                    if new_path.exists():
                        # Ajouter suffixe
                        base = new_path.stem
                        new_filename = f"{base}-{card.order:03d}.md"
                        new_path = card.filepath.parent / new_filename
                    
                    # Sauvegarder mapping pour update liens
                    old_stem = card.filepath.stem
                    new_stem = new_path.stem
                    rename_map[old_stem] = new_stem
                    
                    # Renommer
                    card.filepath.rename(new_path)
                    card.filepath = new_path
                    
                    if renamed_count < 5:  # Afficher premiers renommages
                        print(f"  {old_name}")
                        print(f"  → {new_filename}")
                    
                    renamed_count += 1
            
            if renamed_count > 5:
                print(f"  ... and {renamed_count - 5} more")
            
            print(f"\n✅ Renamed {renamed_count} cards\n")
            
            # Sauvegarder rename map pour step suivant
            self.rename_map = rename_map
            return True
            
        except Exception as e:
            print(f"❌ Renaming failed: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def _update_links(self) -> bool:
        """Step 5: Mise à jour liens inter-cartes."""
        print("🔗 Step 5: Update Inter-card Links")
        print("-" * 70)
        
        try:
            if not hasattr(self, 'rename_map') or not self.rename_map:
                print("  No renames, links already correct")
                print()
                return True
            
            updated_count = 0
            
            for card in self.cards:
                content = card.filepath.read_text(encoding='utf-8')
                original_content = content
                
                # Remplacer tous les anciens noms par nouveaux
                for old_name, new_name in self.rename_map.items():
                    # Pattern: [[old_name]] ou [[old_name|alias]]
                    content = content.replace(f"[[{old_name}]]", f"[[{new_name}]]")
                    content = content.replace(f"[[{old_name}|", f"[[{new_name}|")
                
                # Sauvegarder si changé
                if content != original_content:
                    card.filepath.write_text(content, encoding='utf-8')
                    updated_count += 1
            
            print(f"  Updated links in {updated_count} cards")
            print()
            return True
            
        except Exception as e:
            print(f"❌ Link update failed: {e}")
            return False
    
    def _generate_enriched_moc(self) -> bool:
        """Step 6: MOC enrichi."""
        print("📊 Step 6: Generate Enriched MOC")
        print("-" * 70)
        
        try:
            moc_path = self.session_dir / f"_MOC_{self.args.title.replace(' ', '-')}.md"
            
            # Supprimer ancien MOC basique
            old_moc = list(self.session_dir.glob('_MOC_*.md'))
            for old in old_moc:
                if old != moc_path:
                    old.unlink()
            
            # Générer nouveau MOC enrichi
            EnrichedMOCGenerator.generate(self.cards, moc_path, self.args.title)
            
            print(f"  MOC: {moc_path.name}")
            print()
            return True
            
        except Exception as e:
            print(f"❌ MOC generation failed: {e}")
            return False
    
    def _print_summary(self) -> bool:
        """Affiche résumé final."""
        print("\n📈 Summary")
        print("-" * 70)
        
        # Stats
        user_count = len([c for c in self.cards if c.role == 'user'])
        assistant_count = len([c for c in self.cards if c.role == 'assistant'])
        
        questions = len([c for c in self.cards if CardRenamer.categorize(c) == 'Q'])
        responses = len([c for c in self.cards if CardRenamer.categorize(c) == 'R'])
        statements = len([c for c in self.cards if CardRenamer.categorize(c) == 'S'])
        
        print(f"  📦 Total cards: {len(self.cards)}")
        print(f"  👤 User messages: {user_count}")
        print(f"  🤖 Assistant messages: {assistant_count}")
        print()
        print(f"  ❓ Questions: {questions}")
        print(f"  💬 Responses: {responses}")
        print(f"  📝 Statements: {statements}")
        print()
        print(f"  📂 Location: {self.session_dir}")
        print(f"  📊 MOC: _MOC_{self.args.title.replace(' ', '-')}.md")
        
        return True


def main():
    """Point d'entrée."""
    parser = argparse.ArgumentParser(
        description='Complete chat-to-cards automation',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # With existing export
  python chat_to_cards.py \\
    --input export.md \\
    --output vault/Chat-Exports/Power-BI \\
    --title "Power BI Architecture"
  
  # With auto duplicate removal
  python chat_to_cards.py \\
    --input export.md \\
    --output vault/Chat-Exports/Power-BI \\
    --title "Power BI Architecture" \\
    --auto-remove-duplicates
        """
    )
    
    # Input
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument('-i', '--input', type=Path,
                            help='Path to exported markdown file')
    input_group.add_argument('-u', '--url', type=str,
                            help='Claude.ai chat URL (not yet implemented)')
    
    # Output
    parser.add_argument('-o', '--output', type=Path, required=True,
                       help='Output directory for cards')
    parser.add_argument('-t', '--title', type=str, required=True,
                       help='Session title')
    
    # Options
    parser.add_argument('--auto-remove-duplicates', action='store_true',
                       help='Automatically remove duplicate cards')
    parser.add_argument('--duplicate-threshold', type=float, default=0.85,
                       help='Duplicate similarity threshold (default: 0.85)')
    parser.add_argument('--dry-run', action='store_true',
                       help='Show what would be done without doing it')
    
    args = parser.parse_args()
    
    # Vérifier dry-run
    if args.dry_run:
        print("⚠️  DRY RUN MODE - No files will be modified")
        print()
    
    # Run orchestrator
    orchestrator = ChatToCardsOrchestrator(args)
    return orchestrator.run()


if __name__ == '__main__':
    exit(main())