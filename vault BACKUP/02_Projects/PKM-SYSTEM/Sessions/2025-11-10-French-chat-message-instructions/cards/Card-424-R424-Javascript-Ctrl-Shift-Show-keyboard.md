---
type: chat-card
parent_export: '[[Export]]'
order: 424
role: assistant
created: '2025-11-10T21:12:08.169435Z'
tags:
- chat-card
- python
- automation
attachments_count: 0
---

# 🤖 Message 424 - Assistant

**ID:** msg-424

## 💬 Content


**ID:** msg-424

javascript // Ctrl+Shift+I - Show keyboard shortcuts
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

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-423-R423-PERFECT-PLAN-CHANGEMENTS-APPLIQUER-GLOBA]]
- ⬇️ Next: [[Card-425-R425-Javascript-KEYBOARD-SHORTCUTS-INTERNAL-O]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #automation
