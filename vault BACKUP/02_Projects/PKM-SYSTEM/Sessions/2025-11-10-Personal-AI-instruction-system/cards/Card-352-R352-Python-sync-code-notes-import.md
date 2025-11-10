---
type: chat-card
parent_export: '[[Export]]'
order: 352
role: assistant
created: '2025-11-10T21:46:10.685188Z'
tags:
- chat-card
- python
- obsidian
- code
attachments_count: 0
---

# 🤖 Message 352 - Assistant

**ID:** msg-352

## 💬 Content


**ID:** msg-352

python# sync-code-notes.py

import os
import re
from datetime import datetime

def extract_functions(file_path):
 \"\"\"Extrait les fonctions d'un fichier JS\"\"\"
 with open(file_path, 'r') as f:
 content = f.read()

 # Regex pour fonctions
 functions = re.findall(r'function (\\w+)\\(', content)
 # + arrow functions
 functions += re.findall(r'const (\\w+) = \\(.*\\) =>', content)

 return functions

def update_code_note(js_file, note_file):
 \"\"\"Met à jour la note avec les nouvelles fonctions\"\"\"
 functions = extract_functions(js_file)

 # Lit la note existante
 with open(note_file, 'r') as f:
 note = f.read()

 # Update section \"Fonctions Principales\"
 # (logique de remplacement...)

 # Update \"updated\" timestamp
 # (logique de remplacement...)

# Lance pour tous les fichiers
for js_file in glob('src/**/*.js'):
 note_file = f'vault/04_Resources/Code/{js_file}.md'
 update_code_note(js_file, note_file)

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-351-R351-Markdown-created-updated-type-code]]
- ⬇️ Next: [[Card-353-R353-Markdown-Implémentation-Fichier-main-fon]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #python
- #obsidian
- #code
