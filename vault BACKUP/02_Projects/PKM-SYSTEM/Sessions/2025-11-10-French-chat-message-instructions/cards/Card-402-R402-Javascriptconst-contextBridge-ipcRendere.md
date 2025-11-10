---
type: chat-card
parent_export: '[[Export]]'
order: 402
role: assistant
created: '2025-11-10T21:12:07.883773Z'
tags:
- chat-card
- python
- code
- automation
attachments_count: 0
---

# 🤖 Message 402 - Assistant

**ID:** msg-402

## 💬 Content


**ID:** msg-402

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

 // Navigation listeners
 onNavigate: (callback) => ipcRenderer.on('navigate-to', (_, page) => callback(page)),
 onToggleSidebar: (callback) => ipcRenderer.on('toggle-sidebar', callback),

 // NEW: Notify main process of page changes
 notifyPageChange: (page) => ipcRenderer.send('current-page-changed', page),

 // NEW: Hide window
 hideWindow: () => ipcRenderer.send('hide-window')
});

console.log('✅ Preload script loaded');
console.log(` Platform: ${process.platform}`);

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-401-R401-Javascript-script-LISTENERS-window-elect]]
- ⬇️ Next: [[Card-403-R403-Html-Keyboard-Shortcuts-Hint-keyboardHin]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #code
- #automation
