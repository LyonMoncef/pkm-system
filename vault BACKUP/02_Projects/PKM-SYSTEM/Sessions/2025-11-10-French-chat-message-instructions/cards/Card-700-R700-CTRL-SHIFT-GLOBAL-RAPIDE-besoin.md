---
type: chat-card
parent_export: '[[Export]]'
order: 700
role: assistant
created: '2025-11-10T21:12:14.874304Z'
tags:
- chat-card
- python
- code
- automation
attachments_count: 0
---

# 🤖 Message 700 - Assistant

**ID:** msg-700

## 💬 Content


**ID:** msg-700

🔧 CTRL+SHIFT+I GLOBAL - FIX RAPIDE
Pas besoin de research ici, c'est juste ajouter le shortcut dans main.js !

📝 FIX - Dans main.js
Dans la fonction registerGlobalShortcuts(), vérifie que tu as bien :
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
Si ça existe déjà, vérifie que le listener IPC existe dans app.html :
javascript if (window.electronAPI) {
 // ... autres listeners ...

 // Listen for show shortcuts command
 window.electronAPI.onShowShortcuts(() => {
 showKeyboardHints();
 });
 }
Et dans preload.js :
javascript // Show shortcuts listener
 onShowShortcuts: (callback) => ipcRenderer.on('show-shortcuts', callback),

🚀 SI MANQUANT
Dis-moi quelle partie manque et je te donne le code complet !
Ou balance-moi ton main.js actuel et je check ! 💪

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-699-R699-CTRL-SHIFT-GLOBAL-RAPIDE-besoin]]
- ⬇️ Next: [[Card-701-R701-Javascript-Ctrl-Shift-Show-keyboard]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #code
- #automation
