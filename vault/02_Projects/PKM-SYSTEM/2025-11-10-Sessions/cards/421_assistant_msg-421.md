---
type: chat-card
parent_export: '[[Export]]'
order: 421
role: assistant
created: '2025-11-10T03:56:34.137778Z'
tags:
- chat-card
- python
- code
- automation
attachments_count: 0
---

# 🤖 Message 421 - Assistant

**ID:** msg-421

## 💬 Content


**ID:** msg-421

🎯 PERFECT PLAN !
🔧 CHANGEMENTS À APPLIQUER

1️⃣ GLOBAL Ctrl+Shift+I → Show shortcuts (dans main.js)
2️⃣ GLOBAL Ctrl+Shift+W → Quit app (kill process)
3️⃣ INTERNAL Ctrl+W → Hide window (dans capture.html)
4️⃣ Supprimer le listener Shift+? dans app.html

📝 CODE À APPLIQUER
1. DANS main.js - Ajoute ces 2 nouveaux global shortcuts
Dans la fonction registerGlobalShortcuts(), ajoute AVANT le console.log :
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

2. DANS app.html - Supprime le listener Shift+? et ajoute listener IPC
Supprime cette section :
javascript// === KEYBOARD SHORTCUTS (INTERNAL APP ONLY) ===
document.addEventListener('keydown', (e) => {
 // Shift+? - Show shortcuts hint
 if (e.shiftKey && e.key === '?') {
 e.preventDefault();
 showKeyboardHints();
 }
});
Et ajoute ce listener IPC après les autres IPC listeners (ligne ~15) :
javascript if (window.electronAPI) {
 // Écoute les commandes de navigation depuis main process
 window.electronAPI.onNavigate((page) => {
 navigateToPage(page);
 });

 window.electronAPI.onToggleSidebar(() => {
 toggleSidebar();
 });

 // NEW: Listen for show shortcuts command
 window.electronAPI.onShowShortcuts(() => {
 showKeyboardHints();
 });
 }

3. DANS preload.js - Ajoute le listener show-shortcuts
Ajoute dans exposeInMainWorld :
javascript // Navigation listeners
 onNavigate: (callback) => ipcRenderer.on('navigate-to', (_, page) => callback(page)),
 onToggleSidebar: (callback) => ipcRenderer.on('toggle-sidebar', callback),

 // NEW: Show shortcuts listener
 onShowShortcuts: (callback) => ipcRenderer.on('show-shortcuts', callback),

4. DANS capture.html - Ajoute Ctrl+W pour hide
Dans le listener keyboard de capture.html, ajoute AVANT la section relay :
javascript // === CTRL+W - Quick save + hide window ===
 if (e.ctrlKey && e.key === 'w') {
 e.preventDefault();

 // Force un dernier save en localStorage
 const content = editor.value;
 if (content.trim()) {
 localStorage.setItem('pkm-quick-note', content);
 localStorage.setItem('pkm-quick-note-timestamp', Date.now());
 showNotification('💾 Sauvegardé + caché');
 } else {
 showNotification('📦 Fenêtre cachée');
 }

 // Hide window via IPC
 setTimeout(() => {
 if (window.electronAPI && window.electronAPI.hideWindow) {
 window.electronAPI.hideWindow();
 }
 }, 300); // Délai pour voir la notif
 }

5. MISE À JOUR KEYBOARD HINTS TEXT
Dans app.html, remplace le contenu du #keyboardHint par :
html <!-- Keyboard Shortcuts Hint -->
 <div id=\"keyboardHint\" class=\"keyboard-hint\">
 <div class=\"hint-title\">⌨️ Keyboard Shortcuts</div>
 <div class=\"hint-content\">
 <div class=\"hint-section\">
 <strong>🌍 Global (work when app closed):</strong><br>
 <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>Space</kbd> Toggle Capture<br>
 <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>F</kbd> Toggle Reference<br>
 <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>H</kbd> Toggle Hub<br>
 <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>I</kbd> Show shortcuts (this!)<br>
 <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>W</kbd> Quit app completely
 </div>
 <div class=\"hint-section\">
 <strong>🏠 Internal Navigation:</strong><br>
 <kbd>Ctrl</kbd>+<kbd>1/2/3</kbd> Quick navigate pages<br>
 <kbd>Ctrl</kbd>+<kbd>B</kbd> Toggle sidebar
 </div>
 <div class=\"hint-section\">
 <strong>✍️ Capture Page:</strong><br>
 <kbd>Esc</kbd> Normal mode | <kbd>Ctrl</kbd>+<kbd>I</kbd> Insert mode<br>
 <kbd>Ctrl</kbd>+<kbd>S</kbd> Save to file | <kbd>Ctrl</kbd>+<kbd>K</kbd> Clear<br>
 <kbd>Ctrl</kbd>+<kbd>W</kbd> Quick save + hide window
 </div>
 </div>
 </div>

✅ RÉSUMÉ DES CHANGEMENTS
Nouveaux shortcuts globaux :

✅ Ctrl+Shift+I → Show keyboard shortcuts
✅ Ctrl+Shift+W → Force quit (kill process)

Shortcuts internes :

✅ Ctrl+W dans Capture → Save cache + hide window

Supprimé :

❌ Shortcut Shift+? (ne marchait pas)


🚀 TESTE

Applique les 4 fichiers modifiés
Restart app
Teste :

Ctrl+Shift+I → Shortcuts popup (même app fermée)
Ctrl+Shift+W → Quit complet (process killed)
Ctrl+W dans Capture → Hide window
Sidebar collapse → Contenu centré maintenant


Balance ton feedback ! 💪Réessayer

---


## 🔗 Navigation

- ⬆️ Previous: [[420_user_msg-420]]
- ⬇️ Next: [[422_assistant_msg-422]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #code
- #automation
