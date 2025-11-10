---
type: chat-card
parent_export: '[[Export]]'
order: 398
role: assistant
created: '2025-11-10T03:56:33.798947Z'
tags:
- chat-card
- python
- receipts
- code
- automation
attachments_count: 0
---

# 🤖 Message 398 - Assistant

**ID:** msg-398

## 💬 Content


**ID:** msg-398

🚀 STEP 2: Refactor app.html
🔧 CODE REFACTORÉ - Section JavaScript
Dans app.html, remplace toute la section <script> par :
javascript <script>
 // === IPC LISTENERS ===
 if (window.electronAPI) {
 // Écoute les commandes de navigation depuis main process
 window.electronAPI.onNavigate((page) => {
 navigateToPage(page);
 });

 window.electronAPI.onToggleSidebar(() => {
 toggleSidebar();
 });
 }

 // === FOCUS MANAGEMENT SYSTEM ===
 // Écoute les events clavier des iframes
 window.addEventListener('message', (event) => {
 if (event.data.type === 'keyboard-event') {
 const keyEvent = event.data.event;

 // Ctrl+1/2/3 - Navigate pages (INTERNAL ONLY)
 if (keyEvent.ctrlKey && ['1', '2', '3'].includes(keyEvent.key)) {
 const pages = ['capture', 'hub', 'reference'];
 const pageIndex = parseInt(keyEvent.key) - 1;
 if (pages[pageIndex]) {
 navigateToPage(pages[pageIndex]);
 }
 }

 // Ctrl+B - Toggle sidebar (INTERNAL ONLY)
 if (keyEvent.ctrlKey && keyEvent.key === 'b') {
 toggleSidebar();
 }
 }
 });

 // === STATE ===
 let currentPage = 'capture';
 let selectedNavIndex = 0;
 const navItems = document.querySelectorAll('.nav-item');

 // === INITIALIZE ===
 document.addEventListener('DOMContentLoaded', () => {
 updateNavSelection();
 });

 // === NAVIGATE TO PAGE ===
 function navigateToPage(pageName) {
 // Hide all pages
 document.querySelectorAll('.view-page').forEach(page => {
 page.classList.remove('active');
 });

 // Show target page
 const targetPage = document.getElementById(`page-${pageName}`);
 if (targetPage) {
 targetPage.classList.add('active');
 currentPage = pageName;

 // Notify main process of page change (for smart toggle tracking)
 if (window.electronAPI && window.electronAPI.notifyPageChange) {
 window.electronAPI.notifyPageChange(pageName);
 }

 // Update title
 const titles = {
 'capture': 'Quick Capture',
 'hub': 'Hub',
 'reference': 'Quick Reference'
 };
 document.getElementById('pageTitle').textContent = titles[pageName] || pageName;

 // Update nav active state
 navItems.forEach(item => item.classList.remove('active'));
 const activeNav = document.querySelector(`[data-page=\"${pageName}\"]`);
 if (activeNav) {
 activeNav.classList.add('active');
 selectedNavIndex = Array.from(navItems).indexOf(activeNav);
 }
 }
 }

 // === TOGGLE SIDEBAR ===
 function toggleSidebar() {
 document.getElementById('sidebar').classList.toggle('collapsed');
 }

 // === SHOW KEYBOARD HINTS ===
 function showKeyboardHints() {
 const hint = document.getElementById('keyboardHint');
 hint.classList.add('show');
 setTimeout(() => {
 hint.classList.remove('show');
 }, 5000);
 }

 // === SHOW NOTIFICATION ===
 function showNotification(message, type = 'success') {
 const notification = document.getElementById('notification');
 notification.textContent = message;
 notification.className = `notification ${type}`;
 notification.classList.add('show');
 setTimeout(() => {
 notification.classList.remove('show');
 }, 3000);
 }

 // === SETTINGS (placeholder) ===
 function openSettings() {
 showNotification('Settings coming soon!');
 }

 // === ARROW KEY NAVIGATION ===
 function updateNavSelection() {
 navItems.forEach((item, index) => {
 if (index === selectedNavIndex) {
 item.style.outline = '2px solid #667eea';
 item.style.outlineOffset = '-2px';
 } else {
 item.style.outline = 'none';
 }
 });
 }

 // === CLICK NAVIGATION ===
 navItems.forEach(item => {
 item.addEventListener('click', () => {
 const page = item.getAttribute('data-page');
 navigateToPage(page);
 });
 });

 // === KEYBOARD SHORTCUTS (INTERNAL APP ONLY) ===
 document.addEventListener('keydown', (e) => {
 // Shift+? - Show shortcuts hint (FIXED)
 if (e.shiftKey && e.key === '?') {
 e.preventDefault();
 showKeyboardHints();
 }
 });

 // === ANTI-FREEZE WATCHDOG ===
 let lastInteraction = Date.now();

 document.addEventListener('mousemove', () => {
 lastInteraction = Date.now();
 });

 document.addEventListener('keydown', () => {
 lastInteraction = Date.now();
 });

 // Check every 5 seconds
 setInterval(() => {
 const timeSinceInteraction = Date.now() - lastInteraction;

 // If no interaction for 30sec AND app is focused
 if (timeSinceInteraction > 30000 && document.hasFocus()) {
 console.warn('Possible freeze detected, reloading active iframe');
 const activeIframe = document.querySelector('.view-page.active iframe');
 if (activeIframe) {
 activeIframe.src = activeIframe.src; // Force reload
 }
 }
 }, 5000);

 console.log('🥷 Ninja Mode Activated!');
 console.log('Global: Ctrl+Shift+Space/F/H | Internal: Ctrl+1/2/3, Ctrl+B, Shift+?');
 </script>

🔧 MISE À JOUR preload.js
Ajoute cette nouvelle API dans preload.js :
javascriptconst { contextBridge, ipcRenderer } = require('electron');

// Expose protected methods to renderer
contextBridge.exposeInMainWorld('electronAPI', {
 // File operations
 saveNote: (filename, content) => ipcRenderer.invoke('save-note', { filename, content }),

 // Platform info
 platform: process.platform,

 // Versions
 versions: {
 node: process.versions.node,
 chrome: process.versions.chrome,
 electron: process.versions.electron
 },

 // Navigation listeners
 onNavigate: (callback) => ipcRenderer.on('navigate-to', (_, page) => callback(page)),
 onToggleSidebar: (callback) => ipcRenderer.on('toggle-sidebar', callback),

 // NEW: Notify main process of page changes
 notifyPageChange: (page) => ipcRenderer.send('current-page-changed', page),

 // NEW: Hide window
 hideWindow: () => ipcRenderer.send('hide-window')
});

console.log('✅ Preload script loaded');
console.log(` Platform: ${process.platform}`);

🔧 MISE À JOUR Keyboard Hints Text
Dans app.html, trouve la div #keyboardHint et remplace le contenu par :
html <!-- Keyboard Shortcuts Hint -->
 <div id=\"keyboardHint\" class=\"keyboard-hint\">
 <div class=\"hint-title\">⌨️ Keyboard Shortcuts</div>
 <div class=\"hint-content\">
 <div class=\"hint-section\">
 <strong>🌍 Global (work when app closed):</strong><br>
 <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>Space</kbd> Toggle Capture<br>
 <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>F</kbd> Toggle Reference<br>
 <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>H</kbd> Toggle Hub
 </div>
 <div class=\"hint-section\">
 <strong>🏠 Internal Navigation:</strong><br>
 <kbd>Ctrl</kbd>+<kbd>1/2/3</kbd> Quick navigate pages<br>
 <kbd>Ctrl</kbd>+<kbd>B</kbd> Toggle sidebar<br>
 <kbd>Shift</kbd>+<kbd>?</kbd> Show this help
 </div>
 <div class=\"hint-section\">
 <strong>✍️ Capture Page:</strong><br>
 <kbd>Esc</kbd> Normal mode | <kbd>Ctrl</kbd>+<kbd>I</kbd> Insert mode<br>
 <kbd>Ctrl</kbd>+<kbd>S</kbd> Save | <kbd>Ctrl</kbd>+<kbd>K</kbd> Clear<br>
 <kbd>Ctrl</kbd>+<kbd>W</kbd> Quick save + hide
 </div>
 </div>
 </div>

✅ CHANGEMENTS APPLIQUÉS
✅ Fixé

✅ Shortcut ? → Shift+? (gère le Shift correctement)
✅ Notification du changement de page vers main.js
✅ Keyboard hints text mis à jour

✅ Supprimé

❌ Listeners redondants pour Ctrl+1/2/3 (maintenant SEULEMENT via relay iframe)
❌ Commentaires obsolètes

✅ Ajouté

✅ notifyPageChange() API dans preload
✅ Appel notifyPageChange(pageName) dans navigateToPage()
✅ Documentation shortcuts dans hints


🚀 TESTE

Remplace le <script> dans app.html
Remplace preload.js complet
Remplace les keyboard hints HTML
Restart app
Teste :

Shift+? → Devrait afficher les hints mis à jour
Ctrl+1/2/3 → Navigation marche
Change de page → Main.js devrait logger \"📄 Current page: X\"
Ctrl+Shift+Space 2x depuis Capture → Hide puis show


Balance ton feedback ! 💪Réessayer

---


## 🔗 Navigation

- ⬆️ Previous: [[397_assistant_msg-397]]
- ⬇️ Next: [[399_assistant_msg-399]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #receipts
- #code
- #automation
