---
type: chat-card
parent_export: '[[Export]]'
order: 871
role: assistant
created: '2025-11-10T21:12:17.204774Z'
tags:
- chat-card
- python
- automation
attachments_count: 0
---

# 🤖 Message 871 - Assistant

**ID:** msg-871

## 💬 Content


**ID:** msg-871

javascript // === RELAY TO PARENT - Ctrl+1/2/3, Ctrl+B ===
 if (e.ctrlKey && ['1', '2', '3', 'b', 'B'].includes(e.key)) {
 e.preventDefault();

 window.parent.postMessage({
 type: 'keyboard-event',
 event: {
 key: e.key.toLowerCase(),
 code: e.code,
 ctrlKey: e.ctrlKey,
 shiftKey: e.shiftKey,
 altKey: e.altKey,
 metaKey: e.metaKey
 }
 }, '*');
 }

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-870-R870-Javascriptdocument-addEventListener-keyd]]
- ⬇️ Next: [[Card-872-R872-MFça-marche-pasViens-commit-dans]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #automation
