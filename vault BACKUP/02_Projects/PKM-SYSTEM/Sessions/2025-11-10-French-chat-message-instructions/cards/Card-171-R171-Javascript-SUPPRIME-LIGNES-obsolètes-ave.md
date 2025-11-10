---
type: chat-card
parent_export: '[[Export]]'
order: 171
role: assistant
created: '2025-11-10T21:12:05.290477Z'
tags:
- chat-card
- python
- code
- automation
attachments_count: 0
---

# 🤖 Message 171 - Assistant

**ID:** msg-171

## 💬 Content


**ID:** msg-171

javascript// SUPPRIME CES LIGNES (obsolètes avec single window)
function registerShortcuts() {
 globalShortcut.register('CommandOrControl+Shift+Space', () => {
 if (captureWindow) {
 captureWindow.isVisible() ? captureWindow.hide() : captureWindow.show();
 } else {
 createCaptureWindow();
 }
 });

 globalShortcut.register('CommandOrControl+Shift+F', () => {
 if (referenceWindow) {
 referenceWindow.isVisible() ? referenceWindow.hide() : referenceWindow.show();
 } else {
 createReferenceWindow();
 }
 });

 console.log('✅ Global shortcuts registered!');
}

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-170-R170-Javascriptconst-contextMenu-Menu-buildFr]]
- ⬇️ Next: [[Card-172-R172-Javascriptfunction-registerShortcuts-Ctr]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #code
- #automation
