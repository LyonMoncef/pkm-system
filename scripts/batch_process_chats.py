#!/usr/bin/env python3
"""
Batch Chat Processor
====================

Traite tous les chats d'un dossier en batch.
"""

from pathlib import Path
import subprocess
import sys

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
    
    for idx, chat_file in enumerate(chat_files, 1):
        print(f"[{idx}/{total}] Processing: {chat_file.name}")
        
        try:
            # Appeler chat_to_cards.py
            result = subprocess.run([
                'python3', 'scripts/chat-atomizer/chat_to_cards.py',
                '--input', str(chat_file),
                '--output', str(output_base),
                '--auto-clean'
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                success += 1
                print(f"  ✅ Success\n")
            else:
                failed += 1
                print(f"  ❌ Failed: {result.stderr}\n")
        
        except Exception as e:
            failed += 1
            print(f"  ❌ Error: {e}\n")
    
    print(f"\n{'='*60}")
    print(f"📊 BATCH SUMMARY")
    print(f"{'='*60}")
    print(f"  Total: {total}")
    print(f"  Success: {success}")
    print(f"  Failed: {failed}")
    print(f"\n📂 Output: {output_base}")

if __name__ == '__main__':
    input_dir = Path("/mnt/c/Users/idsmf/Projects/pkm-system/vault BACKUP/04_Resources/Chat-Exports/Sessions")
    output_base = Path("/mnt/c/Users/idsmf/Projects/pkm-system/vault/02_Projects/PKM-SYSTEM/Sessions")
    
    batch_process(input_dir, output_base)
