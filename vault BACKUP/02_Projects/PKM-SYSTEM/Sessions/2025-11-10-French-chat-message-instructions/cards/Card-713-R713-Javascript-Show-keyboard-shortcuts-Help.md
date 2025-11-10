---
type: chat-card
parent_export: '[[Export]]'
order: 713
role: assistant
created: '2025-11-10T21:12:15.046900Z'
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

- ⬆️ Previous: [[Card-712-R712-Javascript-Ctrl-Shift-Show-keyboard]]
- ⬇️ Next: [[Card-714-R714-CTRL-POUR-SHORTCUTS-RAPIDE-besoin]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #automation
