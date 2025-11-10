---
type: chat-card
parent_export: '[[Export]]'
order: 182
role: assistant
created: '2025-11-10T03:56:31.320432Z'
tags:
- chat-card
- python
- obsidian
- code
- automation
attachments_count: 0
---

# 🤖 Message 182 - Assistant

**ID:** msg-182

## 💬 Content


**ID:** msg-182

javascriptconst { app, BrowserWindow, globalShortcut, ipcMain, Menu, Tray } = require('electron');
const path = require('path');

let mainWindow = null;
let tray = null;

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

// Global keyboard shortcuts for internal navigation
function setupGlobalKeyboardShortcuts() {
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

 tray.setToolTip('PKM System');
 tray.setContextMenu(contextMenu);
 } catch (err) {
 console.log('Tray icon not found, skipping tray');
 }
}

// Register global shortcuts for window toggle
function registerShortcuts() {
 // Ctrl+Shift+Space - Toggle main window + go to capture
 globalShortcut.register('CommandOrControl+Shift+Space', () => {
 if (mainWindow) {
 if (mainWindow.isVisible()) {
 mainWindow.hide();
 } else {
 mainWindow.show();
 mainWindow.webContents.send('navigate-to', 'capture');
 }
 } else {
 createMainWindow();
 }
 });

 // Ctrl+Shift+F - Toggle main window + go to reference
 globalShortcut.register('CommandOrControl+Shift+F', () => {
 if (mainWindow) {
 if (mainWindow.isVisible()) {
 mainWindow.hide();
 } else {
 mainWindow.show();
 mainWindow.webContents.send('navigate-to', 'reference');
 }
 } else {
 createMainWindow();
 }
 });

 console.log('✅ Global shortcuts registered!');
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

// App lifecycle
app.whenReady().then(() => {
 createMainWindow();
 createTray();
 registerShortcuts();
 setupGlobalKeyboardShortcuts();
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

---


## 🔗 Navigation

- ⬆️ Previous: [[181_assistant_msg-181]]
- ⬇️ Next: [[183_assistant_msg-183]]
- 📊 MOC: [[_MOC_French chat message instructions]]

## 🏷️ Topics

- #python
- #obsidian
- #code
- #automation
