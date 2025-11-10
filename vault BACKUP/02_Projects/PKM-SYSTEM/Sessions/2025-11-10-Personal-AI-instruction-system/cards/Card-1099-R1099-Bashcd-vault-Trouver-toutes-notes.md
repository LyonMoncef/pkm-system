---
type: chat-card
parent_export: '[[Export]]'
order: 1099
role: assistant
created: '2025-11-10T21:46:20.666653Z'
tags:
- chat-card
- obsidian
attachments_count: 0
---

# 🤖 Message 1099 - Assistant

**ID:** msg-1099

## 💬 Content


**ID:** msg-1099

bashcd ~/vault

# Trouver toutes les notes avec \"**Tags:**\" ou \"Tags:\" en markdown
grep -r \"\\*\\*Tags:\\*\\*\" --include=\"*.md\" .

# Extraire les tags inline
grep -r \"#[A-Z][a-zA-Z-]*\" --include=\"*.md\" . | \\
 grep -v \"^tags:\" | \\
 head -20

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-1098-R1098-Markdown-Tags-Electron-BuildInPublic-Mil]]
- ⬇️ Next: [[Card-1100-R1100-Python-Script-migration-automatique-tags]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #obsidian
