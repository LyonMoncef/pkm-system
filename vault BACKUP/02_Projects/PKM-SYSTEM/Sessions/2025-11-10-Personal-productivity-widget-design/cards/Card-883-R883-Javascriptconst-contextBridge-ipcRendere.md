---
type: chat-card
parent_export: '[[Export]]'
order: 883
role: assistant
created: '2025-11-10T22:56:04.530996Z'
tags:
- chat-card
- python
- code
- automation
attachments_count: 0
---

# 🤖 Message 883 - Assistant

**ID:** msg-883

## 💬 Content


**ID:** msg-883

javascriptconst { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electronAPI', {
 // Existing
 saveNote: (filename, content) => ipcRenderer.invoke('save-note', { filename, content }),
 platform: process.platform,
 versions: { /* ... */ },

 // NEW
 onNavigate: (callback) => ipcRenderer.on('navigate-to', (_, page) => callback(page)),
 onToggleSidebar: (callback) => ipcRenderer.on('toggle-sidebar', callback)
});

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-882-R882-Javascript-Juste-après-script-commence]]
- ⬇️ Next: [[Card-884-R884-Javascript-Setup-listeners-window-electr]]
- 📊 MOC: [[_MOC_Personal productivity widget design]]

## 🏷️ Topics

- #python
- #code
- #automation
