---
type: chat-card
parent_export: '[[Export]]'
order: 712
role: assistant
created: '2025-11-10T21:12:15.032481Z'
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

- ⬆️ Previous: [[Card-711-R711-DEBUG-CTRL-SHIFT-research-nécessaire]]
- ⬇️ Next: [[Card-713-R713-Javascript-Show-keyboard-shortcuts-Help]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #automation
