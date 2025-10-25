const { contextBridge, ipcRenderer } = require('electron');

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
    onShowShortcuts: (callback) => ipcRenderer.on('show-shortcuts', callback),
    
    // NEW: Notify main process of page changes
    notifyPageChange: (page) => ipcRenderer.send('current-page-changed', page),
    
    // NEW: Hide window
    hideWindow: () => ipcRenderer.send('hide-window')
    // Quick save and hide listener
    onQuickSaveAndHide: (callback) => ipcRenderer.on('quick-save-and-hide', callback),
});

console.log('✅ Preload script loaded');
console.log(`   Platform: ${process.platform}`);

