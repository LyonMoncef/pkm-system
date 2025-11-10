---
type: chat-card
parent_export: '[[Export]]'
order: 172
role: assistant
created: '2025-11-10T21:12:05.303225Z'
tags:
- chat-card
- python
- code
- automation
attachments_count: 0
---

# 🤖 Message 172 - Assistant

**ID:** msg-172

## 💬 Content


**ID:** msg-172

javascriptfunction registerShortcuts() {
 // Ctrl+Shift+Space - Toggle main window + go to capture
 globalShortcut.register('CommandOrControl+Shift+Space', () => {
 if (mainWindow) {
 if (mainWindow.isVisible()) {
 mainWindow.hide();
 } else {
 mainWindow.show();
 mainWindow.webContents.send('navigate-to', 'capture');
 }
 } else {
 createMainWindow();
 }
 });

 // Ctrl+Shift+F - Toggle main window + go to reference
 globalShortcut.register('CommandOrControl+Shift+F', () => {
 if (mainWindow) {
 if (mainWindow.isVisible()) {
 mainWindow.hide();
 } else {
 mainWindow.show();
 mainWindow.webContents.send('navigate-to', 'reference');
 }
 } else {
 createMainWindow();
 }
 });

 console.log('✅ Global shortcuts registered!');
}

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-171-R171-Javascript-SUPPRIME-LIGNES-obsolètes-ave]]
- ⬇️ Next: [[Card-173-R173-Javascriptapp-whenReady-then-createMainW]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #code
- #automation
