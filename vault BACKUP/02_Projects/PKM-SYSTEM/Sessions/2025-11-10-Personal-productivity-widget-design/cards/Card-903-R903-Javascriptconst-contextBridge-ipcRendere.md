---
type: chat-card
parent_export: '[[Export]]'
order: 903
role: assistant
created: '2025-11-10T22:56:04.710055Z'
tags:
- chat-card
- python
- code
- automation
attachments_count: 0
---

# 🤖 Message 903 - Assistant

**ID:** msg-903

## 💬 Content


**ID:** msg-903

javascriptconst { contextBridge, ipcRenderer } = require('electron');

// Expose protected methods to renderer
contextBridge.exposeInMainWorld('electronAPI', {
 // File operations
 saveNote: (filename, content) => ipcRenderer.invoke('save-note', { filename, content }),

 // Platform info
 platform: process.platform,

 // Versions
 versions: {
 node: process.versions.node,
 chrome: process.versions.chrome,
 electron: process.versions.electron
 },

 // Navigation commands (NEW)
 onNavigate: (callback) => {
 ipcRenderer.on('navigate-to', (event, page) => callback(page));
 },

 onToggleSidebar: (callback) => {
 ipcRenderer.on('toggle-sidebar', () => callback());
 }
});

console.log('✅ Preload script loaded');
console.log(` Platform: ${process.platform}`);

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-902-R902-Javascript-Écoute-messages-pour-focus]]
- ⬇️ Next: [[Card-904-R904-Javascript-Setup-keyboard-shortcuts-inte]]
- 📊 MOC: [[_MOC_Personal productivity widget design]]

## 🏷️ Topics

- #python
- #code
- #automation
