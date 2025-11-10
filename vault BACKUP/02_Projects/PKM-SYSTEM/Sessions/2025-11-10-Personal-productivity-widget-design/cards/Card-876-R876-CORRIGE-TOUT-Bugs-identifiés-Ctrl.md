---
type: chat-card
parent_export: '[[Export]]'
order: 876
role: assistant
created: '2025-11-10T22:56:04.468840Z'
tags:
- chat-card
- python
- receipts
- code
- automation
attachments_count: 0
---

# 🤖 Message 876 - Assistant

**ID:** msg-876

## 💬 Content


**ID:** msg-876

OK ! ON CORRIGE TOUT ÇA ! 🔧
Bugs identifiés :

❌ Ctrl+Flèches → devrait naviguer direct (pas juste highlight)
❌ Ctrl+Chiffre ne marche pas sans focus sur sidebar
❌ Pas de focus auto dans textarea
❌ App plante / freeze parfois
❌ Ctrl+B (toggle sidebar) ne marche pas
❌ Tray icon fantôme reste après quit

ON RÈGLE TOUT ! 💪

🔧 FIX 1 : NAVIGATION DIRECTE AVEC CTRL+FLÈCHES
Dans app.html, trouve la section keyboard shortcuts (vers la fin) :
Remplace tout le bloc des flèches par :
javascript// Arrow keys - Navigate directly (no Enter needed)
if (e.ctrlKey && e.key === 'ArrowDown') {
 e.preventDefault();
 selectedNavIndex = (selectedNavIndex + 1) % navItems.length;
 const selectedNav = navItems[selectedNavIndex];
 const page = selectedNav.getAttribute('data-page');
 navigateToPage(page); // Navigate immédiatement
}

if (e.ctrlKey && e.key === 'ArrowUp') {
 e.preventDefault();
 selectedNavIndex = (selectedNavIndex - 1 + navItems.length) % navItems.length;
 const selectedNav = navItems[selectedNavIndex];
 const page = selectedNav.getAttribute('data-page');
 navigateToPage(page); // Navigate immédiatement
}
Supprime le bloc \"Enter - Select nav item\" (plus besoin) :
javascript// SUPPRIME ÇA :
// if (e.key === 'Enter' && document.activeElement === document.body) {
// const selectedNav = navItems[selectedNavIndex];
// const page = selectedNav.getAttribute('data-page');
// navigateToPage(page);
// }

🔧 FIX 2 : CTRL+CHIFFRE MARCHE PARTOUT
Le problème : Les iframes \"volent\" les events clavier
Solution : Écouter au niveau de la fenêtre principale
Dans main.js, ajoute ça APRÈS la fonction createMainWindow() :
javascript// Global keyboard listener (au niveau Electron)
function setupGlobalKeyboardShortcuts() {
 const { globalShortcut } = require('electron');

 // Ctrl+1/2/3 pour navigation interne
 globalShortcut.register('CommandOrControl+1', () => {
 if (mainWindow) {
 mainWindow.webContents.send('navigate-to', 'capture');
 }
 });

 globalShortcut.register('CommandOrControl+2', () => {
 if (mainWindow) {
 mainWindow.webContents.send('navigate-to', 'hub');
 }
 });

 globalShortcut.register('CommandOrControl+3', () => {
 if (mainWindow) {
 mainWindow.webContents.send('navigate-to', 'reference');
 }
 });

 // Ctrl+B pour toggle sidebar
 globalShortcut.register('CommandOrControl+B', () => {
 if (mainWindow) {
 mainWindow.webContents.send('toggle-sidebar');
 }
 });
}
Puis dans app.whenReady(), ajoute l'appel :
javascriptapp.whenReady().then(() => {
 createMainWindow();
 createTray();
 registerShortcuts();
 setupGlobalKeyboardShortcuts(); // ← AJOUTE ÇA
 // ...
});
Puis dans app.html, ajoute le listener IPC :
javascript// Juste après le script qui commence
if (window.electronAPI) {
 // Écoute les commandes de navigation
 window.addEventListener('message', (event) => {
 if (event.data.type === 'navigate-to') {
 navigateToPage(event.data.page);
 }
 if (event.data.type === 'toggle-sidebar') {
 toggleSidebar();
 }
 });
}
Attends, mieux : utilise l'IPC renderer
Dans preload.js, ajoute :
javascriptconst { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electronAPI', {
 // Existing
 saveNote: (filename, content) => ipcRenderer.invoke('save-note', { filename, content }),
 platform: process.platform,
 versions: { /* ... */ },

 // NEW
 onNavigate: (callback) => ipcRenderer.on('navigate-to', (_, page) => callback(page)),
 onToggleSidebar: (callback) => ipcRenderer.on('toggle-sidebar', callback)
});
Puis dans app.html :
javascript// Setup IPC listeners
if (window.electronAPI) {
 window.electronAPI.onNavigate((page) => {
 navigateToPage(page);
 });

 window.electronAPI.onToggleSidebar(() => {
 toggleSidebar();
 });
}

🔧 FIX 3 : AUTO-FOCUS DANS TEXTAREA
Le problème : L'iframe charge capture.html mais le focus ne va pas dans le textarea
Solution : Dans capture.html, ajoute au load :
javascript// À la toute fin du script, APRÈS le window.addEventListener('load')

// Force focus dans textarea au chargement
window.addEventListener('load', () => {
 const autosaved = localStorage.getItem('pkm-autosave');
 if (autosaved) {
 editor.value = autosaved;
 updatePreview();
 lastSaved.textContent = 'Restored from autosave';
 }

 // AJOUTE ÇA :
 // Focus automatique dans l'éditeur
 setTimeout(() => {
 editor.focus();
 }, 100);
});

🔧 FIX 4 : APP QUI PLANTE/FREEZE
Cause probable : Les iframes qui bloquent
Solution temporaire : Reload l'iframe si freeze détecté
Dans app.html, ajoute un watchdog :
javascript// Anti-freeze watchdog
let lastInteraction = Date.now();

document.addEventListener('mousemove', () => {
 lastInteraction = Date.now();
});

document.addEventListener('keydown', () => {
 lastInteraction = Date.now();
});

// Check toutes les 5 secondes
setInterval(() => {
 const timeSinceInteraction = Date.now() - lastInteraction;

 // Si pas d'interaction depuis 30 sec ET app active
 if (timeSinceInteraction > 30000 && document.hasFocus()) {
 console.warn('Possible freeze detected, reloading active iframe');
 const activeIframe = document.querySelector('.view-page.active iframe');
 if (activeIframe) {
 activeIframe.src = activeIframe.src; // Force reload
 }
 }
}, 5000);
Mais mieux : identifie POURQUOI ça freeze. Tu as des erreurs dans la console ?

🔧 FIX 5 : TOGGLE SIDEBAR NE MARCHE PAS
Vérifie que la fonction toggleSidebar() existe dans app.html :
javascript// Toggle sidebar
function toggleSidebar() {
 const sidebar = document.getElementById('sidebar');
 sidebar.classList.toggle('collapsed');
}
Et que le bouton appelle bien la fonction :
html<button class=\"toggle-sidebar-btn\" onclick=\"toggleSidebar()\">☰</button>

🔧 FIX 6 : TRAY ICON FANTÔME
Dans main.js, ajoute un cleanup proper :
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
ET dans la fonction createTray(), gère mieux le quit :
javascript// Dans le menu tray
{
 label: 'Quit',
 click: () => {
 // Détruire tray AVANT quit
 if (tray) {
 tray.destroy();
 tray = null;
 }
 app.quit();
 }
}

🧪 TEST RAPIDE
Après avoir fait tous ces changements :
powershellnpm start
Teste :

✅ Ctrl+↑↓ navigue direct ?
✅ Ctrl+1/2/3 marche partout ?
✅ Focus auto dans textarea ?
✅ Ctrl+B toggle sidebar ?
✅ Quit → Tray disparaît proprement ?


💬 DIS-MOI
Fais les changements, teste, et dis-moi :
A) Tous les bugs fixés ! 🎉
B) Certains bugs persistent → Lesquels ?
C) Nouvelles erreurs → Montre-moi
GO ! 🔥💪

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-875-R875-CORRIGE-TOUT-Bugs-identifiés-Ctrl]]
- ⬇️ Next: [[Card-877-R877-CORRIGE-TOUT-Bugs-identifiés-Ctrl]]
- 📊 MOC: [[_MOC_Personal productivity widget design]]

## 🏷️ Topics

- #python
- #receipts
- #code
- #automation
