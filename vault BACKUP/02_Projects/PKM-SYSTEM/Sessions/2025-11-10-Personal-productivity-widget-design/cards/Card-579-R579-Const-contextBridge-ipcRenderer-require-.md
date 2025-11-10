---
type: chat-card
parent_export: '[[Export]]'
order: 579
role: assistant
created: '2025-11-10T22:56:01.565187Z'
tags:
- chat-card
- code
attachments_count: 0
---

# 🤖 Message 579 - Assistant

**ID:** msg-579

## 💬 Content


**ID:** msg-579

const { contextBridge, ipcRenderer } = require('electron');

// Expose protected methods to renderer
contextBridge.exposeInMainWorld('electronAPI', {
 // File operations
 saveNote: (filename, content) => ipcRenderer.invoke('save-note', { filena

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-578-R578-Electron-Preload-Script]]
- ⬇️ Next: [[Card-580-R580-Const-contextBridge-ipcRenderer-require-]]
- 📊 MOC: [[_MOC_Personal productivity widget design]]

## 🏷️ Topics

- #code
