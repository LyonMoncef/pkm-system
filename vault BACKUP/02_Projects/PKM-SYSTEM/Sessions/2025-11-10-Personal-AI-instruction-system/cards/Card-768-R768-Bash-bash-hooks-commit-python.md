---
type: chat-card
parent_export: '[[Export]]'
order: 768
role: assistant
created: '2025-11-10T21:46:16.372817Z'
tags:
- chat-card
- python
- git
- automation
attachments_count: 0
---

# 🤖 Message 768 - Assistant

**ID:** msg-768

## 💬 Content


**ID:** msg-768

bash#!/bin/bash
# .git/hooks/pre-commit

python scripts/validate-tags.py
if [ $? -ne 0 ]; then
 echo \"❌ Invalid tags detected. Check TAG_REGISTRY.md\"
 exit 1
fi

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-767-R767-Pythonimport-import-import-yaml-Load]]
- ⬇️ Next: [[Card-769-R769-Markdown-MANAGEMENT-RÈGLE-CRITIQUE-TOUJO]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #python
- #git
- #automation
