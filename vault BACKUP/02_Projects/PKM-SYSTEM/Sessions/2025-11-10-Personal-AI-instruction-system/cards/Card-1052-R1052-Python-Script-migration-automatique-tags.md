---
type: chat-card
parent_export: '[[Export]]'
order: 1052
role: assistant
created: '2025-11-10T21:46:20.099492Z'
tags:
- chat-card
- python
- obsidian
- git
- automation
attachments_count: 0
---

# 🤖 Message 1052 - Assistant

**ID:** msg-1052

## 💬 Content


**ID:** msg-1052

python#!/usr/bin/env python3
\"\"\"
Script de migration automatique des tags Obsidian
Applique le mapping défini dans TAG_REGISTRY.md
\"\"\"

import os
import re
import yaml
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Set

# ============================================================================
# CONFIGURATION
# ============================================================================

VAULT_PATH = Path.home() / \"vault\" # Ajuste si nécessaire
BACKUP_SUFFIX = \".backup\"
DRY_RUN = True # True = simulation, False = vraie migration

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

def extract_frontmatter(content: str) -> tuple:
 \"\"\"
 Extrait le frontmatter YAML d'un fichier markdown
 Retourne: (frontmatter_dict, start_pos, end_pos)
 \"\"\"
 match = re.search(r'^---\
(.*?)\
---\
', content, re.DOTALL)
 if not match:
 return None, 0, 0

 try:
 frontmatter = yaml.safe_load(match.group(1))
 return frontmatter, match.start(), match.end()
 except yaml.YAMLError as e:
 print(f\" ⚠️ YAML Error: {e}\")
 return None, 0, 0


def migrate_tags(tags: List[str]) -> tuple:
 \"\"\"
 Migre une liste de tags selon le mapping
 Retourne: (new_tags, changed)
 \"\"\"
 if not tags:
 return [], False

 new_tags = []
 changed = False

 for tag in tags:
 # Nettoyer le tag (enlever # si présent)
 clean_tag = tag.lstrip('#')

 # Supprimer les tags à delete
 if clean_tag in TAGS_TO_DELETE:
 changed = True
 continue

 # Appliquer migration
 if clean_tag in TAG_MIGRATIONS:
 new_tag = TAG_MIGRATIONS[clean_tag]
 new_tags.append(new_tag)
 changed = True
 else:
 new_tags.append(clean_tag)

 # Dédupliquer et trier
 new_tags = sorted(list(set(new_tags)))

 return new_tags, changed


def update_file(filepath: Path, dry_run: bool = True) -> Dict:
 \"\"\"
 Met à jour un fichier avec les tags migrés
 Retourne: dict avec stats
 \"\"\"
 result = {
 'file': str(filepath.relative_to(VAULT_PATH)),
 'changed': False,
 'old_tags': [],
 'new_tags': [],
 'error': None
 }

 try:
 with open(filepath, 'r', encoding='utf-8') as f:
 content = f.read()

 # Extraire frontmatter
 frontmatter, start, end = extract_frontmatter(content)

 if not frontmatter or 'tags' not in frontmatter:
 return result

 # Migrer tags
 old_tags = frontmatter['tags']
 if isinstance(old_tags, str):
 old_tags = [old_tags]

 new_tags, changed = migrate_tags(old_tags)

 if not changed:
 return result

 # Marquer comme changé
 result['changed'] = True
 result['old_tags'] = old_tags
 result['new_tags'] = new_tags

 if dry_run:
 return result

 # Vraie modification
 frontmatter['tags'] = new_tags
 frontmatter['updated'] = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

 # Reconstruire le fichier
 new_frontmatter = yaml.dump(frontmatter,
 default_flow_style=False,
 allow_unicode=True,
 sort_keys=False)

 new_content = f\"---\
{new_frontmatter}---\
{content[end:]}\"

 # Backup
 backup_path = filepath.with_suffix(filepath.suffix + BACKUP_SUFFIX)
 with open(backup_path, 'w', encoding='utf-8') as f:
 f.write(content)

 # Écrire nouveau contenu
 with open(filepath, 'w', encoding='utf-8') as f:
 f.write(new_content)

 return result

 except Exception as e:
 result['error'] = str(e)
 return result


def scan_vault(vault_path: Path, dry_run: bool = True) -> List[Dict]:
 \"\"\"
 Scanne tout le vault et migre les tags
 \"\"\"
 results = []
 total_files = 0

 for md_file in vault_path.rglob('*.md'):
 total_files += 1
 result = update_file(md_file, dry_run)
 if result['changed'] or result['error']:
 results.append(result)

 return results, total_files


def print_report(results: List[Dict], total_files: int, dry_run: bool):
 \"\"\"
 Affiche le rapport de migration
 \"\"\"
 print(\"\
\" + \"=\"*80)
 if dry_run:
 print(\"🔍 SIMULATION - Aucun fichier modifié\")
 else:
 print(\"✅ MIGRATION TERMINÉE\")
 print(\"=\"*80 + \"\
\")

 changed_files = [r for r in results if r['changed']]
 error_files = [r for r in results if r['error']]

 print(f\"📊 Statistiques:\")
 print(f\" Total fichiers scannés: {total_files}\")
 print(f\" Fichiers à modifier: {len(changed_files)}\")
 print(f\" Erreurs: {len(error_files)}\")
 print()

 if changed_files:
 print(\"📝 Fichiers modifiés:\
\")
 for r in changed_files:
 print(f\" 📄 {r['file']}\")
 print(f\" Old: {r['old_tags']}\")
 print(f\" New: {r['new_tags']}\")
 print()

 if error_files:
 print(\"⚠️ Erreurs:\
\")
 for r in error_files:
 print(f\" ❌ {r['file']}: {r['error']}\")
 print()

 # Statistiques tags
 tag_changes = {}
 for r in changed_files:
 for old_tag in r['old_tags']:
 if old_tag in TAG_MIGRATIONS:
 new_tag = TAG_MIGRATIONS[old_tag]
 tag_changes[old_tag] = tag_changes.get(old_tag, 0) + 1
 elif old_tag in TAGS_TO_DELETE:
 tag_changes[f\"{old_tag} (DELETED)\"] = tag_changes.get(f\"{old_tag} (DELETED)\", 0) + 1

 if tag_changes:
 print(\"🏷️ Tags migrés:\
\")
 for old_tag, count in sorted(tag_changes.items()):
 if \"(DELETED)\" in old_tag:
 print(f\" ❌ {old_tag}: {count} occurrences\")
 else:
 new_tag = TAG_MIGRATIONS.get(old_tag.replace(\" (DELETED)\", \"\"), old_tag)
 print(f\" {old_tag} → {new_tag}: {count} occurrences\")
 print()


# ============================================================================
# MAIN
# ============================================================================

def main():
 print(f\"\
🏷️ MIGRATION TAGS OBSIDIAN\
\")
 print(f\"Vault: {VAULT_PATH}\")
 print(f\"Mode: {'🔍 SIMULATION (DRY RUN)' if DRY_RUN else '⚠️ MIGRATION RÉELLE'}\")
 print(\"\
Mapping:\")
 for old, new in sorted(TAG_MIGRATIONS.items()):
 print(f\" {old} → {new}\")

 if TAGS_TO_DELETE:
 print(\"\
Tags à supprimer:\")
 for tag in TAGS_TO_DELETE:
 print(f\" ❌ {tag}\")

 print(\"\
\" + \"-\"*80)
 input(\"\
Appuie sur ENTRÉE pour continuer...\")
 print()

 # Scanner et migrer
 results, total_files = scan_vault(VAULT_PATH, DRY_RUN)

 # Rapport
 print_report(results, total_files, DRY_RUN)

 if DRY_RUN:
 print(\"💡 Pour appliquer vraiment les changements:\")
 print(\" 1. Vérifie le rapport ci-dessus\")
 print(\" 2. Change DRY_RUN = False dans le script\")
 print(\" 3. Relance le script\")
 print(\" 4. Commit les changements\")
 else:
 print(\"✅ Migration terminée!\")
 print(\"💾 Backups créés avec extension .backup\")
 print(\"🔍 Vérifie les changements et commit si OK\")
 print(\"\
📝 Commandes Git:\")
 print(\" git add .\")
 print(' git commit -m \"refactor: migrate all tags to canonical format\"')
 print(\" git push\")


if __name__ == \"__main__\":
 main()

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-1051-R1051-Bashgit-Decisions-commit-feat-finalize]]
- ⬇️ Next: [[Card-1053-R1053-Bashmkdir-vault-scripts-nvim-vault]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #python
- #obsidian
- #git
- #automation
