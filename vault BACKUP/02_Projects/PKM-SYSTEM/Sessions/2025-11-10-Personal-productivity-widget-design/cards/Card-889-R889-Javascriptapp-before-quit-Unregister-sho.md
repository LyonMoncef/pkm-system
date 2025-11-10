---
type: chat-card
parent_export: '[[Export]]'
order: 889
role: assistant
created: '2025-11-10T22:56:04.582720Z'
tags:
- chat-card
- python
- automation
attachments_count: 0
---

# 🤖 Message 889 - Assistant

**ID:** msg-889

## 💬 Content


**ID:** msg-889

javascriptapp.on('before-quit', () => {
 // Unregister shortcuts
 globalShortcut.unregisterAll();

 // Destroy tray AVANT quit
 if (tray) {
 tray.destroy();
 tray = null;
 }
});

app.on('will-quit', () => {
 // Double cleanup au cas où
 if (tray) {
 tray.destroy();
 tray = null;
 }
});

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-888-R888-Html-button-class-toggle-sidebar]]
- ⬇️ Next: [[Card-890-R890-Javascript-Dans-menu-tray-label]]
- 📊 MOC: [[_MOC_Personal productivity widget design]]

## 🏷️ Topics

- #python
- #automation
