diff --git a/electron/icon.svg b/electron/icon.svg
new file mode 100644
index 0000000..1062cd3
--- /dev/null
+++ b/electron/icon.svg
@@ -0,0 +1,14 @@
+<svg width="512" height="512" xmlns="http://www.w3.org/2000/svg">
+  <defs>
+    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
+      <stop offset="0%" style="stop-color:#667eea;stop-opacity:1" />
+      <stop offset="100%" style="stop-color:#764ba2;stop-opacity:1" />
+    </linearGradient>
+  </defs>
+  
+  <!-- Background circle -->
+  <circle cx="256" cy="256" r="240" fill="url(#grad)"/>
+  
+  <!-- Brain icon -->
+  <text x="256" y="340" font-size="200" text-anchor="middle" fill="white">🧠</text>
+</svg>
diff --git a/electron/package.json b/electron/package.json
index 91fb8fd..b395c2a 100644
--- a/electron/package.json
+++ b/electron/package.json
@@ -4,7 +4,7 @@
   "description": "Personal Knowledge Management System - Desktop App",
   "main": "src/main/main.js",
   "scripts": {
-    "start": "electron .",
+    "start": "electron . --trace-warnings",
     "dev": "electron . --trace-warnings",
     "build": "electron-builder",
     "build:win": "electron-builder --win",
diff --git a/electron/src/main/main.js b/electron/src/main/main.js
index b8faf4f..1f5a0dd 100644
--- a/electron/src/main/main.js
+++ b/electron/src/main/main.js
@@ -1,252 +1,260 @@
-const { cconst { app, BrowserWindow, globalShortcut, ipcMain, Menu, Tray } = require('electron');
+const { app, BrowserWindow, globalShortcut, ipcMain, Menu, Tray } = require('electron');
 const path = require('path');
 
 let mainWindow = null;
-let captureWindow = null;
-let referenceWindow = null;
 let tray = null;
+let currentPage = 'capture'; // Track current page for smart toggle
 
-// Create main hub window
+// Create main window (single window architecture)
 function createMainWindow() {
     mainWindow = new BrowserWindow({
-        width: 600,
+        width: 900,
         height: 700,
         webPreferences: {
             nodeIntegration: false,
             contextIsolation: true,
             preload: path.join(__dirname, '../preload/preload.js')
         },
-        frame: true,
-        icon: path.join(__dirname, '../../build/icon.png')
+        frame: true
     });
 
-    mainWindow.loadFile(path.join(__dirname, '../renderer/hub.html'));
-
-    // Open DevTools in development
-    if (process.env.NODE_ENV === 'development') {
-        mainWindow.webContents.openDevTools();
-    }
+    mainWindow.loadFile(path.join(__dirname, '../renderer/app.html'));
 
     mainWindow.on('closed', () => {
         mainWindow = null;
     });
 }
 
-// Create Quick Capture window
-function createCaptureWindow() {
-    if (captureWindow) {
-        captureWindow.focus();
-        return;
+// Smart toggle: show/hide window based on state and target page
+function smartToggle(targetPage) {
+    if (!mainWindow) {
+        // Window doesn't exist → Create + navigate
+        createMainWindow();
+        setTimeout(() => {
+            mainWindow.webContents.send('navigate-to', targetPage);
+            currentPage = targetPage;
+        }, 500);
+    } else if (!mainWindow.isVisible()) {
+        // Window hidden → Show + navigate
+        mainWindow.show();
+        mainWindow.webContents.send('navigate-to', targetPage);
+        currentPage = targetPage;
+    } else {
+        // Window visible → Smart behavior
+        if (currentPage === targetPage) {
+            // Already on target page → Hide (toggle off)
+            mainWindow.hide();
+        } else {
+            // Different page → Navigate
+            mainWindow.webContents.send('navigate-to', targetPage);
+            currentPage = targetPage;
+        }
     }
-
-    captureWindow = new BrowserWindow({
-        width: 900,
-        height: 700,
-        webPreferences: {
-            nodeIntegration: false,
-            contextIsolation: true,
-            preload: path.join(__dirname, '../preload/preload.js')
-        },
-        frame: true,
-        icon: path.join(__dirname, '../../build/icon.png')
-    });
-
-    captureWindow.loadFile(path.join(__dirname, '../renderer/capture.html'));
-
-    captureWindow.on('closed', () => {
-        captureWindow = null;
-    });
 }
 
-// Create Quick Reference window
-function createReferenceWindow() {
-    if (referenceWindow) {
-        referenceWindow.focus();
-        return;
+// Create system tray
+function createTray() {
+    const iconPath = path.join(__dirname, '../../build/icon.png');
+    
+    try {
+        tray = new Tray(iconPath);
+        
+        const contextMenu = Menu.buildFromTemplate([
+            { label: '🧠 PKM System', enabled: false },
+            { type: 'separator' },
+            { 
+                label: '🏠 Hub', 
+                click: () => smartToggle('hub')
+            },
+            { 
+                label: '✍️ Quick Capture', 
+                click: () => smartToggle('capture')
+            },
+            { 
+                label: '⚡ Quick Reference', 
+                click: () => smartToggle('reference')
+            },
+            { type: 'separator' },
+            { 
+                label: 'Quit',
+                click: () => {
+                    if (tray) {
+                        tray.destroy();
+                        tray = null;
+                    }
+                    app.quit();
+                }
+            }
+        ]);
+
+        tray.setToolTip('PKM System');
+        tray.setContextMenu(contextMenu);
+    } catch (err) {
+        console.log('Tray icon not found, skipping tray');
     }
+}
 
-    referenceWindow = new BrowserWindow({
-        width: 700,
-        height: 800,
-        webPreferences: {
-            nodeIntegration: false,
-            contextIsolation: true,
-            preload: path.join(__dirname, '../preload/preload.js')
-        },
-        frame: true,
-        icon: path.join(__dirname, '../../build/icon.png')
+// Register GLOBAL OS shortcuts (work when app closed)
+function registerGlobalShortcuts() {
+    // Ctrl+Shift+Space - Toggle Capture
+    globalShortcut.register('CommandOrControl+Shift+Space', () => {
+        smartToggle('capture');
     });
 
-    referenceWindow.loadFile(path.join(__dirname, '../renderer/reference.html'));
+    // Ctrl+Shift+F - Toggle Reference
+    globalShortcut.register('CommandOrControl+Shift+F', () => {
+        smartToggle('reference');
+    });
 
-    referenceWindow.on('closed', () => {
-        referenceWindow = null;
+    // Ctrl+Shift+H - Toggle Hub (NEW)
+    globalShortcut.register('CommandOrControl+Shift+H', () => {
+        smartToggle('hub');
     });
-}
 
-// Create system tray
-function createTray() {
-    tray = new Tray(path.join(__dirname, '../../build/icon.png'));
-    
-    const contextMenu = Menu.buildFromTemplate([
-        {
-            label: '🧠 PKM System',
-            type: 'normal',
-            enabled: false
-        },
-        { type: 'separator' },
-        {
-            label: '🏠 Hub',
-            click: () => {
-                if (mainWindow) {
-                    mainWindow.show();
-                    mainWindow.focus();
-                } else {
-                    createMainWindow();
-                }
-            }
-        },
-        {
-            label: '✍️ Quick Capture',
-            accelerator: 'CmdOrCtrl+Shift+Space',
-            click: createCaptureWindow
-        },
-        {
-            label: '⚡ Quick Reference',
-            accelerator: 'CmdOrCtrl+Shift+F',
-            click: createReferenceWindow
-        },
-        { type: 'separator' },
-        {
-            label: 'Quit',
-            click: () => {
-                app.quit();
-            }
+    // Ctrl+W - Quick save + hide window (GLOBAL)
+    globalShortcut.register('CommandOrControl+W', () => {
+        if (mainWindow && mainWindow.isVisible()) {
+            // Send signal to save before hiding
+            mainWindow.webContents.send('quick-save-and-hide');
         }
-    ]);
-
-    tray.setToolTip('PKM System');
-    tray.setContextMenu(contextMenu);
+    });
 
-    // Click on tray icon shows main window
-    tray.on('click', () => {
-        if (mainWindow) {
-            mainWindow.isVisible() ? mainWindow.hide() : mainWindow.show();
+    // === TEST SHORTCUTS HELP (3 raccourcis pour debug) ===
+    
+    // F1 - Show keyboard shortcuts
+    globalShortcut.register('F1', () => {
+        console.log('🔑 F1 pressed!');
+        if (mainWindow && mainWindow.isVisible()) {
+            mainWindow.webContents.send('show-shortcuts');
+        } else if (mainWindow) {
+            mainWindow.show();
+            setTimeout(() => {
+                mainWindow.webContents.send('show-shortcuts');
+            }, 300);
         } else {
             createMainWindow();
+            setTimeout(() => {
+                mainWindow.webContents.send('show-shortcuts');
+            }, 800);
         }
     });
-}
 
-// Register global shortcuts
-function registerShortcuts() {
-    // Ctrl+Shift+Space - Quick Capture
-    const captureShortcut = globalShortcut.register('CommandOrControl+Shift+Space', () => {
-        if (captureWindow) {
-            if (captureWindow.isVisible()) {
-                captureWindow.hide();
-            } else {
-                captureWindow.show();
-                captureWindow.focus();
-            }
+    // Ctrl+/ - Show keyboard shortcuts
+    globalShortcut.register('CommandOrControl+/', () => {
+        console.log('🔑 Ctrl+/ pressed!');
+        if (mainWindow && mainWindow.isVisible()) {
+            mainWindow.webContents.send('show-shortcuts');
+        } else if (mainWindow) {
+            mainWindow.show();
+            setTimeout(() => {
+                mainWindow.webContents.send('show-shortcuts');
+            }, 300);
         } else {
-            createCaptureWindow();
+            createMainWindow();
+            setTimeout(() => {
+                mainWindow.webContents.send('show-shortcuts');
+            }, 800);
         }
     });
 
-    if (!captureShortcut) {
-        console.log('Failed to register Quick Capture shortcut');
-    }
-
-    // Ctrl+Shift+F - Quick Reference
-    const refShortcut = globalShortcut.register('CommandOrControl+Shift+F', () => {
-        if (referenceWindow) {
-            if (referenceWindow.isVisible()) {
-                referenceWindow.hide();
-            } else {
-                referenceWindow.show();
-                referenceWindow.focus();
-            }
+    // Ctrl+Shift+L - Show keyboard shortcuts (test)
+    globalShortcut.register('CommandOrControl+Shift+L', () => {
+        console.log('🔑 Ctrl+Shift+L pressed!');
+        if (mainWindow && mainWindow.isVisible()) {
+            mainWindow.webContents.send('show-shortcuts');
+        } else if (mainWindow) {
+            mainWindow.show();
+            setTimeout(() => {
+                mainWindow.webContents.send('show-shortcuts');
+            }, 300);
         } else {
-            createReferenceWindow();
+            createMainWindow();
+            setTimeout(() => {
+                mainWindow.webContents.send('show-shortcuts');
+            }, 800);
         }
     });
 
-    if (!refShortcut) {
-        console.log('Failed to register Quick Reference shortcut');
-    }
+    // Ctrl+Shift+W - Quit app completely (kill process)
+    globalShortcut.register('CommandOrControl+Shift+W', () => {
+        console.log('🔴 Force quit requested');
+        if (tray) {
+            tray.destroy();
+            tray = null;
+        }
+        app.quit();
+        process.exit(0); // Force kill
+    });
 
-    console.log('✅ Global shortcuts registered!');
-    console.log('   Ctrl+Shift+Space - Quick Capture');
-    console.log('   Ctrl+Shift+F - Quick Reference');
+    console.log('✅ Global OS shortcuts registered!');
 }
 
-// IPC handlers for file operations
+// IPC handler for saving notes
 ipcMain.handle('save-note', async (event, { filename, content }) => {
     const fs = require('fs').promises;
     const { dialog } = require('electron');
     
     try {
-        // Ask user for vault location (first time)
         const result = await dialog.showOpenDialog({
             properties: ['openDirectory'],
-            title: 'Select Vault Directory',
-            buttonLabel: 'Select Vault'
+            title: 'Select Vault Directory'
         });
 
-        if (result.canceled) {
-            return { success: false, error: 'Cancelled' };
-        }
+        if (result.canceled) return { success: false };
 
         const vaultPath = result.filePaths[0];
         const inboxPath = path.join(vaultPath, '00_Inbox');
         
-        // Create 00_Inbox if doesn't exist
-        try {
-            await fs.access(inboxPath);
-        } catch {
-            await fs.mkdir(inboxPath, { recursive: true });
-        }
-
-        const filePath = path.join(inboxPath, filename);
-        await fs.writeFile(filePath, content, 'utf8');
+        await fs.mkdir(inboxPath, { recursive: true });
+        await fs.writeFile(path.join(inboxPath, filename), content, 'utf8');
 
-        return { success: true, path: filePath };
+        return { success: true };
     } catch (error) {
-        console.error('Error saving note:', error);
         return { success: false, error: error.message };
     }
 });
 
+// IPC handler for tracking current page
+ipcMain.on('current-page-changed', (event, page) => {
+    currentPage = page;
+    console.log(`📄 Current page: ${page}`);
+});
+
+// IPC handler for hiding window
+ipcMain.on('hide-window', () => {
+    if (mainWindow) {
+        mainWindow.hide();
+    }
+});
+
 // App lifecycle
 app.whenReady().then(() => {
     createMainWindow();
     createTray();
-    registerShortcuts();
-
-    app.on('activate', () => {
-        if (BrowserWindow.getAllWindows().length === 0) {
-            createMainWindow();
-        }
-    });
+    registerGlobalShortcuts();
 });
 
-app.on('window-all-closed', () => {
-    // Keep app running in tray on macOS
-    if (process.platform !== 'darwin') {
-        // On Windows/Linux, keep running in background
-        // User must quit via tray menu
+app.on('before-quit', () => {
+    // Unregister shortcuts
+    globalShortcut.unregisterAll();
+    
+    // Destroy tray
+    if (tray) {
+        tray.destroy();
+        tray = null;
     }
 });
 
 app.on('will-quit', () => {
-    // Unregister all shortcuts
-    globalShortcut.unregisterAll();
+    // Double cleanup
+    if (tray) {
+        tray.destroy();
+        tray = null;
+    }
+});
+
+app.on('window-all-closed', () => {
+    // Keep running on Windows/Linux
 });
 
-// Log app info
 console.log('🧠 PKM System Starting...');
-console.log(`   Electron: ${process.versions.electron}`);
-console.log(`   Chrome: ${process.versions.chrome}`);
-console.log(`   Node: ${process.versions.node}`);
-console.log(`   Platform: ${process.platform}`);ontextBridge, ipcRenderer } = require('electron');
diff --git a/electron/src/preload/preload.js b/electron/src/preload/preload.js
index e78f8c3..75ce297 100644
--- a/electron/src/preload/preload.js
+++ b/electron/src/preload/preload.js
@@ -13,8 +13,22 @@ contextBridge.exposeInMainWorld('electronAPI', {
         node: process.versions.node,
         chrome: process.versions.chrome,
         electron: process.versions.electron
-    }
+    },
+    
+    // Navigation listeners
+    onNavigate: (callback) => ipcRenderer.on('navigate-to', (_, page) => callback(page)),
+    onToggleSidebar: (callback) => ipcRenderer.on('toggle-sidebar', callback),
+    onShowShortcuts: (callback) => ipcRenderer.on('show-shortcuts', callback),
+    
+    // NEW: Notify main process of page changes
+    notifyPageChange: (page) => ipcRenderer.send('current-page-changed', page),
+    
+    // NEW: Hide window
+    hideWindow: () => ipcRenderer.send('hide-window')
+    // Quick save and hide listener
+    onQuickSaveAndHide: (callback) => ipcRenderer.on('quick-save-and-hide', callback),
 });
 
 console.log('✅ Preload script loaded');
 console.log(`   Platform: ${process.platform}`);
+
diff --git a/electron/src/renderer/app.html b/electron/src/renderer/app.html
new file mode 100644
index 0000000..f0a304f
--- /dev/null
+++ b/electron/src/renderer/app.html
@@ -0,0 +1,662 @@
+<!DOCTYPE html>
+<html lang="en">
+<head>
+    <meta charset="UTF-8">
+    <meta name="viewport" content="width=device-width, initial-scale=1.0">
+    <title>PKM System</title>
+</head>
+    <style>
+        * {
+            margin: 0;
+            padding: 0;
+            box-sizing: border-box;
+        }
+
+        body {
+            font-family: 'Monaco', 'Consolas', 'Courier New', monospace;
+            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
+            overflow: hidden;
+        }
+
+        .app-container {
+            display: flex;
+            height: 100vh;
+            width: 100vw;
+            overflow: hidden;
+        }
+
+        /* SIDEBAR */
+        #sidebar {
+            width: 250px;
+            min-width: 250px;
+            background: rgba(20, 20, 30, 0.95);
+            border-right: 1px solid rgba(255, 255, 255, 0.1);
+            display: flex;
+            flex-direction: column;
+            transition: all 0.3s ease;
+            overflow: hidden;
+            backdrop-filter: blur(20px);
+        }
+
+        #sidebar.collapsed {
+            width: 0;
+            min-width: 0;
+            border-right: none;
+        }
+
+        .sidebar-header {
+            padding: 20px;
+            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
+            background: rgba(255, 255, 255, 0.05);
+        }
+
+        .app-logo {
+            display: flex;
+            align-items: center;
+            gap: 12px;
+            color: white;
+            font-size: 20px;
+            font-weight: 600;
+        }
+
+        .nav-section {
+            flex: 1;
+            padding: 20px 0;
+            overflow-y: auto;
+        }
+
+        .nav-item {
+            padding: 12px 20px;
+            display: flex;
+            align-items: center;
+            gap: 12px;
+            cursor: pointer;
+            transition: all 0.2s;
+            color: rgba(255, 255, 255, 0.6);
+            border-left: 3px solid transparent;
+        }
+
+        .nav-item:hover {
+            background: rgba(255, 255, 255, 0.05);
+            color: white;
+        }
+
+        .nav-item.active {
+            background: rgba(102, 126, 234, 0.2);
+            color: white;
+            border-left-color: #667eea;
+        }
+
+        .nav-icon {
+            font-size: 20px;
+        }
+
+        .nav-content {
+            flex: 1;
+        }
+
+        .nav-label {
+            font-size: 14px;
+            font-weight: 600;
+        }
+
+        .nav-shortcut {
+            font-size: 11px;
+            color: rgba(255, 255, 255, 0.4);
+            margin-top: 2px;
+        }
+
+        .sidebar-footer {
+            padding: 16px 20px;
+            border-top: 1px solid rgba(255, 255, 255, 0.1);
+        }
+
+        .footer-item {
+            padding: 8px 0;
+            cursor: pointer;
+            color: rgba(255, 255, 255, 0.5);
+            font-size: 13px;
+            transition: color 0.2s;
+            display: flex;
+            align-items: center;
+            gap: 8px;
+        }
+
+        .footer-item:hover {
+            color: #667eea;
+        }
+
+        /* MAIN CONTENT */
+        .main-content {
+            flex: 1;
+            display: flex;
+            flex-direction: column;
+            overflow: hidden;
+            min-width: 0; /* Important pour le flex shrink */
+        }
+
+        .content-header {
+            display: flex;
+            align-items: center;
+            justify-content: space-between;
+            padding: 16px 24px;
+            background: rgba(20, 20, 30, 0.9);
+            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
+            backdrop-filter: blur(20px);
+        }
+
+        .toggle-sidebar-btn {
+            background: rgba(255, 255, 255, 0.1);
+            border: 1px solid rgba(255, 255, 255, 0.15);
+            color: white;
+            padding: 8px 12px;
+            border-radius: 6px;
+            cursor: pointer;
+            font-size: 18px;
+            transition: all 0.2s;
+        }
+
+        .toggle-sidebar-btn:hover {
+            background: rgba(255, 255, 255, 0.15);
+            border-color: #667eea;
+        }
+
+        .content-title {
+            color: white;
+            font-size: 18px;
+            font-weight: 600;
+            flex: 1;
+            text-align: center;
+        }
+
+        .header-actions {
+            display: flex;
+            gap: 8px;
+        }
+
+        .header-btn {
+            background: rgba(102, 126, 234, 0.2);
+            border: 1px solid rgba(102, 126, 234, 0.4);
+            color: white;
+            padding: 8px 16px;
+            border-radius: 6px;
+            cursor: pointer;
+            font-size: 13px;
+            transition: all 0.2s;
+            display: flex;
+            align-items: center;
+            gap: 6px;
+        }
+
+        .header-btn:hover {
+            background: rgba(102, 126, 234, 0.3);
+            border-color: #667eea;
+        }
+
+        .view-container {
+            flex: 1;
+            overflow: hidden;
+            position: relative;
+            width: 100%;
+        }
+
+        .view-page {
+            display: none;
+            width: 100%;
+            height: 100%;
+        }
+
+        .view-page.active {
+            display: block;
+        }
+
+        .view-page iframe {
+            width: 100%;
+            height: 100%;
+            border: none;
+        }
+
+        /* NOTIFICATIONS */
+        .notification {
+            position: fixed;
+            top: 20px;
+            right: 20px;
+            padding: 16px 24px;
+            background: rgba(20, 20, 30, 0.95);
+            border: 1px solid rgba(255, 255, 255, 0.2);
+            border-radius: 8px;
+            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
+            backdrop-filter: blur(20px);
+            color: white;
+            opacity: 0;
+            transform: translateY(-20px);
+            transition: all 0.3s;
+            z-index: 10000;
+        }
+
+        .notification.show {
+            opacity: 1;
+            transform: translateY(0);
+        }
+
+        /* KEYBOARD HINTS */
+        .keyboard-hint {
+            position: fixed;
+            top: 50%;
+            left: 50%;
+            transform: translate(-50%, -50%);
+            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
+            padding: 30px 40px;
+            border-radius: 16px;
+            box-shadow: 0 20px 60px rgba(102, 126, 234, 0.4);
+            z-index: 10000;
+            opacity: 0;
+            pointer-events: none;
+            transition: opacity 0.3s ease;
+            max-width: 700px;
+            width: 90%;
+            color: white;
+        }
+
+        .keyboard-hint.show {
+            opacity: 1;
+            pointer-events: auto;
+        }
+
+        .hint-title {
+            font-size: 28px;
+            font-weight: bold;
+            margin-bottom: 24px;
+            text-align: center;
+            color: white;
+            text-shadow: 0 2px 4px rgba(0,0,0,0.2);
+        }
+
+        .hint-content {
+            display: grid;
+            grid-template-columns: 1fr;
+            gap: 20px;
+            font-size: 15px;
+            line-height: 1.8;
+        }
+
+        .hint-section {
+            padding: 20px;
+            background: rgba(255, 255, 255, 0.1);
+            border-radius: 12px;
+            backdrop-filter: blur(10px);
+            border: 1px solid rgba(255, 255, 255, 0.2);
+        }
+
+        .hint-section strong {
+            display: block;
+            margin-bottom: 12px;
+            color: #ffd700;
+            font-size: 17px;
+            text-shadow: 0 1px 2px rgba(0,0,0,0.2);
+        }
+
+        .keyboard-hint kbd {
+            background: rgba(255, 255, 255, 0.2);
+            color: white;
+            padding: 6px 10px;
+            border-radius: 6px;
+            font-family: 'Courier New', monospace;
+            font-size: 14px;
+            font-weight: bold;
+            margin: 0 3px;
+            border: 1px solid rgba(255, 255, 255, 0.3);
+            box-shadow: 0 2px 4px rgba(0,0,0,0.2);
+        }
+        /* STATUS BAR */
+        .status-bar {
+            padding: 12px 24px;
+            background: rgba(102, 126, 234, 0.1);
+            border-top: 1px solid rgba(102, 126, 234, 0.2);
+            display: flex;
+            justify-content: space-between;
+            align-items: center;
+            font-size: 12px;
+            color: #a5b4fc;
+        }
+
+        .status-left {
+            display: flex;
+            gap: 20px;
+            align-items: center;
+        }
+
+        .status-item {
+            display: flex;
+            align-items: center;
+            gap: 8px;
+        }
+
+        .status-dot {
+            width: 6px;
+            height: 6px;
+            border-radius: 50%;
+            background: #27c93f;
+            animation: pulse 2s infinite;
+        }
+
+        @keyframes pulse {
+            0%, 100% { opacity: 1; }
+            50% { opacity: 0.5; }
+        }
+
+        .status-right {
+            color: rgba(255, 255, 255, 0.5);
+        }
+    </style>
+<body>
+    <div class="app-container">
+        <!-- Sidebar -->
+        <nav class="sidebar" id="sidebar">
+            <div class="sidebar-header">
+                <div class="sidebar-logo">🧠</div>
+                <div class="sidebar-title">PKM System</div>
+            </div>
+
+            <div class="sidebar-nav">
+                <div class="nav-item active" data-page="capture">
+                    <div class="nav-icon">✍️</div>
+                    <div class="nav-content">
+                        <div class="nav-label">Quick Capture</div>
+                        <div class="nav-shortcut">Ctrl+1</div>
+                    </div>
+                </div>
+
+                <div class="nav-item" data-page="hub">
+                    <div class="nav-icon">🏠</div>
+                    <div class="nav-content">
+                        <div class="nav-label">Hub</div>
+                        <div class="nav-shortcut">Ctrl+2</div>
+                    </div>
+                </div>
+
+                <div class="nav-item" data-page="reference">
+                    <div class="nav-icon">⚡</div>
+                    <div class="nav-content">
+                        <div class="nav-label">Quick Reference</div>
+                        <div class="nav-shortcut">Ctrl+3</div>
+                    </div>
+                </div>
+            </div>
+
+            <div class="sidebar-footer">
+                <div class="footer-item" onclick="openSettings()">
+                    <span>⚙️</span>
+                    <span>Settings</span>
+                </div>
+                <div class="footer-item" onclick="showKeyboardHints()">
+                    <span>⌨️</span>
+                    <span>Shortcuts</span>
+                </div>
+            </div>
+        </nav>
+
+        <!-- Main Content -->
+        <div class="main-content">
+            <div class="content-header">
+                <button class="toggle-sidebar-btn" onclick="toggleSidebar()">☰</button>
+                <div class="content-title" id="pageTitle">Quick Capture</div>
+                <div class="header-actions">
+                    <button class="header-btn" onclick="showKeyboardHints()">⌨️ Shortcuts</button>
+                </div>
+            </div>
+
+            <div class="view-container">
+                <!-- Quick Capture View -->
+                <div class="view-page active" id="page-capture">
+                    <iframe src="capture.html" style="width: 100%; height: 100%; border: none;"></iframe>
+                </div>
+
+                <!-- Hub View -->
+                <div class="view-page" id="page-hub">
+                    <iframe src="hub.html" style="width: 100%; height: 100%; border: none;"></iframe>
+                </div>
+
+                <!-- Quick Reference View -->
+                <div class="view-page" id="page-reference">
+                    <iframe src="reference.html" style="width: 100%; height: 100%; border: none;"></iframe>
+                </div>
+            </div>
+            <div class="status-bar">
+                <div class="status-left">
+                    <div class="status-item">
+                        <div class="status-dot"></div>
+                        <span>Ready</span>
+                    </div>
+                    <div class="status-item">
+                        <span>Vault: Configured</span>
+                    </div>
+                </div>
+                <div class="status-right">
+                    Press Ctrl+Shift+I for shortcuts
+                </div>
+            </div>
+        </div>
+    </div>
+
+    <!-- Keyboard Shortcuts Hint -->
+        <div id="keyboardHint" class="keyboard-hint">
+            <div class="hint-title">⌨️ Keyboard Shortcuts</div>
+            <div class="hint-content">
+                <div class="hint-section">
+                    <strong>🌍 Global (work when app closed):</strong><br>
+                    <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>Space</kbd> Toggle Capture<br>
+                    <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>F</kbd> Toggle Reference<br>
+                    <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>H</kbd> Toggle Hub
+                </div>
+                <div class="hint-section">
+                    <strong>🏠 Internal Navigation:</strong><br>
+                    <kbd>Ctrl</kbd>+<kbd>1/2/3</kbd> Quick navigate pages<br>
+                    <kbd>Ctrl</kbd>+<kbd>B</kbd> Toggle sidebar<br>
+                    <kbd>Shift</kbd>+<kbd>?</kbd> Show this help
+                </div>
+                <div class="hint-section">
+                    <strong>✍️ Capture Page:</strong><br>
+                    <kbd>Esc</kbd> Normal mode | <kbd>Ctrl</kbd>+<kbd>I</kbd> Insert mode<br>
+                    <kbd>Ctrl</kbd>+<kbd>S</kbd> Save | <kbd>Ctrl</kbd>+<kbd>K</kbd> Clear<br>
+                    <kbd>Ctrl</kbd>+<kbd>W</kbd> Quick save + hide
+                </div>
+            </div>
+        </div>
+
+
+    <!-- Notification -->
+    <div class="notification" id="notification"></div>
+
+    <script>
+        // === IPC LISTENERS ===
+        if (window.electronAPI) {
+            // Écoute les commandes de navigation depuis main process
+            window.electronAPI.onNavigate((page) => {
+                navigateToPage(page);
+            });
+            
+            window.electronAPI.onToggleSidebar(() => {
+                toggleSidebar();
+            });
+            
+            // Listen for show shortcuts command
+            window.electronAPI.onShowShortcuts(() => {
+                console.log('📨 IPC received: show-shortcuts');
+                console.log('🔍 keyboardHint element:', document.getElementById('keyboardHint'));
+                showKeyboardHints();
+            });
+            
+            // NEW: Listen for quick save and hide
+            window.electronAPI.onQuickSaveAndHide(() => {
+                // Forward to active iframe (capture page)
+                const activeIframe = document.querySelector('.view-page.active iframe');
+                if (activeIframe && activeIframe.contentWindow) {
+                    activeIframe.contentWindow.postMessage({ type: 'quick-save-and-hide' }, '*');
+                }
+                
+                // Hide window after short delay
+                setTimeout(() => {
+                    if (window.electronAPI && window.electronAPI.hideWindow) {
+                        window.electronAPI.hideWindow();
+                    }
+                }, 300);
+            });
+        }
+
+        // === FOCUS MANAGEMENT SYSTEM ===
+        // Écoute les events clavier des iframes
+        window.addEventListener('message', (event) => {
+            if (event.data.type === 'show-shortcuts-test') {
+                console.log('🧪 app.html received: show-shortcuts-test');
+                console.log('🧪 Calling showKeyboardHints()');
+                showKeyboardHints();
+            }
+
+            if (event.data.type === 'keyboard-event') {
+                const keyEvent = event.data.event;
+                
+                // Ctrl+1/2/3 - Navigate pages (INTERNAL ONLY)
+                if (keyEvent.ctrlKey && ['1', '2', '3'].includes(keyEvent.key)) {
+                    const pages = ['capture', 'hub', 'reference'];
+                    const pageIndex = parseInt(keyEvent.key) - 1;
+                    if (pages[pageIndex]) {
+                        navigateToPage(pages[pageIndex]);
+                    }
+                }
+                
+                // Ctrl+B - Toggle sidebar (INTERNAL ONLY)
+                if (keyEvent.ctrlKey && keyEvent.key === 'b') {
+                    toggleSidebar();
+                }
+            }
+        });
+
+        // === STATE ===
+        let currentPage = 'capture';
+        let selectedNavIndex = 0;
+        const navItems = document.querySelectorAll('.nav-item');
+
+        // === INITIALIZE ===
+        document.addEventListener('DOMContentLoaded', () => {
+            updateNavSelection();
+        });
+
+        // === NAVIGATE TO PAGE ===
+        function navigateToPage(pageName) {
+            // Hide all pages
+            document.querySelectorAll('.view-page').forEach(page => {
+                page.classList.remove('active');
+            });
+
+            // Show target page
+            const targetPage = document.getElementById(`page-${pageName}`);
+            if (targetPage) {
+                targetPage.classList.add('active');
+                currentPage = pageName;
+
+                // Notify main process of page change (for smart toggle tracking)
+                if (window.electronAPI && window.electronAPI.notifyPageChange) {
+                    window.electronAPI.notifyPageChange(pageName);
+                }
+
+                // Update title
+                const titles = {
+                    'capture': 'Quick Capture',
+                    'hub': 'Hub',
+                    'reference': 'Quick Reference'
+                };
+                document.getElementById('pageTitle').textContent = titles[pageName] || pageName;
+
+                // Update nav active state
+                navItems.forEach(item => item.classList.remove('active'));
+                const activeNav = document.querySelector(`[data-page="${pageName}"]`);
+                if (activeNav) {
+                    activeNav.classList.add('active');
+                    selectedNavIndex = Array.from(navItems).indexOf(activeNav);
+                }
+            }
+        }
+
+        // === TOGGLE SIDEBAR ===
+        function toggleSidebar() {
+            document.getElementById('sidebar').classList.toggle('collapsed');
+        }
+
+        // === SHOW KEYBOARD HINTS ===
+        function showKeyboardHints() {
+            const hint = document.getElementById('keyboardHint');
+            hint.classList.add('show');
+            setTimeout(() => {
+                hint.classList.remove('show');
+            }, 5000);
+        }
+
+        // === SHOW NOTIFICATION ===
+        function showNotification(message, type = 'success') {
+            const notification = document.getElementById('notification');
+            notification.textContent = message;
+            notification.className = `notification ${type}`;
+            notification.classList.add('show');
+            setTimeout(() => {
+                notification.classList.remove('show');
+            }, 3000);
+        }
+
+        // === SETTINGS (placeholder) ===
+        function openSettings() {
+            showNotification('Settings coming soon!');
+        }
+
+        // === ARROW KEY NAVIGATION ===
+        function updateNavSelection() {
+            navItems.forEach((item, index) => {
+                if (index === selectedNavIndex) {
+                    item.style.outline = '2px solid #667eea';
+                    item.style.outlineOffset = '-2px';
+                } else {
+                    item.style.outline = 'none';
+                }
+            });
+        }
+
+        // === CLICK NAVIGATION ===
+        navItems.forEach(item => {
+            item.addEventListener('click', () => {
+                const page = item.getAttribute('data-page');
+                navigateToPage(page);
+            });
+        });
+
+        // === TEST RACCOURCIS VIERGES (Layer 2 internal) ===
+        document.addEventListener('keydown', (e) => {
+            // Ctrl+Shift+K - Test 1
+            if (e.ctrlKey && e.shiftKey && e.key === 'K') {
+                e.preventDefault();
+                console.log('🧪 TEST: Ctrl+Shift+K caught in app.html');
+                showKeyboardHints();
+            }
+            
+            // Ctrl+Shift+P - Test 2
+            if (e.ctrlKey && e.shiftKey && e.key === 'P') {
+                e.preventDefault();
+                console.log('🧪 TEST: Ctrl+Shift+P caught in app.html');
+                showKeyboardHints();
+            }
+            
+            // F12 - Test 3
+            if (e.key === 'F12') {
+                e.preventDefault();
+                console.log('🧪 TEST: F12 caught in app.html');
+                showKeyboardHints();
+            }
+        });
+
+
+        console.log('🥷 Ninja Mode Activated!');
+        console.log('Global: Ctrl+Shift+Space/F/H | Internal: Ctrl+1/2/3, Ctrl+B, Shift+?');
+    </script>
+
+
+</body>
+</html>
diff --git a/electron/src/renderer/capture.html b/electron/src/renderer/capture.html
index 41d0c13..b389d7a 100644
--- a/electron/src/renderer/capture.html
+++ b/electron/src/renderer/capture.html
@@ -3,7 +3,7 @@
 <head>
     <meta charset="UTF-8">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
-    <title>PKM Widget - Quick Capture</title>
+    <title>Quick Capture</title>
     <style>
         * {
             margin: 0;
@@ -14,143 +14,79 @@
         body {
             font-family: 'Monaco', 'Consolas', 'Courier New', monospace;
             background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
-            min-height: 100vh;
+            height: 100vh;
             display: flex;
-            align-items: center;
-            justify-content: center;
-            padding: 20px;
-        }
-
-        .widget-container {
-            background: rgba(20, 20, 30, 0.95);
-            border-radius: 16px;
-            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
-            border: 1px solid rgba(255, 255, 255, 0.1);
-            width: 800px;
-            max-width: 95vw;
-            backdrop-filter: blur(20px);
+            flex-direction: column;
             overflow: hidden;
         }
 
-        .widget-header {
-            background: rgba(255, 255, 255, 0.05);
-            padding: 16px 20px;
-            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
-            display: flex;
-            align-items: center;
-            justify-content: space-between;
-        }
-
-        .widget-title {
-            color: #fff;
-            font-size: 16px;
-            font-weight: 600;
-            display: flex;
-            align-items: center;
-            gap: 10px;
-        }
-
-        .status-indicator {
-            width: 8px;
-            height: 8px;
-            border-radius: 50%;
-            background: #27c93f;
-            animation: pulse 2s infinite;
-        }
-
-        @keyframes pulse {
-            0%, 100% { opacity: 1; }
-            50% { opacity: 0.5; }
-        }
-
-        .widget-controls {
-            display: flex;
-            gap: 8px;
-        }
-
-        .control-btn {
-            width: 12px;
-            height: 12px;
-            border-radius: 50%;
-            cursor: pointer;
-            transition: transform 0.2s;
-        }
-
-        .control-btn:hover {
-            transform: scale(1.2);
-        }
-
-        .control-btn.close { background: #ff5f56; }
-        .control-btn.minimize { background: #ffbd2e; }
-        .control-btn.maximize { background: #27c93f; }
-
-        .widget-toolbar {
-            padding: 12px 20px;
-            background: rgba(255, 255, 255, 0.03);
-            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
+        .container {
+            flex: 1;
             display: flex;
-            gap: 12px;
-            align-items: center;
-        }
-
-        .toolbar-btn {
-            background: rgba(255, 255, 255, 0.1);
-            border: 1px solid rgba(255, 255, 255, 0.15);
-            color: #fff;
-            padding: 6px 12px;
-            border-radius: 6px;
-            font-size: 12px;
-            cursor: pointer;
-            transition: all 0.2s;
-            font-family: inherit;
+            flex-direction: column;
+            padding: 20px;
+            max-width: 1400px;
+            margin: 0 auto;
+            width: 100%;
         }
 
-        .toolbar-btn:hover {
-            background: rgba(255, 255, 255, 0.15);
-            border-color: #667eea;
+        .header {
+            text-align: center;
+            color: white;
+            margin-bottom: 20px;
         }
 
-        .toolbar-btn.active {
-            background: rgba(102, 126, 234, 0.3);
-            border-color: #667eea;
+        .header h1 {
+            font-size: 2em;
+            font-weight: 600;
+            text-shadow: 0 2px 10px rgba(0,0,0,0.3);
         }
 
-        .widget-content {
+        .editor-container {
+            flex: 1;
             display: flex;
-            height: 500px;
+            gap: 20px;
+            background: rgba(20, 20, 30, 0.95);
+            border-radius: 16px;
+            padding: 20px;
+            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
+            border: 1px solid rgba(255, 255, 255, 0.1);
+            backdrop-filter: blur(20px);
+            overflow: hidden;
         }
 
-        .editor-pane, .preview-pane {
+        .editor-section, .preview-section {
             flex: 1;
             display: flex;
             flex-direction: column;
         }
 
-        .pane-header {
-            padding: 12px 20px;
-            background: rgba(255, 255, 255, 0.03);
-            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
-            color: rgba(255, 255, 255, 0.7);
-            font-size: 12px;
-            text-transform: uppercase;
-            letter-spacing: 1px;
-        }
-
-        .editor-pane {
-            border-right: 1px solid rgba(255, 255, 255, 0.1);
+        .section-title {
+            font-size: 1.2em;
+            font-weight: 600;
+            margin-bottom: 12px;
+            color: #a5b4fc;
         }
 
         #editor {
             flex: 1;
-            background: rgba(0, 0, 0, 0.2);
-            color: #fff;
-            border: none;
-            padding: 20px;
-            font-family: inherit;
-            font-size: 14px;
-            line-height: 1.6;
+            width: 100%;
+            padding: 16px;
+            border: 1px solid rgba(255, 255, 255, 0.1);
+            border-radius: 8px;
+            font-size: 16px;
+            font-family: 'Courier New', monospace;
             resize: none;
+            transition: all 0.3s;
+            background: rgba(255, 255, 255, 0.05);
+            color: #e2e8f0;
+        }
+
+        #editor:focus {
             outline: none;
+            border-color: #667eea;
+            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.2);
+            background: rgba(255, 255, 255, 0.08);
         }
 
         #editor::placeholder {
@@ -159,122 +95,69 @@
 
         #preview {
             flex: 1;
-            padding: 20px;
+            padding: 16px;
+            border: 1px solid rgba(255, 255, 255, 0.1);
+            border-radius: 8px;
             overflow-y: auto;
-            color: #eee;
-            font-size: 14px;
-            line-height: 1.6;
-        }
-
-        #preview h1 { font-size: 2em; margin: 0.67em 0; color: #fff; }
-        #preview h2 { font-size: 1.5em; margin: 0.75em 0; color: #fff; }
-        #preview h3 { font-size: 1.17em; margin: 0.83em 0; color: #fff; }
-        #preview p { margin: 1em 0; }
-        #preview code {
-            background: rgba(255, 255, 255, 0.1);
-            padding: 2px 6px;
-            border-radius: 3px;
-            font-family: inherit;
-        }
-        #preview pre {
-            background: rgba(0, 0, 0, 0.3);
-            padding: 12px;
-            border-radius: 6px;
-            overflow-x: auto;
-            margin: 1em 0;
-        }
-        #preview pre code {
-            background: none;
-            padding: 0;
-        }
-        #preview ul, #preview ol {
-            margin: 1em 0;
-            padding-left: 2em;
-        }
-        #preview blockquote {
-            border-left: 4px solid #667eea;
-            padding-left: 16px;
-            margin: 1em 0;
-            color: rgba(255, 255, 255, 0.8);
-        }
-        #preview a {
-            color: #667eea;
-            text-decoration: none;
-        }
-        #preview a:hover {
-            text-decoration: underline;
-        }
-
-        .widget-footer {
-            padding: 12px 20px;
             background: rgba(255, 255, 255, 0.03);
-            border-top: 1px solid rgba(255, 255, 255, 0.1);
-            display: flex;
-            justify-content: space-between;
-            align-items: center;
-        }
-
-        .footer-info {
-            display: flex;
-            gap: 20px;
-            color: rgba(255, 255, 255, 0.5);
-            font-size: 11px;
+            color: #e2e8f0;
         }
 
-        .footer-actions {
+        .controls {
             display: flex;
-            gap: 8px;
+            gap: 12px;
+            margin-top: 16px;
         }
 
-        .btn-primary {
-            background: #667eea;
-            color: #fff;
-            border: none;
-            padding: 8px 16px;
-            border-radius: 6px;
-            font-size: 13px;
+        button {
+            flex: 1;
+            padding: 12px 24px;
+            border: 1px solid rgba(255, 255, 255, 0.15);
+            border-radius: 8px;
+            font-size: 16px;
             font-weight: 600;
             cursor: pointer;
-            transition: all 0.2s;
+            transition: all 0.3s;
             font-family: inherit;
         }
 
+        .btn-primary {
+            background: rgba(102, 126, 234, 0.3);
+            color: white;
+            border-color: #667eea;
+        }
+
         .btn-primary:hover {
-            background: #5568d3;
-            transform: translateY(-1px);
+            background: rgba(102, 126, 234, 0.5);
+            transform: translateY(-2px);
             box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
         }
 
         .btn-secondary {
             background: rgba(255, 255, 255, 0.1);
-            color: #fff;
-            border: 1px solid rgba(255, 255, 255, 0.15);
-            padding: 8px 16px;
-            border-radius: 6px;
-            font-size: 13px;
-            cursor: pointer;
-            transition: all 0.2s;
-            font-family: inherit;
+            color: white;
         }
 
         .btn-secondary:hover {
             background: rgba(255, 255, 255, 0.15);
+            transform: translateY(-2px);
         }
 
         .notification {
             position: fixed;
             top: 20px;
             right: 20px;
-            background: rgba(39, 201, 63, 0.9);
-            color: #fff;
-            padding: 12px 20px;
+            padding: 16px 24px;
+            background: rgba(20, 20, 30, 0.95);
+            border: 1px solid rgba(255, 255, 255, 0.2);
             border-radius: 8px;
-            font-size: 13px;
+            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
+            backdrop-filter: blur(20px);
             opacity: 0;
             transform: translateY(-20px);
             transition: all 0.3s;
-            pointer-events: none;
             z-index: 1000;
+            color: white;
         }
 
         .notification.show {
@@ -282,367 +165,322 @@
             transform: translateY(0);
         }
 
-        ::-webkit-scrollbar {
-            width: 8px;
+        .notification.success {
+            border-left: 4px solid #27c93f;
         }
 
-        ::-webkit-scrollbar-track {
-            background: rgba(255, 255, 255, 0.03);
+        .notification.error {
+            border-left: 4px solid #f56565;
         }
 
-        ::-webkit-scrollbar-thumb {
-            background: rgba(255, 255, 255, 0.2);
-            border-radius: 4px;
+        .notification.info {
+            border-left: 4px solid #667eea;
         }
 
-        ::-webkit-scrollbar-thumb:hover {
-            background: rgba(255, 255, 255, 0.3);
+        /* Markdown Preview Styles */
+        #preview h1, #preview h2, #preview h3 {
+            margin-top: 16px;
+            margin-bottom: 8px;
+            color: #a5b4fc;
         }
 
-        .word-count {
-            color: rgba(255, 255, 255, 0.5);
-            font-size: 11px;
+        #preview p {
+            margin-bottom: 12px;
+            line-height: 1.6;
+            color: rgba(255, 255, 255, 0.8);
         }
 
-        .hidden {
-            display: none !important;
+        #preview code {
+            background: rgba(255, 255, 255, 0.1);
+            padding: 2px 6px;
+            border-radius: 4px;
+            font-family: 'Courier New', monospace;
+            color: #fbbf24;
         }
-    </style>
-</head>
-<body>
-    <div class="notification" id="notification">✓ Note saved!</div>
 
-    <div class="widget-container">
-        <div class="widget-header">
-            <div class="widget-title">
-                <span class="status-indicator"></span>
-                🧠 PKM Quick Capture
-            </div>
-            <div class="widget-controls">
-                <div class="control-btn close" onclick="hideWidget()"></div>
-                <div class="control-btn minimize"></div>
-                <div class="control-btn maximize" onclick="toggleFullscreen()"></div>
-            </div>
-        </div>
+        #preview ul, #preview ol {
+            margin-left: 24px;
+            margin-bottom: 12px;
+        }
 
-        <div class="widget-toolbar">
-            <button class="toolbar-btn active" onclick="toggleMode('split')" id="btn-split">Split View</button>
-            <button class="toolbar-btn" onclick="toggleMode('editor')" id="btn-editor">Editor Only</button>
-            <button class="toolbar-btn" onclick="toggleMode('preview')" id="btn-preview">Preview Only</button>
-            <div style="flex: 1"></div>
-            <button class="toolbar-btn" onclick="clearEditor()">Clear</button>
-        </div>
+        #preview li {
+            margin-bottom: 4px;
+            color: rgba(255, 255, 255, 0.8);
+        }
 
-        <div class="widget-content">
-            <div class="editor-pane" id="editor-pane">
-                <div class="pane-header">Markdown Editor</div>
-                <textarea id="editor" placeholder="# Start typing...
+        /* Scrollbar styling */
+        #preview::-webkit-scrollbar {
+            width: 8px;
+        }
 
-Write your thoughts here. Markdown is supported!
+        #preview::-webkit-scrollbar-track {
+            background: rgba(255, 255, 255, 0.05);
+            border-radius: 4px;
+        }
 
-**Bold text**, *italic*, `code`, and more..."></textarea>
+        #preview::-webkit-scrollbar-thumb {
+            background: rgba(102, 126, 234, 0.5);
+            border-radius: 4px;
+        }
+
+        #preview::-webkit-scrollbar-thumb:hover {
+            background: rgba(102, 126, 234, 0.7);
+        }
+    </style>
+</head>
+<body>
+    <div class="container">
+        <div class="header">
+            <h1>✍️ Quick Capture</h1>
+        </div>
+        
+        <div class="editor-container">
+            <div class="editor-section">
+                <div class="section-title">Editor</div>
+                <textarea id="editor" placeholder="Start typing your thoughts..."></textarea>
             </div>
-            <div class="preview-pane" id="preview-pane">
-                <div class="pane-header">Live Preview</div>
+            
+            <div class="preview-section">
+                <div class="section-title">Preview</div>
                 <div id="preview"></div>
             </div>
         </div>
 
-        <div class="widget-footer">
-            <div class="footer-info">
-                <span class="word-count" id="word-count">0 words</span>
-                <span>•</span>
-                <span id="last-saved">Not saved yet</span>
-                <span>•</span>
-                <span>Press Esc to hide</span>
-            </div>
-            <div class="footer-actions">
-                <button class="btn-secondary" onclick="downloadNote()">📥 Save Note</button>
-            </div>
+        <div class="controls">
+            <button class="btn-primary" onclick="saveNote()">💾 Save to Vault</button>
+            <button class="btn-secondary" onclick="clearEditor()">🗑️ Clear</button>
         </div>
+    </div>
+
+    <div class="notification" id="notification"></div>
 
     <script>
         const editor = document.getElementById('editor');
         const preview = document.getElementById('preview');
-        const wordCount = document.getElementById('word-count');
-        const lastSaved = document.getElementById('last-saved');
-        const notification = document.getElementById('notification');
-
-        let autosaveTimer;
-        let currentMode = 'split';
 
         // Simple markdown parser
         function parseMarkdown(text) {
             return text
-                // Headers
                 .replace(/^### (.*$)/gim, '<h3>$1</h3>')
                 .replace(/^## (.*$)/gim, '<h2>$1</h2>')
                 .replace(/^# (.*$)/gim, '<h1>$1</h1>')
-                // Bold
                 .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
-                // Italic
                 .replace(/\*(.+?)\*/g, '<em>$1</em>')
-                // Code inline
                 .replace(/`(.+?)`/g, '<code>$1</code>')
-                // Code blocks
-                .replace(/```([\s\S]*?)```/g, '<pre><code>$1</code></pre>')
-                // Links
-                .replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2">$1</a>')
-                // Line breaks
+                .replace(/^\- (.+)$/gim, '<li>$1</li>')
                 .replace(/\n\n/g, '</p><p>')
-                .replace(/\n/g, '<br>')
-                // Blockquotes
-                .replace(/^&gt; (.*$)/gim, '<blockquote>$1</blockquote>')
-                // Lists
-                .replace(/^\- (.*$)/gim, '<li>$1</li>')
-                // Wrap in paragraphs
-                .replace(/^(?!<[h|l|b|p])(.*$)/gim, '<p>$1</p>');
+                .replace(/^(.+)$/gim, '<p>$1</p>');
         }
 
-        // Update preview
         function updatePreview() {
-            const text = editor.value;
-            preview.innerHTML = parseMarkdown(text);
-            
-            // Update word count
-            const words = text.trim().split(/\s+/).filter(w => w.length > 0).length;
-            wordCount.textContent = `${words} word${words !== 1 ? 's' : ''}`;
+            const markdown = editor.value;
+            preview.innerHTML = parseMarkdown(markdown);
         }
 
-        // Editor input handler
-        editor.addEventListener('input', () => {
-            updatePreview();
-            
-            // Clear existing timer
-            clearTimeout(autosaveTimer);
-            
-            // Set new autosave timer (5 seconds)
-            autosaveTimer = setTimeout(() => {
-                autosave();
-            }, 5000);
-        });
-
-        // Autosave to localStorage
-        function autosave() {
-            const content = editor.value;
-            if (content.trim()) {
-                localStorage.setItem('pkm-autosave', content);
-                const now = new Date().toLocaleTimeString();
-                lastSaved.textContent = `Auto-saved at ${now}`;
-            }
-        }
-
-        // Vault directory handle (stored globally)
-        let vaultDirHandle = null;
-
-        // Initialize vault directory
-        async function initVault() {
-            try {
-                // Check if File System Access API is supported
-                if (!('showDirectoryPicker' in window)) {
-                    alert('File System Access API not supported. Please use Chrome/Edge or download notes manually.');
-                    return false;
-                }
+        editor.addEventListener('input', updatePreview);
 
-                // Ask user to select vault directory
-                vaultDirHandle = await window.showDirectoryPicker({
-                    mode: 'readwrite',
-                    startIn: 'documents'
-                });
+        // Auto-focus on load
+        setTimeout(() => {
+            editor.focus();
+        }, 100);
 
-                // Store handle reference (can't persist it directly due to security)
-                localStorage.setItem('pkm-vault-configured', 'true');
-                
-                showNotification('Vault configured! You can now save notes.');
-                return true;
-            } catch (err) {
-                if (err.name !== 'AbortError') {
-                    console.error('Error selecting vault:', err);
-                    alert('Error configuring vault. You can still download notes manually.');
-                }
-                return false;
-            }
+        function showNotification(message, type = 'success') {
+            const notification = document.getElementById('notification');
+            notification.textContent = message;
+            notification.className = `notification ${type}`;
+            notification.classList.add('show');
+            
+            setTimeout(() => {
+                notification.classList.remove('show');
+            }, 3000);
         }
 
-        // Save note (simplified download)
-        function saveNote() {
-            const content = editor.value;
-            if (!content.trim()) {
-                alert('Nothing to save!');
+        function clearEditor() {
+            if (editor.value.trim() && !confirm('Clear all content?')) {
                 return;
             }
-
-            const now = new Date();
-            const timestamp = now.toISOString().slice(0, 19).replace('T', '_').replace(/:/g, '-');
-            
-            // Extract title from first heading
-            const firstLine = content.split('\n')[0];
-            let title = 'note';
-            if (firstLine.startsWith('#')) {
-                title = firstLine.replace(/^#+\s*/, '').trim()
-                    .toLowerCase()
-                    .replace(/[^a-z0-9]+/g, '-')
-                    .substring(0, 50);
-            }
-            
-            const filename = `${timestamp}_${title}.md`;
-
-            // Download file
-            const blob = new Blob([content], { type: 'text/markdown' });
-            const url = URL.createObjectURL(blob);
-            const a = document.createElement('a');
-            a.href = url;
-            a.download = filename;
-            document.body.appendChild(a);
-            a.click();
-            document.body.removeChild(a);
-            URL.revokeObjectURL(url);
-
-            localStorage.removeItem('pkm-autosave');
-            showNotification(`✅ Note saved: ${filename}`);
-            lastSaved.textContent = `Saved at ${now.toLocaleTimeString()}`;
-
-            if (confirm('Note saved! Clear editor for new note?')) {
-                clearEditor();
-            }
+            editor.value = '';
+            updatePreview();
+            localStorage.removeItem('pkm-quick-note');
+            localStorage.removeItem('pkm-quick-note-timestamp');
+            showNotification('🗑️ Cleared', 'info');
         }
+		// === AUTO-SAVE TO CACHE ===
+        let saveTimeout;
+        editor.addEventListener('input', () => {
+            clearTimeout(saveTimeout);
+            saveTimeout = setTimeout(() => {
+                const content = editor.value;
+                if (content.trim()) {
+                    localStorage.setItem('pkm-quick-note', content);
+                    localStorage.setItem('pkm-quick-note-timestamp', Date.now());
+                    console.log('💾 Auto-saved to cache');
+                }
+            }, 2000);
+        });
 
-
-        // Add configure vault button functionality
-        async function configureVault() {
-            const configured = await initVault();
-            if (configured) {
-                alert('Vault configured successfully! Your notes will be saved to the selected folder.');
+        // === LOAD FROM CACHE ON STARTUP ===
+        let hasLoadedFromCache = false;
+        
+        function loadFromCache() {
+            if (!hasLoadedFromCache) {
+                const savedNote = localStorage.getItem('pkm-quick-note');
+                if (savedNote) {
+                    editor.value = savedNote;
+                    updatePreview();
+                    console.log('📂 Loaded from cache');
+                }
+                hasLoadedFromCache = true;
             }
         }
-
-        // Download note as file
-        function downloadNote() {
-            const content = editor.value;
-            if (!content.trim()) {
-                alert('Nothing to download!');
-                return;
-            }
-
-            const blob = new Blob([content], { type: 'text/markdown' });
-            const url = URL.createObjectURL(blob);
-            const a = document.createElement('a');
-            a.href = url;
-            a.download = `note-${new Date().toISOString().slice(0, 10)}.md`;
-            document.body.appendChild(a);
-            a.click();
-            document.body.removeChild(a);
-            URL.revokeObjectURL(url);
-
-            showNotification('Note downloaded!');
+        
+        if (document.readyState === 'loading') {
+            document.addEventListener('DOMContentLoaded', loadFromCache);
+        } else {
+            loadFromCache();
         }
 
-        // Clear editor
-        function clearEditor() {
-            if (editor.value.trim() && !confirm('Clear all content?')) {
+        // === CTRL+S - SAVE TO VAULT (CLEAR AFTER) ===
+        async function saveNote() {
+            const content = editor.value.trim();
+            
+            if (!content) {
+                showNotification('⚠️ Nothing to save', 'info');
                 return;
             }
-            editor.value = '';
-            updatePreview();
-            localStorage.removeItem('pkm-autosave');
-            lastSaved.textContent = 'Not saved yet';
-        }
-
-        // Toggle view mode
-        function toggleMode(mode) {
-            currentMode = mode;
-            const editorPane = document.getElementById('editor-pane');
-            const previewPane = document.getElementById('preview-pane');
-            const btnSplit = document.getElementById('btn-split');
-            const btnEditor = document.getElementById('btn-editor');
-            const btnPreview = document.getElementById('btn-preview');
-
-            // Remove active class from all
-            [btnSplit, btnEditor, btnPreview].forEach(btn => btn.classList.remove('active'));
-
-            if (mode === 'split') {
-                editorPane.classList.remove('hidden');
-                previewPane.classList.remove('hidden');
-                btnSplit.classList.add('active');
-            } else if (mode === 'editor') {
-                editorPane.classList.remove('hidden');
-                previewPane.classList.add('hidden');
-                btnEditor.classList.add('active');
-            } else if (mode === 'preview') {
-                editorPane.classList.add('hidden');
-                previewPane.classList.remove('hidden');
-                btnPreview.classList.add('active');
-            }
-        }
 
-        // Show notification
-        function showNotification(message) {
-            notification.textContent = message;
-            notification.classList.add('show');
-            setTimeout(() => {
-                notification.classList.remove('show');
-            }, 2000);
-        }
+            const now = new Date();
+            const timestamp = now.toISOString().replace(/[:.]/g, '-').slice(0, -5);
+            const filename = `quick-capture-${timestamp}.md`;
 
-        // Hide widget
-        function hideWidget() {
-            if (confirm('Hide widget? (Progress will be saved)')) {
-                autosave();
-                document.querySelector('.widget-container').style.opacity = '0';
-                setTimeout(() => {
-                    alert('Widget hidden! (In real app, this would minimize to tray)');
-                    document.querySelector('.widget-container').style.opacity = '1';
-                }, 300);
+            try {
+                const result = await window.electronAPI.saveNote(filename, content);
+                
+                if (result.success) {
+                    showNotification('✅ Saved + Ready for new note');
+                    
+                    // CLEAR editor after successful save
+                    editor.value = '';
+                    updatePreview();
+                    
+                    // CLEAR localStorage
+                    localStorage.removeItem('pkm-quick-note');
+                    localStorage.removeItem('pkm-quick-note-timestamp');
+                    
+                    console.log('🗑️ Cleared after save to vault');
+                } else {
+                    showNotification('❌ Save failed', 'error');
+                }
+            } catch (error) {
+                console.error('Save error:', error);
+                showNotification('❌ Save error', 'error');
             }
         }
 
-        // Toggle fullscreen
-        function toggleFullscreen() {
-            if (!document.fullscreenElement) {
-                document.documentElement.requestFullscreen();
+        // === QUICK SAVE TO CACHE (KEEP CONTENT) ===
+        function quickSaveToCache() {
+            const content = editor.value.trim();
+            if (content) {
+                localStorage.setItem('pkm-quick-note', content);
+                localStorage.setItem('pkm-quick-note-timestamp', Date.now());
+                showNotification('💾 Saved to cache', 'info');
+                console.log('💾 Quick saved to cache');
             } else {
-                document.exitFullscreen();
+                showNotification('📦 Window hidden', 'info');
             }
         }
 
-        // Keyboard shortcuts
+        // Listen for quick save command from parent (Ctrl+W)
+        window.addEventListener('message', (event) => {
+            if (event.data.type === 'quick-save-and-hide') {
+                quickSaveToCache();
+            }
+        });
+		
+		// === VIM-LIKE MODES ===
+        let insertMode = true;
+        
         document.addEventListener('keydown', (e) => {
-            // Esc to hide
+            // === ESC - Sort du mode édition ===
             if (e.key === 'Escape') {
-                hideWidget();
+                e.preventDefault();
+                
+                if (document.activeElement === editor) {
+                    editor.blur();
+                    insertMode = false;
+                    showNotification('Mode normal activé', 'info');
+                }
+            }
+            
+            // === CTRL+I - Entre en mode édition ===
+            if (e.ctrlKey && e.key === 'i' && !insertMode) {
+                e.preventDefault();
+                editor.focus();
+                insertMode = true;
+                showNotification('Mode insertion activé', 'info');
             }
             
-            // Ctrl/Cmd + S to save
+            // === CTRL+S - Save ===
             if ((e.ctrlKey || e.metaKey) && e.key === 's') {
                 e.preventDefault();
                 saveNote();
             }
-
-            // Ctrl/Cmd + K to clear
+            
+            // === CTRL+K - Clear ===
             if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
                 e.preventDefault();
                 clearEditor();
             }
-        });
+            
+            // === TEST RACCOURCIS LOCAUX ===
+            // Ctrl+Shift+K - Test 1
+            if (e.ctrlKey && e.shiftKey && e.key === 'K') {
+                e.preventDefault();
+                console.log('🧪 Ctrl+Shift+K - Relaying to parent');
+                
+                window.parent.postMessage({
+                    type: 'show-shortcuts-test',
+                    event: {key: e.key,ctrlKey: e.ctrlKey,shiftKey: e.shiftKey}
+                }, '*');
+            }
+            
+            // === CTRL+S - Save ===
+            if ((e.ctrlKey || e.metaKey) && e.key === 's') {
+                e.preventDefault();
+                saveNote();
+            }
 
-        // Load autosaved content on startup
-        window.addEventListener('load', () => {
-            const autosaved = localStorage.getItem('pkm-autosave');
-            if (autosaved) {
-                editor.value = autosaved;
-                updatePreview();
-                lastSaved.textContent = 'Restored from autosave';
+            // === RELAY TO PARENT ===
+            if (
+                (e.ctrlKey && ['1', '2', '3', 'b', 'B'].includes(e.key)) {
+                e.preventDefault();
+                
+                window.parent.postMessage({
+                    type: 'keyboard-event',
+                    event: {
+                        key: e.key,
+                        code: e.code,
+                        ctrlKey: e.ctrlKey,
+                        shiftKey: e.shiftKey,
+                        altKey: e.altKey,
+                        metaKey: e.metaKey
+                    }
+                }, '*');
             }
-        });
 
-        // Initial preview update
-        updatePreview();
+        });
+        
+        // Sync insertMode avec le focus du textarea
+        editor.addEventListener('focus', () => {
+            insertMode = true;
+        });
+        
+        editor.addEventListener('blur', () => {
+            insertMode = false;
+        });
 
-        console.log('🧠 PKM Widget loaded!');
-        console.log('Shortcuts:');
-        console.log('  - Esc: Hide widget');
-        console.log('  - Ctrl+S: Save note');
-        console.log('  - Ctrl+K: Clear editor');
+        console.log('✅ Quick Capture loaded - Dark theme');
+        console.log('✅ Keyboard relay active');
     </script>
 </body>
 </html>
diff --git a/electron/src/renderer/hub.html b/electron/src/renderer/hub.html
index ccac962..6e20fdf 100644
--- a/electron/src/renderer/hub.html
+++ b/electron/src/renderer/hub.html
@@ -329,7 +329,7 @@
     </div>
 
     <div class="current-widget" id="referenceView">
-        <iframe src="quick-reference.html" class="widget-frame" id="referenceFrame"></iframe>
+        <iframe src="reference.html" class="widget-frame" id="referenceFrame"></iframe>
     </div>
 
     <script>
@@ -415,6 +415,27 @@
         console.log('  - Ctrl+Shift+Space: Toggle Quick Capture');
         console.log('  - Ctrl+Shift+F: Toggle Quick Reference');
         console.log('  - Esc: Return to hub');
+        // === RELAY KEYBOARD EVENTS TO PARENT ===
+        document.addEventListener('keydown', (e) => {
+            // Relay Ctrl+1/2/3, Ctrl+B, Ctrl+Arrows to parent
+            if (e.ctrlKey && ['1', '2', '3', 'b', 'B', 'ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight'].includes(e.key)) {
+                e.preventDefault(); // Empêche le comportement par défaut
+                
+                window.parent.postMessage({
+                    type: 'keyboard-event',
+                    event: {
+                        key: e.key.toLowerCase(), // Normalise en minuscule
+                        code: e.code,
+                        ctrlKey: e.ctrlKey,
+                        shiftKey: e.shiftKey,
+                        altKey: e.altKey,
+                        metaKey: e.metaKey
+                    }
+                }, '*');
+            }
+        });
+        
+        console.log('✅ Keyboard relay active');
     </script>
 </body>
 </html>
diff --git a/electron/src/renderer/reference.html b/electron/src/renderer/reference.html
index 32c8a2b..9a065ea 100644
--- a/electron/src/renderer/reference.html
+++ b/electron/src/renderer/reference.html
@@ -994,6 +994,28 @@
         renderCheatsheets();
 
         console.log('⚡ PKM Quick Reference V4 loaded!');
+        // === RELAY KEYBOARD EVENTS TO PARENT ===
+        document.addEventListener('keydown', (e) => {
+            // Relay Ctrl+1/2/3, Ctrl+B, Ctrl+Arrows to parent
+            if (e.ctrlKey && ['1', '2', '3', 'b', 'B', 'ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight'].includes(e.key)) {
+                e.preventDefault(); // Empêche le comportement par défaut
+                
+                window.parent.postMessage({
+                    type: 'keyboard-event',
+                    event: {
+                        key: e.key.toLowerCase(), // Normalise en minuscule
+                        code: e.code,
+                        ctrlKey: e.ctrlKey,
+                        shiftKey: e.shiftKey,
+                        altKey: e.altKey,
+                        metaKey: e.metaKey
+                    }
+                }, '*');
+            }
+        });
+        
+        console.log('✅ Keyboard relay active');
+
     </script>
 </body>
 </html>
diff --git a/widget/assets/icons/.gitkeep b/widgetOLDBACKUP/assets/icons/.gitkeep
similarity index 100%
rename from widget/assets/icons/.gitkeep
rename to widgetOLDBACKUP/assets/icons/.gitkeep
diff --git a/widget/package.json b/widgetOLDBACKUP/package.json
similarity index 100%
rename from widget/package.json
rename to widgetOLDBACKUP/package.json
diff --git a/widget/src/.gitkeep b/widgetOLDBACKUP/src/.gitkeep
similarity index 100%
rename from widget/src/.gitkeep
rename to widgetOLDBACKUP/src/.gitkeep
diff --git a/widget/src/app.js b/widgetOLDBACKUP/src/app.js
similarity index 100%
rename from widget/src/app.js
rename to widgetOLDBACKUP/src/app.js
diff --git a/widget/src/hub.html b/widgetOLDBACKUP/src/hub.html
similarity index 100%
rename from widget/src/hub.html
rename to widgetOLDBACKUP/src/hub.html
diff --git a/widget/src/index.html b/widgetOLDBACKUP/src/index.html
similarity index 100%
rename from widget/src/index.html
rename to widgetOLDBACKUP/src/index.html
diff --git a/widget/src/quick-reference.html b/widgetOLDBACKUP/src/quick-reference.html
similarity index 100%
rename from widget/src/quick-reference.html
rename to widgetOLDBACKUP/src/quick-reference.html
diff --git a/widget/src/styles.css b/widgetOLDBACKUP/src/styles.css
similarity index 100%
rename from widget/src/styles.css
rename to widgetOLDBACKUP/src/styles.css
diff --git a/widget/src/v3 b/widgetOLDBACKUP/src/v3
similarity index 100%
rename from widget/src/v3
rename to widgetOLDBACKUP/src/v3
