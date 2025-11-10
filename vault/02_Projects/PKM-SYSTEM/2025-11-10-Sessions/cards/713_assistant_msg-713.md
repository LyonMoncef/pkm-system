---
type: chat-card
parent_export: '[[Export]]'
order: 713
role: assistant
created: '2025-11-10T03:56:37.489714Z'
tags:
- chat-card
- python
- automation
attachments_count: 0
---

# 🤖 Message 713 - Assistant

**ID:** msg-713

## 💬 Content


**ID:** msg-713

javascript // F1 - Show keyboard shortcuts (Help)
 globalShortcut.register('F1', () => {
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

- ⬆️ Previous: [[712_assistant_msg-712]]
- ⬇️ Next: [[714_assistant_msg-714]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #automation
