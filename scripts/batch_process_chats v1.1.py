#!/usr/bin/env python3
"""
Batch Chat Processor v1.1
==========================

Traite tous les chats d'un dossier en batch.
Auto-détecte le titre depuis le nom du fichier.
"""

from pathlib import Path
import subprocess
import sys


def extract_title(chat_file: Path) -> str:
    """
    Extrait le titre d'un fichier de chat.
    
    Priorités:
    1. Nom du dossier parent (si structure: Titre/Titre.md)
    2. Nom du fichier sans extension
    """
    # Si structure: Sessions/Titre/Titre.md
    # Utiliser le nom du dossier parent
    parent_name = chat_file.parent.name
    file_stem = chat_file.stem
    
    # Si le nom du dossier parent != "Sessions"
    # et ressemble au titre (pas juste un timestamp)
    if parent_name != "Sessions" and not parent_name.startswith("20"):
        title = parent_name
    else:
        title = file_stem
    
    return title


def batch_process(input_dir: Path, output_base: Path):
    """Traite tous les chats d'un dossier."""
    
    # Trouver tous les .md et .txt
    chat_files = []
    for ext in ['*.md', '*.txt']:
        chat_files.extend(input_dir.rglob(ext))
    
    total = len(chat_files)
    
    print(f"🎯 BATCH PROCESSING CHATS")
    print(f"==========================\n")
    print(f"📊 Found {total} chat files to process\n")
    
    success = 0
    failed = 0
    errors = []
    
    for idx, chat_file in enumerate(chat_files, 1):
        # Extraire titre
        title = extract_title(chat_file)
        
        print(f"[{idx}/{total}] Processing: {chat_file.name}")
        print(f"  📝 Title: {title}")
        
        try:
            # Appeler chat_to_cards.py
            result = subprocess.run([
                'python3', 'scripts/chat-atomizer/chat_to_cards.py',
                '--input', str(chat_file),
                '--output', str(output_base),
                '--title', title,
                '--auto-remove-duplicates'
            ], capture_output=True, text=True, check=False)
            
            if result.returncode == 0:
                success += 1
                print(f"  ✅ Success\n")
            else:
                failed += 1
                error_msg = result.stderr.strip().split('\n')[-1]  # Dernière ligne
                print(f"  ❌ Failed: {error_msg}\n")
                errors.append((chat_file.name, error_msg))
        
        except Exception as e:
            failed += 1
            print(f"  ❌ Error: {e}\n")
            errors.append((chat_file.name, str(e)))
    
    print(f"\n{'='*60}")
    print(f"📊 BATCH SUMMARY")
    print(f"{'='*60}")
    print(f"  Total: {total}")
    print(f"  Success: {success}")
    print(f"  Failed: {failed}")
    
    if errors:
        print(f"\n❌ ERRORS:")
        for filename, error in errors:
            print(f"  - {filename}: {error}")
    
    print(f"\n📂 Output: {output_base}")


if __name__ == '__main__':
    # Ajuster ces chemins selon ton setup
    input_dir = Path("vault BACKUP/04_Resources/Chat-Exports/Sessions")
    output_base = Path("vault/02_Projects/PKM-SYSTEM/Sessions")
    
    if not input_dir.exists():
        print(f"❌ Input directory not found: {input_dir}")
        sys.exit(1)
    
    output_base.mkdir(parents=True, exist_ok=True)
    
    batch_process(input_dir, output_base)
