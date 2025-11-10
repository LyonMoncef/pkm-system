---
type: chat-card
parent_export: '[[Export]]'
order: 880
role: assistant
created: '2025-11-10T22:56:04.503188Z'
tags:
- chat-card
- python
- code
- automation
attachments_count: 0
---

# 🤖 Message 880 - Assistant

**ID:** msg-880

## 💬 Content


**ID:** msg-880

javascript// Global keyboard listener (au niveau Electron)
function setupGlobalKeyboardShortcuts() {
 const { globalShortcut } = require('electron');

 // Ctrl+1/2/3 pour navigation interne
 globalShortcut.register('CommandOrControl+1', () => {
 if (mainWindow) {
 mainWindow.webContents.send('navigate-to', 'capture');
 }
 });

 globalShortcut.register('CommandOrControl+2', () => {
 if (mainWindow) {
 mainWindow.webContents.send('navigate-to', 'hub');
 }
 });

 globalShortcut.register('CommandOrControl+3', () => {
 if (mainWindow) {
 mainWindow.webContents.send('navigate-to', 'reference');
 }
 });

 // Ctrl+B pour toggle sidebar
 globalShortcut.register('CommandOrControl+B', () => {
 if (mainWindow) {
 mainWindow.webContents.send('toggle-sidebar');
 }
 });
}

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-879-R879-Javascript-SUPPRIME-Enter-document-activ]]
- ⬇️ Next: [[Card-881-R881-Javascriptapp-whenReady-then-createMainW]]
- 📊 MOC: [[_MOC_Personal productivity widget design]]

## 🏷️ Topics

- #python
- #code
- #automation
