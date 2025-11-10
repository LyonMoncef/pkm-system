---
type: chat-card
parent_export: '[[Export]]'
order: 580
role: assistant
created: '2025-11-10T22:56:01.573358Z'
tags:
- chat-card
- code
attachments_count: 0
---

# 🤖 Message 580 - Assistant

**ID:** msg-580

## 💬 Content


**ID:** msg-580

const { contextBridge, ipcRenderer } = require('electron');

// Expose protected methods to renderer
contextBridge.exposeInMainWorld('electronAPI', {
 // File operations
 saveNote: (filename, content) => ipcRenderer.invoke('save-note', { filena

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-579-R579-Const-contextBridge-ipcRenderer-require-]]
- ⬇️ Next: [[Card-581-R581-Copier-fichiers-HTML-bashcd-Projects]]
- 📊 MOC: [[_MOC_Personal productivity widget design]]

## 🏷️ Topics

- #code
