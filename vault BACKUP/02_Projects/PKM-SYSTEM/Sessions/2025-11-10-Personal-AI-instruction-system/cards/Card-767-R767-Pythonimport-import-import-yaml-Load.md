---
type: chat-card
parent_export: '[[Export]]'
order: 767
role: assistant
created: '2025-11-10T21:46:16.360331Z'
tags:
- chat-card
- python
- obsidian
- automation
attachments_count: 0
---

# 🤖 Message 767 - Assistant

**ID:** msg-767

## 💬 Content


**ID:** msg-767

pythonimport os
import re
import yaml

# Load registry
ALLOWED_TAGS = [
 'moc', 'concept', 'feature', 'shortcut',
 'electron', 'javascript', 'ipc',
 # ... (load from TAG_REGISTRY.md)
]

def validate_note(filepath):
 with open(filepath, 'r') as f:
 content = f.read()

 # Extract frontmatter
 match = re.search(r'^---\
(.*?)\
---', content, re.DOTALL)
 if not match:
 return []

 frontmatter = yaml.safe_load(match.group(1))
 tags = frontmatter.get('tags', [])

 # Check tags
 invalid = [tag for tag in tags if tag not in ALLOWED_TAGS]

 return invalid

# Usage
for root, dirs, files in os.walk('vault'):
 for file in files:
 if file.endswith('.md'):
 invalid = validate_note(os.path.join(root, file))
 if invalid:
 print(f\"❌ {file}: Invalid tags {invalid}\")

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-766-R766-MarkdownUser-Crée-note-système-Electron]]
- ⬇️ Next: [[Card-768-R768-Bash-bash-hooks-commit-python]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #python
- #obsidian
- #automation
