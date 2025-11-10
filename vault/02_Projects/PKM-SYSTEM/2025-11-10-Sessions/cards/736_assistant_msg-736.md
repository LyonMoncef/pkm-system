---
type: chat-card
parent_export: '[[Export]]'
order: 736
role: assistant
created: '2025-11-10T03:56:37.734263Z'
tags:
- chat-card
- python
- automation
attachments_count: 0
---

# 🤖 Message 736 - Assistant

**ID:** msg-736

## 💬 Content


**ID:** msg-736

javascript // === TEST SHORTCUTS HELP (3 raccourcis pour debug) ===

 // F1 - Show keyboard shortcuts
 globalShortcut.register('F1', () => {
 console.log('🔑 F1 pressed!');
 if (mainWindow && mainWindow.isVisible()) {
 mainWindow.webContents.send('show-shortcuts');
 } else if (mainWindow) {
 mainWindow.show();
 setTimeout(() => {
 mainWindow.webContents.send('show-shortcuts');
 }, 300);
 } else {
 createMainWindow();
 setTimeout(() => {
 mainWindow.webContents.send('show-shortcuts');
 }, 800);
 }
 });

 // Ctrl+/ - Show keyboard shortcuts
 globalShortcut.register('CommandOrControl+/', () => {
 console.log('🔑 Ctrl+/ pressed!');
 if (mainWindow && mainWindow.isVisible()) {
 mainWindow.webContents.send('show-shortcuts');
 } else if (mainWindow) {
 mainWindow.show();
 setTimeout(() => {
 mainWindow.webContents.send('show-shortcuts');
 }, 300);
 } else {
 createMainWindow();
 setTimeout(() => {
 mainWindow.webContents.send('show-shortcuts');
 }, 800);
 }
 });

 // Ctrl+Shift+L - Show keyboard shortcuts (test)
 globalShortcut.register('CommandOrControl+Shift+L', () => {
 console.log('🔑 Ctrl+Shift+L pressed!');
 if (mainWindow && mainWindow.isVisible()) {
 mainWindow.webContents.send('show-shortcuts');
 } else if (mainWindow) {
 mainWindow.show();
 setTimeout(() => {
 mainWindow.webContents.send('show-shortcuts');
 }, 300);
 } else {
 createMainWindow();
 setTimeout(() => {
 mainWindow.webContents.send('show-shortcuts');
 }, 800);
 }
 });

---


## 🔗 Navigation

- ⬆️ Previous: [[735_assistant_msg-735]]
- ⬇️ Next: [[737_assistant_msg-737]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #automation
