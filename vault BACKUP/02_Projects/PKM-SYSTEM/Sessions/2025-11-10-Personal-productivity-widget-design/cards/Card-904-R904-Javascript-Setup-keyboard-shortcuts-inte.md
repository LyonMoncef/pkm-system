---
type: chat-card
parent_export: '[[Export]]'
order: 904
role: assistant
created: '2025-11-10T22:56:04.718294Z'
tags:
- chat-card
- python
- code
- automation
attachments_count: 0
---

# 🤖 Message 904 - Assistant

**ID:** msg-904

## 💬 Content


**ID:** msg-904

javascript// Setup keyboard shortcuts for internal navigation
function setupInternalShortcuts() {
 const { globalShortcut } = require('electron');

 // Ctrl+1/2/3 for page navigation
 globalShortcut.register('CommandOrControl+1', () => {
 if (mainWindow && !mainWindow.isDestroyed()) {
 mainWindow.webContents.send('navigate-to', 'capture');
 }
 });

 globalShortcut.register('CommandOrControl+2', () => {
 if (mainWindow && !mainWindow.isDestroyed()) {
 mainWindow.webContents.send('navigate-to', 'hub');
 }
 });

 globalShortcut.register('CommandOrControl+3', () => {
 if (mainWindow && !mainWindow.isDestroyed()) {
 mainWindow.webContents.send('navigate-to', 'reference');
 }
 });

 // Ctrl+B for sidebar toggle
 globalShortcut.register('CommandOrControl+B', () => {
 if (mainWindow && !mainWindow.isDestroyed()) {
 mainWindow.webContents.send('toggle-sidebar');
 }
 });

 console.log('✅ Internal navigation shortcuts registered!');
}

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-903-R903-Javascriptconst-contextBridge-ipcRendere]]
- ⬇️ Next: [[Card-905-R905-Javascriptapp-whenReady-then-createMainW]]
- 📊 MOC: [[_MOC_Personal productivity widget design]]

## 🏷️ Topics

- #python
- #code
- #automation
