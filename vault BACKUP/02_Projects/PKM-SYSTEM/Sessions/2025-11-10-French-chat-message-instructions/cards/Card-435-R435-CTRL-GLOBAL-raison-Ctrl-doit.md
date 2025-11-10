---
type: chat-card
parent_export: '[[Export]]'
order: 435
role: assistant
created: '2025-11-10T21:12:08.359768Z'
tags:
- chat-card
- python
- code
- automation
attachments_count: 0
---

# 🤖 Message 435 - Assistant

**ID:** msg-435

## 💬 Content


**ID:** msg-435

🎯 CTRL+W GLOBAL - FIX
T'as raison, Ctrl+W doit être global comme les autres !

🔧 CHANGEMENTS
1. SUPPRIMER Ctrl+W de capture.html
Supprime la section Ctrl+W qu'on vient d'ajouter dans capture.html.

2. AJOUTER Ctrl+W GLOBAL dans main.js
Dans registerGlobalShortcuts(), ajoute APRÈS les autres shortcuts :
javascript // Ctrl+W - Quick save + hide window (GLOBAL)
 globalShortcut.register('CommandOrControl+W', () => {
 if (mainWindow && mainWindow.isVisible()) {
 // Send signal to save before hiding
 mainWindow.webContents.send('quick-save-and-hide');
 }
 });

 // Ctrl+Shift+I - Show keyboard shortcuts
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

 // Ctrl+Shift+W - Quit app completely (kill process)
 globalShortcut.register('CommandOrControl+Shift+W', () => {
 console.log('🔴 Force quit requested');
 if (tray) {
 tray.destroy();
 tray = null;
 }
 app.quit();
 process.exit(0); // Force kill
 });

 console.log('✅ Global OS shortcuts registered!');

3. AJOUTER listener IPC dans app.html
Ajoute après les autres IPC listeners :
javascript if (window.electronAPI) {
 // Écoute les commandes de navigation depuis main process
 window.electronAPI.onNavigate((page) => {
 navigateToPage(page);
 });

 window.electronAPI.onToggleSidebar(() => {
 toggleSidebar();
 });

 // Listen for show shortcuts command
 window.electronAPI.onShowShortcuts(() => {
 showKeyboardHints();
 });

 // NEW: Listen for quick save and hide
 window.electronAPI.onQuickSaveAndHide(() => {
 // Forward to active iframe (capture page)
 const activeIframe = document.querySelector('.view-page.active iframe');
 if (activeIframe && activeIframe.contentWindow) {
 activeIframe.contentWindow.postMessage({ type: 'quick-save-and-hide' }, '*');
 }

 // Hide window after short delay
 setTimeout(() => {
 if (window.electronAPI && window.electronAPI.hideWindow) {
 window.electronAPI.hideWindow();
 }
 }, 300);
 });
 }

4. AJOUTER dans preload.js
javascript // Quick save and hide listener
 onQuickSaveAndHide: (callback) => ipcRenderer.on('quick-save-and-hide', callback),

5. AJOUTER dans capture.html - Listener postMessage
Ajoute APRÈS le listener keyboard relay, AVANT console.log('✅ Keyboard relay active') :
javascript // Listen for quick save command from parent
 window.addEventListener('message', (event) => {
 if (event.data.type === 'quick-save-and-hide') {
 // Force save to localStorage
 const content = editor.value;
 if (content.trim()) {
 localStorage.setItem('pkm-quick-note', content);
 localStorage.setItem('pkm-quick-note-timestamp', Date.now());
 showNotification('💾 Sauvegardé + caché');
 } else {
 showNotification('📦 Fenêtre cachée');
 }
 }
 });

 console.log('✅ Keyboard relay active');

🎯 FLOW COMPLET

User fait Ctrl+W (n'importe où, même app fermée si visible)
→ main.js détecte le shortcut global
→ Envoie IPC quick-save-and-hide à app.html
→ app.html forward postMessage à l'iframe active
→ capture.html reçoit, save en localStorage, montre notif
→ app.html hide la fenêtre après 300ms


✅ RÉSUMÉ
Shortcuts globaux finaux :

Ctrl+Shift+Space → Toggle Capture
Ctrl+Shift+F → Toggle Reference
Ctrl+Shift+H → Toggle Hub
Ctrl+Shift+I → Show shortcuts
Ctrl+W → Quick save + hide
Ctrl+Shift+W → Force quit


🚀 TESTE
Applique les 4 fichiers et teste Ctrl+W depuis n'importe où !
Balance ton retour ! 💪Réessayer

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-434-S434-ID-msg-434]]
- ⬇️ Next: [[Card-436-R436-CTRL-GLOBAL-raison-Ctrl-doit]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #code
- #automation
