const { app, BrowserWindow, globalShortcut, ipcMain, Menu, Tray } = require('electron');
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

    // Ctrl+W - Quick save + hide window (GLOBAL)
    globalShortcut.register('CommandOrControl+W', () => {
        if (mainWindow && mainWindow.isVisible()) {
            // Send signal to save before hiding
            mainWindow.webContents.send('quick-save-and-hide');
        }
    });

    // === TEST SHORTCUTS HELP (3 raccourcis pour debug) ===
    
    // F1 - Show keyboard shortcuts
    globalShortcut.register('F1', () => {
        console.log('🔑 F1 pressed!');
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

    // Ctrl+/ - Show keyboard shortcuts
    globalShortcut.register('CommandOrControl+/', () => {
        console.log('🔑 Ctrl+/ pressed!');
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

    // Ctrl+Shift+L - Show keyboard shortcuts (test)
    globalShortcut.register('CommandOrControl+Shift+L', () => {
        console.log('🔑 Ctrl+Shift+L pressed!');
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
