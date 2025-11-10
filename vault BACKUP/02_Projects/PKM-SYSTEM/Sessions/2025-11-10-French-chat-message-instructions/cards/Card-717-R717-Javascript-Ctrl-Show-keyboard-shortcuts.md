---
type: chat-card
parent_export: '[[Export]]'
order: 717
role: assistant
created: '2025-11-10T21:12:15.095301Z'
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

- ⬆️ Previous: [[Card-716-R716-CTRL-POUR-SHORTCUTS-RAPIDE-besoin]]
- ⬇️ Next: [[Card-718-R718-Html-class-status-right-Press]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #automation
