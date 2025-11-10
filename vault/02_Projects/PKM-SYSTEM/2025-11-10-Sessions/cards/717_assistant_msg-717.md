---
type: chat-card
parent_export: '[[Export]]'
order: 717
role: assistant
created: '2025-11-10T03:56:37.527796Z'
tags:
- chat-card
- python
- automation
attachments_count: 0
---

# 🤖 Message 717 - Assistant

**ID:** msg-717

## 💬 Content


**ID:** msg-717

javascript // Ctrl+/ - Show keyboard shortcuts
 globalShortcut.register('CommandOrControl+/', () => {
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

- ⬆️ Previous: [[716_assistant_msg-716]]
- ⬇️ Next: [[718_assistant_msg-718]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #automation
