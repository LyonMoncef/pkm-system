---
type: chat-card
parent_export: '[[Export]]'
order: 1075
role: assistant
created: '2025-11-10T21:46:20.377443Z'
tags:
- chat-card
- obsidian
- code
attachments_count: 0
---

# 🤖 Message 1075 - Assistant

**ID:** msg-1075

## 💬 Content


**ID:** msg-1075

bashcd ~/vault

# Extraire tous les tags du vault
grep -r \"^tags:\" --include=\"*.md\" | \\
 sed 's/.*tags: \\[\\(.*\\)\\]/\\1/' | \\
 tr ',' '\
' | \\
 sed 's/^ *//;s/ *$//' | \\
 sort | uniq -c | sort -rn
```

**Ça va me donner:**
```
 12 electron
 8 Electron
 6 build-in-public
 6 BuildInPublic
 [...]

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-1074-R1074-LANCEMENT-SIMULATION-DIAGNOSTIC-TAGS-ÉTA]]
- ⬇️ Next: [[Card-1076-R1076-Bashcd-vault-scripts-Vérifier-True]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #obsidian
- #code
