---
type: chat-card
parent_export: '[[Export]]'
order: 905
role: assistant
created: '2025-11-10T22:56:04.727524Z'
tags:
- chat-card
- python
- automation
attachments_count: 0
---

# 🤖 Message 905 - Assistant

**ID:** msg-905

## 💬 Content


**ID:** msg-905

javascriptapp.whenReady().then(() => {
 createMainWindow();
 createTray();
 registerShortcuts();
 setupInternalShortcuts(); // ← AJOUTE ÇA

 app.on('activate', () => {
 if (BrowserWindow.getAllWindows().length === 0) {
 createMainWindow();
 }
 });
});

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-904-R904-Javascript-Setup-keyboard-shortcuts-inte]]
- ⬇️ Next: [[Card-906-R906-Javascriptapp-will-quit-globalShortcut-u]]
- 📊 MOC: [[_MOC_Personal productivity widget design]]

## 🏷️ Topics

- #python
- #automation
