---
type: chat-card
parent_export: '[[Export]]'
order: 712
role: assistant
created: '2025-11-10T03:56:37.478783Z'
tags:
- chat-card
- python
- automation
attachments_count: 0
---

# 🤖 Message 712 - Assistant

**ID:** msg-712

## 💬 Content


**ID:** msg-712

javascript // Ctrl+Shift+H - Show keyboard shortcuts (Help)
 globalShortcut.register('CommandOrControl+Shift+H', () => {
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

- ⬆️ Previous: [[711_assistant_msg-711]]
- ⬇️ Next: [[713_assistant_msg-713]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #automation
