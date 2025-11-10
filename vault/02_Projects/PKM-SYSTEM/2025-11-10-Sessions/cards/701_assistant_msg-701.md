---
type: chat-card
parent_export: '[[Export]]'
order: 701
role: assistant
created: '2025-11-10T03:56:37.356669Z'
tags:
- chat-card
- python
- automation
attachments_count: 0
---

# 🤖 Message 701 - Assistant

**ID:** msg-701

## 💬 Content


**ID:** msg-701

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

---


## 🔗 Navigation

- ⬆️ Previous: [[700_assistant_msg-700]]
- ⬇️ Next: [[702_assistant_msg-702]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #automation
