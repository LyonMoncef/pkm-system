---
type: chat-card
parent_export: '[[Export]]'
order: 438
role: assistant
created: '2025-11-10T03:56:34.311704Z'
tags:
- chat-card
- python
- automation
attachments_count: 0
---

# 🤖 Message 438 - Assistant

**ID:** msg-438

## 💬 Content


**ID:** msg-438

javascript // Ctrl+W - Quick save + hide window (GLOBAL)
 globalShortcut.register('CommandOrControl+W', () => {
 if (mainWindow && mainWindow.isVisible()) {
 // Send signal to save before hiding
 mainWindow.webContents.send('quick-save-and-hide');
 }
 });

 // Ctrl+Shift+I - Show keyboard shortcuts
 globalShortcut.register('CommandOrControl+Shift+I', () => {
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

 // Ctrl+Shift+W - Quit app completely (kill process)
 globalShortcut.register('CommandOrControl+Shift+W', () => {
 console.log('🔴 Force quit requested');
 if (tray) {
 tray.destroy();
 tray = null;
 }
 app.quit();
 process.exit(0); // Force kill
 });

 console.log('✅ Global OS shortcuts registered!');

---


## 🔗 Navigation

- ⬆️ Previous: [[437_assistant_msg-437]]
- ⬇️ Next: [[439_assistant_msg-439]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #automation
