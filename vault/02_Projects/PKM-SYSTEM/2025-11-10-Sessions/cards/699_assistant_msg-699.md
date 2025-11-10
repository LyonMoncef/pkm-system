---
type: chat-card
parent_export: '[[Export]]'
order: 699
role: assistant
created: '2025-11-10T03:56:37.319591Z'
tags:
- chat-card
- python
- code
- automation
attachments_count: 0
---

# 🤖 Message 699 - Assistant

**ID:** msg-699

## 💬 Content


**ID:** msg-699

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

- ⬆️ Previous: [[698_assistant_msg-698]]
- ⬇️ Next: [[700_assistant_msg-700]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #code
- #automation
