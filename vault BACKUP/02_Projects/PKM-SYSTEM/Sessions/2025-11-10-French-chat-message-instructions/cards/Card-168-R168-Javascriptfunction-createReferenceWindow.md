---
type: chat-card
parent_export: '[[Export]]'
order: 168
role: assistant
created: '2025-11-10T21:12:05.251830Z'
tags:
- chat-card
- python
- code
- automation
attachments_count: 0
---

# 🤖 Message 168 - Assistant

**ID:** msg-168

## 💬 Content


**ID:** msg-168

javascriptfunction createReferenceWindow() {
 if (referenceWindow) {
 referenceWindow.focus();
 return;
 }

 referenceWindow = new BrowserWindow({
 width: 700,
 height: 800,
 webPreferences: {
 nodeIntegration: false,
 contextIsolation: true,
 preload: path.join(__dirname, '../preload/preload.js')
 },
 frame: true
 });

 referenceWindow.loadFile(path.join(__dirname, '../renderer/reference.html')); // ← LIGNE 98

 referenceWindow.on('closed', () => {
 referenceWindow = null;
 });
}

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-167-R167-TROUVÉ-COUPABLE-erreur-vient-main]]
- ⬇️ Next: [[Card-169-R169-Javascript-label-Quick-Reference-click]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #code
- #automation
