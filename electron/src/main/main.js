const { cconst { app, BrowserWindow, globalShortcut, ipcMain, Menu, Tray } = require('electron');
const path = require('path');

let mainWindow = null;
let captureWindow = null;
let referenceWindow = null;
let tray = null;

// Create main hub window
function createMainWindow() {
    mainWindow = new BrowserWindow({
        width: 600,
        height: 700,
        webPreferences: {
            nodeIntegration: false,
            contextIsolation: true,
            preload: path.join(__dirname, '../preload/preload.js')
        },
        frame: true,
        icon: path.join(__dirname, '../../build/icon.png')
    });

    mainWindow.loadFile(path.join(__dirname, '../renderer/hub.html'));

    // Open DevTools in development
    if (process.env.NODE_ENV === 'development') {
        mainWindow.webContents.openDevTools();
    }

    mainWindow.on('closed', () => {
        mainWindow = null;
    });
}

// Create Quick Capture window
function createCaptureWindow() {
    if (captureWindow) {
        captureWindow.focus();
        return;
    }

    captureWindow = new BrowserWindow({
        width: 900,
        height: 700,
        webPreferences: {
            nodeIntegration: false,
            contextIsolation: true,
            preload: path.join(__dirname, '../preload/preload.js')
        },
        frame: true,
        icon: path.join(__dirname, '../../build/icon.png')
    });

    captureWindow.loadFile(path.join(__dirname, '../renderer/capture.html'));

    captureWindow.on('closed', () => {
        captureWindow = null;
    });
}

// Create Quick Reference window
function createReferenceWindow() {
    if (referenceWindow) {
        referenceWindow.focus();
        return;
    }

    referenceWindow = new BrowserWindow({
        width: 700,
        height: 800,
        webPreferences: {
            nodeIntegration: false,
            contextIsolation: true,
            preload: path.join(__dirname, '../preload/preload.js')
        },
        frame: true,
        icon: path.join(__dirname, '../../build/icon.png')
    });

    referenceWindow.loadFile(path.join(__dirname, '../renderer/reference.html'));

    referenceWindow.on('closed', () => {
        referenceWindow = null;
    });
}

// Create system tray
function createTray() {
    tray = new Tray(path.join(__dirname, '../../build/icon.png'));
    
    const contextMenu = Menu.buildFromTemplate([
        {
            label: '🧠 PKM System',
            type: 'normal',
            enabled: false
        },
        { type: 'separator' },
        {
            label: '🏠 Hub',
            click: () => {
                if (mainWindow) {
                    mainWindow.show();
                    mainWindow.focus();
                } else {
                    createMainWindow();
                }
            }
        },
        {
            label: '✍️ Quick Capture',
            accelerator: 'CmdOrCtrl+Shift+Space',
            click: createCaptureWindow
        },
        {
            label: '⚡ Quick Reference',
            accelerator: 'CmdOrCtrl+Shift+F',
            click: createReferenceWindow
        },
        { type: 'separator' },
        {
            label: 'Quit',
            click: () => {
                app.quit();
            }
        }
    ]);

    tray.setToolTip('PKM System');
    tray.setContextMenu(contextMenu);

    // Click on tray icon shows main window
    tray.on('click', () => {
        if (mainWindow) {
            mainWindow.isVisible() ? mainWindow.hide() : mainWindow.show();
        } else {
            createMainWindow();
        }
    });
}

// Register global shortcuts
function registerShortcuts() {
    // Ctrl+Shift+Space - Quick Capture
    const captureShortcut = globalShortcut.register('CommandOrControl+Shift+Space', () => {
        if (captureWindow) {
            if (captureWindow.isVisible()) {
                captureWindow.hide();
            } else {
                captureWindow.show();
                captureWindow.focus();
            }
        } else {
            createCaptureWindow();
        }
    });

    if (!captureShortcut) {
        console.log('Failed to register Quick Capture shortcut');
    }

    // Ctrl+Shift+F - Quick Reference
    const refShortcut = globalShortcut.register('CommandOrControl+Shift+F', () => {
        if (referenceWindow) {
            if (referenceWindow.isVisible()) {
                referenceWindow.hide();
            } else {
                referenceWindow.show();
                referenceWindow.focus();
            }
        } else {
            createReferenceWindow();
        }
    });

    if (!refShortcut) {
        console.log('Failed to register Quick Reference shortcut');
    }

    console.log('✅ Global shortcuts registered!');
    console.log('   Ctrl+Shift+Space - Quick Capture');
    console.log('   Ctrl+Shift+F - Quick Reference');
}

// IPC handlers for file operations
ipcMain.handle('save-note', async (event, { filename, content }) => {
    const fs = require('fs').promises;
    const { dialog } = require('electron');
    
    try {
        // Ask user for vault location (first time)
        const result = await dialog.showOpenDialog({
            properties: ['openDirectory'],
            title: 'Select Vault Directory',
            buttonLabel: 'Select Vault'
        });

        if (result.canceled) {
            return { success: false, error: 'Cancelled' };
        }

        const vaultPath = result.filePaths[0];
        const inboxPath = path.join(vaultPath, '00_Inbox');
        
        // Create 00_Inbox if doesn't exist
        try {
            await fs.access(inboxPath);
        } catch {
            await fs.mkdir(inboxPath, { recursive: true });
        }

        const filePath = path.join(inboxPath, filename);
        await fs.writeFile(filePath, content, 'utf8');

        return { success: true, path: filePath };
    } catch (error) {
        console.error('Error saving note:', error);
        return { success: false, error: error.message };
    }
});

// App lifecycle
app.whenReady().then(() => {
    createMainWindow();
    createTray();
    registerShortcuts();

    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) {
            createMainWindow();
        }
    });
});

app.on('window-all-closed', () => {
    // Keep app running in tray on macOS
    if (process.platform !== 'darwin') {
        // On Windows/Linux, keep running in background
        // User must quit via tray menu
    }
});

app.on('will-quit', () => {
    // Unregister all shortcuts
    globalShortcut.unregisterAll();
});

// Log app info
console.log('🧠 PKM System Starting...');
console.log(`   Electron: ${process.versions.electron}`);
console.log(`   Chrome: ${process.versions.chrome}`);
console.log(`   Node: ${process.versions.node}`);
console.log(`   Platform: ${process.platform}`);ontextBridge, ipcRenderer } = require('electron');
