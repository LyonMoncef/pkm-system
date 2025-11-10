---
type: chat-card
parent_export: '[[Export]]'
order: 170
role: assistant
created: '2025-11-10T21:12:05.278730Z'
tags:
- chat-card
- python
- code
- automation
attachments_count: 0
---

# 🤖 Message 170 - Assistant

**ID:** msg-170

## 💬 Content


**ID:** msg-170

javascriptconst contextMenu = Menu.buildFromTemplate([
 { label: '🧠 PKM System', enabled: false },
 { type: 'separator' },
 {
 label: '🏠 Hub',
 click: () => {
 if (mainWindow) {
 mainWindow.show();
 mainWindow.webContents.send('navigate-to', 'hub');
 } else {
 createMainWindow();
 }
 }
 },
 {
 label: '✍️ Quick Capture',
 click: () => {
 if (mainWindow) {
 mainWindow.show();
 mainWindow.webContents.send('navigate-to', 'capture');
 } else {
 createMainWindow();
 }
 }
 },
 {
 label: '⚡ Quick Reference',
 click: () => {
 if (mainWindow) {
 mainWindow.show();
 mainWindow.webContents.send('navigate-to', 'reference');
 } else {
 createMainWindow();
 }
 }
 },
 { type: 'separator' },
 {
 label: 'Quit',
 click: () => {
 if (tray) {
 tray.destroy();
 tray = null;
 }
 app.quit();
 }
 }
]);

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-169-R169-Javascript-label-Quick-Reference-click]]
- ⬇️ Next: [[Card-171-R171-Javascript-SUPPRIME-LIGNES-obsolètes-ave]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #code
- #automation
