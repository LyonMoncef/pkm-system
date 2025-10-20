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
    }
});

console.log('✅ Preload script loaded');
console.log(`   Platform: ${process.platform}`);
