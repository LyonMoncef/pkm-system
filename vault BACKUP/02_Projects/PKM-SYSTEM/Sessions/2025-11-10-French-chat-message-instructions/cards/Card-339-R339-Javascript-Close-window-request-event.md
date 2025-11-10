---
type: chat-card
parent_export: '[[Export]]'
order: 339
role: assistant
created: '2025-11-10T21:12:07.181217Z'
tags:
- chat-card
- python
- code
- automation
attachments_count: 0
---

# 🤖 Message 339 - Assistant

**ID:** msg-339

## 💬 Content


**ID:** msg-339

javascript // Close window request
 if (event.data.type === 'close-window') {
 if (window.electronAPI) {
 // Cache la fenêtre au lieu de la fermer
 const { ipcRenderer } = require('electron');
 require('electron').remote.getCurrentWindow().hide();
 }
 }

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-338-R338-Javascript-CTRL-Save-Close-ctrlKey]]
- ⬇️ Next: [[Card-340-R340-Javascript-Window-controls-hideWindow-ip]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #code
- #automation
