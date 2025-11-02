#!/usr/bin/env python3
"""
Script de migration automatique des tags Obsidian - VERSION 2
Gère FRONTMATTER + TAGS INLINE dans le texte
"""

import os
import re
import yaml
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Set, Tuple

# ============================================================================
# CONFIGURATION
# ============================================================================

# VAULT_PATH relatif au repo
SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent
VAULT_PATH = REPO_ROOT / "vault"

BACKUP_SUFFIX = ".backup"
DRY_RUN = True  # True = simulation, False = vraie migration

# ============================================================================
# MAPPING DE MIGRATION
# ============================================================================

TAG_MIGRATIONS = {
    # Casse
    'Electron': 'electron',
    'Milestone': 'milestone',
    'BuildInPublic': 'build-in-public',
    'PKM': 'pkm',
    'JavaScript': 'javascript',
    'OpenSource': 'open-source',
    'ProductivityTools': 'productivity-tools',
    'DesktopApp': 'desktop-app',
    'KnowledgeManagement': 'knowledge-management',
    'Windows': 'windows',
    'MVP': 'mvp',
    
    # Singulier/Pluriel
    'shortcuts': 'shortcut',
    
    # Merge synonymes
    'global': 'layer-1',
    'projet': 'project',
}

# Tags à supprimer complètement (erreurs)
TAGS_TO_DELETE = [
    'Ctrl Space - Split Horizontal',
    'Ctrl Space % - Split Vertical',
]

# ============================================================================
# FONCTIONS
# ============================================================================

def extract_frontmatter(content: str) -> Tuple:
    """
    Extrait le frontmatter YAML d'un fichier markdown
    Retourne: (frontmatter_dict, start_pos, end_pos)
    """
    match = re.search(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not match:
        return None, 0, 0
    
    try:
        frontmatter = yaml.safe_load(match.group(1))
        return frontmatter, match.start(), match.end()
    except yaml.YAMLError as e:
        print(f"  ⚠️  YAML Error: {e}")
        return None, 0, 0


def migrate_tag(tag: str) -> str:
    """
    Migre un seul tag selon le mapping
    Retourne le nouveau tag ou None si à supprimer
    """
    # Nettoyer le tag (enlever # si présent)
    clean_tag = tag.lstrip('#')
    
    # Supprimer les tags à delete
    if clean_tag in TAGS_TO_DELETE:
        return None
    
    # Appliquer migration
    if clean_tag in TAG_MIGRATIONS:
        return TAG_MIGRATIONS[clean_tag]
    
    return clean_tag


def migrate_tags_list(tags: List[str]) -> Tuple[List[str], bool]:
    """
    Migre une liste de tags selon le mapping
    Retourne: (new_tags, changed)
    """
    if not tags:
        return [], False
    
    new_tags = []
    changed = False
    
    for tag in tags:
        new_tag = migrate_tag(tag)
        if new_tag is None:
            changed = True
            continue
        
        if new_tag != tag.lstrip('#'):
            changed = True
        
        new_tags.append(new_tag)
    
    # Dédupliquer et trier
    new_tags = sorted(list(set(new_tags)))
    
    return new_tags, changed


def find_inline_tags(content: str) -> List[Tuple[str, int, int]]:
    """
    Trouve tous les tags inline (#Tag) dans le contenu
    Retourne: [(tag, start_pos, end_pos), ...]
    """
    # Pattern pour tags inline: #Mot (commence par majuscule ou minuscule, peut contenir tirets)
    pattern = r'#([A-Za-z][A-Za-z0-9-]*)'
    
    matches = []
    for match in re.finditer(pattern, content):
        tag = match.group(1)
        matches.append((tag, match.start(), match.end()))
    
    return matches


def migrate_inline_tags(content: str) -> Tuple[str, bool, List[str], List[str]]:
    """
    Migre tous les tags inline dans le contenu
    Retourne: (new_content, changed, old_tags, new_tags)
    """
    inline_tags = find_inline_tags(content)
    
    if not inline_tags:
        return content, False, [], []
    
    # Collecter les anciens tags
    old_tags = [tag for tag, _, _ in inline_tags]
    
    # Remplacer de la fin vers le début (pour ne pas décaler les positions)
    new_content = content
    changed = False
    replacements = []
    
    for tag, start, end in reversed(inline_tags):
        new_tag = migrate_tag(tag)
        
        if new_tag is None:
            # Supprimer le tag
            # Supprimer aussi l'espace avant si présent
            if start > 0 and new_content[start-1] == ' ':
                new_content = new_content[:start-1] + new_content[end:]
            else:
                new_content = new_content[:start] + new_content[end:]
            changed = True
            replacements.append((tag, None))
        elif new_tag != tag:
            # Remplacer le tag
            new_content = new_content[:start] + f"#{new_tag}" + new_content[end:]
            changed = True
            replacements.append((tag, new_tag))
        else:
            replacements.append((tag, tag))
    
    # Nouveaux tags (après migration)
    new_tags = [new_tag for _, new_tag in replacements if new_tag is not None]
    new_tags = sorted(list(set(new_tags)))
    
    return new_content, changed, old_tags, new_tags


def update_file(filepath: Path, dry_run: bool = True) -> Dict:
    """
    Met à jour un fichier avec les tags migrés (frontmatter + inline)
    Retourne: dict avec stats
    """
    result = {
        'file': str(filepath.relative_to(VAULT_PATH)),
        'frontmatter_changed': False,
        'inline_changed': False,
        'old_frontmatter_tags': [],
        'new_frontmatter_tags': [],
        'old_inline_tags': [],
        'new_inline_tags': [],
        'error': None
    }
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # ====================================================================
        # PARTIE 1: FRONTMATTER TAGS
        # ====================================================================
        
        frontmatter, fm_start, fm_end = extract_frontmatter(content)
        
        if frontmatter and 'tags' in frontmatter:
            old_fm_tags = frontmatter['tags']
            if isinstance(old_fm_tags, str):
                old_fm_tags = [old_fm_tags]
            
            new_fm_tags, fm_changed = migrate_tags_list(old_fm_tags)
            
            if fm_changed:
                result['frontmatter_changed'] = True
                result['old_frontmatter_tags'] = old_fm_tags
                result['new_frontmatter_tags'] = new_fm_tags
                
                # Mettre à jour le frontmatter
                frontmatter['tags'] = new_fm_tags
                frontmatter['updated'] = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
                
                # Reconstruire
                new_frontmatter = yaml.dump(frontmatter, 
                                           default_flow_style=False, 
                                           allow_unicode=True,
                                           sort_keys=False)
                
                content = f"---\n{new_frontmatter}---\n{content[fm_end:]}"
        
        # ====================================================================
        # PARTIE 2: INLINE TAGS
        # ====================================================================
        
        # Migrer les tags inline dans la partie APRÈS le frontmatter
        body_start = fm_end if fm_end > 0 else 0
        body = content[body_start:]
        
        new_body, inline_changed, old_inline, new_inline = migrate_inline_tags(body)
        
        if inline_changed:
            result['inline_changed'] = True
            result['old_inline_tags'] = old_inline
            result['new_inline_tags'] = new_inline
            
            content = content[:body_start] + new_body
        
        # ====================================================================
        # ÉCRITURE
        # ====================================================================
        
        if not result['frontmatter_changed'] and not result['inline_changed']:
            return result
        
        if dry_run:
            return result
        
        # Backup
        backup_path = filepath.with_suffix(filepath.suffix + BACKUP_SUFFIX)
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(original_content)
        
        # Écrire nouveau contenu
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return result
        
    except Exception as e:
        result['error'] = str(e)
        return result


def scan_vault(vault_path: Path, dry_run: bool = True) -> Tuple[List[Dict], int]:
    """
    Scanne tout le vault et migre les tags
    """
    results = []
    total_files = 0
    
    for md_file in vault_path.rglob('*.md'):
        total_files += 1
        result = update_file(md_file, dry_run)
        if result['frontmatter_changed'] or result['inline_changed'] or result['error']:
            results.append(result)
    
    return results, total_files


def print_report(results: List[Dict], total_files: int, dry_run: bool):
    """
    Affiche le rapport de migration
    """
    print("\n" + "="*80)
    if dry_run:
        print("🔍 SIMULATION - Aucun fichier modifié")
    else:
        print("✅ MIGRATION TERMINÉE")
    print("="*80 + "\n")
    
    changed_files = [r for r in results if r['frontmatter_changed'] or r['inline_changed']]
    error_files = [r for r in results if r['error']]
    
    print(f"📊 Statistiques:")
    print(f"   Total fichiers scannés: {total_files}")
    print(f"   Fichiers à modifier: {len(changed_files)}")
    print(f"   Erreurs: {len(error_files)}")
    print()
    
    if changed_files:
        print("📝 Fichiers modifiés:\n")
        for r in changed_files:
            print(f"   📄 {r['file']}")
            
            if r['frontmatter_changed']:
                print(f"      🔹 Frontmatter:")
                print(f"         Old: {r['old_frontmatter_tags']}")
                print(f"         New: {r['new_frontmatter_tags']}")
            
            if r['inline_changed']:
                print(f"      🔹 Inline tags:")
                print(f"         Old: {r['old_inline_tags']}")
                print(f"         New: {r['new_inline_tags']}")
            
            print()
    
    if error_files:
        print("⚠️  Erreurs:\n")
        for r in error_files:
            print(f"   ❌ {r['file']}: {r['error']}")
            print()
    
    # Statistiques tags
    tag_changes = {}
    for r in changed_files:
        all_old_tags = r['old_frontmatter_tags'] + r['old_inline_tags']
        for old_tag in all_old_tags:
            clean = old_tag.lstrip('#')
            if clean in TAG_MIGRATIONS:
                tag_changes[clean] = tag_changes.get(clean, 0) + 1
            elif clean in TAGS_TO_DELETE:
                tag_changes[f"{clean} (DELETED)"] = tag_changes.get(f"{clean} (DELETED)", 0) + 1
    
    if tag_changes:
        print("🏷️  Tags migrés:\n")
        for old_tag, count in sorted(tag_changes.items(), key=lambda x: -x[1]):
            if "(DELETED)" in old_tag:
                print(f"   ❌ {old_tag}: {count} occurrences")
            else:
                new_tag = TAG_MIGRATIONS.get(old_tag, old_tag)
                print(f"   {old_tag} → {new_tag}: {count} occurrences")
        print()


# ============================================================================
# MAIN
# ============================================================================

def main():
    print(f"\n🏷️  MIGRATION TAGS OBSIDIAN - VERSION 2\n")
    print(f"Repo: {REPO_ROOT}")
    print(f"Vault: {VAULT_PATH}")
    print(f"Mode: {'🔍 SIMULATION (DRY RUN)' if DRY_RUN else '⚠️  MIGRATION RÉELLE'}")
    print("\n✨ Gère: Frontmatter YAML + Tags Inline (#Tag)")
    print("\nMapping:")
    for old, new in sorted(TAG_MIGRATIONS.items()):
        print(f"  {old} → {new}")
    
    if TAGS_TO_DELETE:
        print("\nTags à supprimer:")
        for tag in TAGS_TO_DELETE:
            print(f"  ❌ {tag}")
    
    print("\n" + "-"*80)
    input("\nAppuie sur ENTRÉE pour continuer...")
    print()
    
    # Scanner et migrer
    results, total_files = scan_vault(VAULT_PATH, DRY_RUN)
    
    # Rapport
    print_report(results, total_files, DRY_RUN)
    
    if DRY_RUN:
        print("💡 Pour appliquer vraiment les changements:")
        print("   1. Vérifie le rapport ci-dessus")
        print("   2. Change DRY_RUN = False dans le script")
        print("   3. Relance le script")
        print("   4. Commit les changements")
    else:
        print("✅ Migration terminée!")
        print("💾 Backups créés avec extension .backup")
        print("🔍 Vérifie les changements et commit si OK")


if __name__ == "__main__":
    main()
