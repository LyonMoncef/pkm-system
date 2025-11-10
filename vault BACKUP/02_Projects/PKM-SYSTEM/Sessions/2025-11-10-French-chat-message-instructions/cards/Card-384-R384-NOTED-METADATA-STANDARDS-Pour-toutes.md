---
type: chat-card
parent_export: '[[Export]]'
order: 384
role: assistant
created: '2025-11-10T21:12:07.672507Z'
tags:
- chat-card
- python
- obsidian
- code
- automation
attachments_count: 0
---

# 🤖 Message 384 - Assistant

**ID:** msg-384

## 💬 Content


**ID:** msg-384

📝 NOTED - METADATA STANDARDS
Pour toutes les futures cartes :
yaml---
title: \"Carte Title\"
date: 2025-10-24
timestamp: 2025-10-24T14:30:00Z
type: [decision-card | bug-card | feature-card | refactor-card]
status: [draft | in-progress | completed | archived]
project: pkm-system
phase: phase-1.5
tags: [shortcuts, refactor, architecture]
related: []
author: claude-moncef-collab
---
Compris poto ! 💪

🚀 STEP 1: CLEANUP main.js
🔧 CODE REFACTORÉ COMPLET
javascriptconst { app, BrowserWindow, globalShortcut, ipcMain, Menu, Tray } = require('electron');
const path = require('path');

let mainWindow = null;
let tray = null;
let currentPage = 'capture'; // Track current page for smart toggle

// Create main window (single window architecture)
function createMainWindow() {
 mainWindow = new BrowserWindow({
 width: 900,
 height: 700,
 webPreferences: {
 nodeIntegration: false,
 contextIsolation: true,
 preload: path.join(__dirname, '../preload/preload.js')
 },
 frame: true
 });

 mainWindow.loadFile(path.join(__dirname, '../renderer/app.html'));

 mainWindow.on('closed', () => {
 mainWindow = null;
 });
}

// Smart toggle: show/hide window based on state and target page
function smartToggle(targetPage) {
 if (!mainWindow) {
 // Window doesn't exist → Create + navigate
 createMainWindow();
 setTimeout(() => {
 mainWindow.webContents.send('navigate-to', targetPage);
 currentPage = targetPage;
 }, 500);
 } else if (!mainWindow.isVisible()) {
 // Window hidden → Show + navigate
 mainWindow.show();
 mainWindow.webContents.send('navigate-to', targetPage);
 currentPage = targetPage;
 } else {
 // Window visible → Smart behavior
 if (currentPage === targetPage) {
 // Already on target page → Hide (toggle off)
 mainWindow.hide();
 } else {
 // Different page → Navigate
 mainWindow.webContents.send('navigate-to', targetPage);
 currentPage = targetPage;
 }
 }
}

// Create system tray
function createTray() {
 const iconPath = path.join(__dirname, '../../build/icon.png');

 try {
 tray = new Tray(iconPath);

 const contextMenu = Menu.buildFromTemplate([
 { label: '🧠 PKM System', enabled: false },
 { type: 'separator' },
 {
 label: '🏠 Hub',
 click: () => smartToggle('hub')
 },
 {
 label: '✍️ Quick Capture',
 click: () => smartToggle('capture')
 },
 {
 label: '⚡ Quick Reference',
 click: () => smartToggle('reference')
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

 tray.setToolTip('PKM System');
 tray.setContextMenu(contextMenu);
 } catch (err) {
 console.log('Tray icon not found, skipping tray');
 }
}

// Register GLOBAL OS shortcuts (work when app closed)
function registerGlobalShortcuts() {
 // Ctrl+Shift+Space - Toggle Capture
 globalShortcut.register('CommandOrControl+Shift+Space', () => {
 smartToggle('capture');
 });

 // Ctrl+Shift+F - Toggle Reference
 globalShortcut.register('CommandOrControl+Shift+F', () => {
 smartToggle('reference');
 });

 // Ctrl+Shift+H - Toggle Hub (NEW)
 globalShortcut.register('CommandOrControl+Shift+H', () => {
 smartToggle('hub');
 });

 console.log('✅ Global OS shortcuts registered!');
}

// IPC handler for saving notes
ipcMain.handle('save-note', async (event, { filename, content }) => {
 const fs = require('fs').promises;
 const { dialog } = require('electron');

 try {
 const result = await dialog.showOpenDialog({
 properties: ['openDirectory'],
 title: 'Select Vault Directory'
 });

 if (result.canceled) return { success: false };

 const vaultPath = result.filePaths[0];
 const inboxPath = path.join(vaultPath, '00_Inbox');

 await fs.mkdir(inboxPath, { recursive: true });
 await fs.writeFile(path.join(inboxPath, filename), content, 'utf8');

 return { success: true };
 } catch (error) {
 return { success: false, error: error.message };
 }
});

// IPC handler for tracking current page
ipcMain.on('current-page-changed', (event, page) => {
 currentPage = page;
 console.log(`📄 Current page: ${page}`);
});

// IPC handler for hiding window
ipcMain.on('hide-window', () => {
 if (mainWindow) {
 mainWindow.hide();
 }
});

// App lifecycle
app.whenReady().then(() => {
 createMainWindow();
 createTray();
 registerGlobalShortcuts();
});

app.on('before-quit', () => {
 // Unregister shortcuts
 globalShortcut.unregisterAll();

 // Destroy tray
 if (tray) {
 tray.destroy();
 tray = null;
 }
});

app.on('will-quit', () => {
 // Double cleanup
 if (tray) {
 tray.destroy();
 tray = null;
 }
});

app.on('window-all-closed', () => {
 // Keep running on Windows/Linux
});

console.log('🧠 PKM System Starting...');

✅ CHANGEMENTS APPLIQUÉS
✅ Supprimé

❌ setupGlobalKeyboardShortcuts() (Ctrl+1/2/3/B ne sont PLUS globaux)
❌ Variables captureWindow, referenceWindow (déjà fait avant)

✅ Ajouté

✅ Variable currentPage pour tracking
✅ Fonction smartToggle(targetPage) avec logique intelligente
✅ Ctrl+Shift+H pour Hub
✅ IPC handler current-page-changed pour sync tracking
✅ IPC handler hide-window pour Ctrl+W

✅ Modifié

✅ registerShortcuts() → registerGlobalShortcuts() (nom plus clair)
✅ Tous les shortcuts utilisent smartToggle()
✅ Tray menu utilise smartToggle()


🚀 TESTE

Remplace main.js complet
Restart app
Teste :

Ctrl+Shift+Space → Toggle Capture
Ctrl+Shift+F → Toggle Reference
Ctrl+Shift+H → Toggle Hub (NEW)
Depuis Capture, fais Ctrl+Shift+Space → Devrait hide
App cachée, fais Ctrl+Shift+Space → Devrait show + Capture


Balance ton feedback ! 💪Réessayer

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-383-S383-ID-msg-383]]
- ⬇️ Next: [[Card-385-R385-NOTED-METADATA-STANDARDS-Pour-toutes]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #obsidian
- #code
- #automation
