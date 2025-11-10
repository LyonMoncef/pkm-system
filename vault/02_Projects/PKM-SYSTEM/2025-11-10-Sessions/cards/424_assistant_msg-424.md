---
type: chat-card
parent_export: '[[Export]]'
order: 424
role: assistant
created: '2025-11-10T03:56:34.171910Z'
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

- ⬆️ Previous: [[423_assistant_msg-423]]
- ⬇️ Next: [[425_assistant_msg-425]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #automation
