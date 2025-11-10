---
type: chat-card
parent_export: '[[Export]]'
order: 669
role: assistant
created: '2025-11-10T21:46:14.925504Z'
tags:
- chat-card
- python
- obsidian
- receipts
- code
- automation
attachments_count: 0
---

# 🤖 Message 669 - Assistant

**ID:** msg-669

## 💬 Content


**ID:** msg-669

markdown---
created: 2025-10-24T15:45:00
updated: 2025-11-01T19:50:00
type: concept
tags: [concept, variable, pkm-system, state-management, tracking]
tech_stack: [javascript]
status: partial
implemented_in: main.js
related:
 - \"[[smartToggle Function]]\"
 - \"[[IPC Communication]]\"
 - \"[[Global Shortcuts System]]\"
 - \"[[Architecture PKM System]]\"
source: \"développement pkm-system phase 1.5\"
---

# 📍 currentPage Variable

> **Variable d'état globale** - Tracking de la page actuellement active

## Description

`currentPage` est une variable globale dans le Main process qui garde en mémoire quelle page de l'application est actuellement affichée. Elle est essentielle au fonctionnement de [[smartToggle Function]] pour implémenter la logique de toggle intelligent.

## Rôle dans l'Architecture

**Position:** Main Process (variable globale)
**Type:** `string`
**Valeurs possibles:** `'capture'`, `'hub'`, `'reference'`
**Scope:** Globale au main.js
```
┌─────────────────────────────┐
│      Main Process           │
│                             │
│  let currentPage = 'hub';   │ ← Variable d'état
│                             │
│  smartToggle() lit/écrit    │
│  cette variable             │
└─────────────────────────────┘
```

## Implémentation

**Fichier:** `main.js`
**Chemin:** `C:\\Users\\idsmf\\Projects\\pkm-system\\electron\\src\\main\\main.js`
**Ligne approximative:** ~10

### Déclaration
```javascript
// Variables globales
let mainWindow = null;
let tray = null;
let currentPage = 'capture';  // Page par défaut au démarrage
```

### Utilisation dans smartToggle
```javascript
function smartToggle(targetPage) {
    if (!mainWindow) {
        createMainWindow();
        setTimeout(() => {
            mainWindow.webContents.send('navigate-to', targetPage);
            currentPage = targetPage;  // ← UPDATE
        }, 500);
    } else if (!mainWindow.isVisible()) {
        mainWindow.show();
        mainWindow.webContents.send('navigate-to', targetPage);
        currentPage = targetPage;  // ← UPDATE
    } else if (currentPage === targetPage) {  // ← READ
        // Toggle off - déjà sur cette page
        mainWindow.hide();
    } else {
        mainWindow.webContents.send('navigate-to', targetPage);
        currentPage = targetPage;  // ← UPDATE
    }
}
```

## États et Transitions

### État Initial
```javascript
currentPage = 'capture'  // Défaut au lancement
```

### Transitions
```
User lance app
    ↓
currentPage = 'capture'  (défaut)
    ↓
User presse Ctrl+Shift+H
    ↓
smartToggle('hub') appelé
    ↓
Navigation vers hub
    ↓
currentPage = 'hub'  ✅
    ↓
User presse Ctrl+Shift+H (même raccourci)
    ↓
smartToggle('hub') vérifie: currentPage === 'hub' ?
    ↓
OUI → Hide window (toggle off)
currentPage reste 'hub'
```

## Synchronisation avec Renderer

### Problème Actuel

⚠️ **La synchronisation est unidirectionnelle et peut désynchroniser**

**Scénario problématique:**
```
1. Main: currentPage = 'capture'
2. User clique dans UI pour aller à 'hub'
3. Renderer: page affichée = 'hub'
4. Main: currentPage = 'capture' ❌ (pas mis à jour!)
5. User presse Ctrl+Shift+H
6. smartToggle('hub') voit: currentPage !== 'hub'
7. Navigate vers hub (inutile, déjà dessus)
```

### Solution: IPC Bidirectionnel

**Architecture visée:**
```
┌─────────────────────────────────────┐
│         MAIN PROCESS                │
│                                     │
│  currentPage = 'capture'            │
│         ↓                           │
│  smartToggle('hub')                 │
│         ↓                           │
│  send('navigate-to', 'hub')         │
│         ↓                           │
│  currentPage = 'hub'  ✅            │
└──────────────┬──────────────────────┘
               │
               ↓ IPC: 'navigate-to'
┌─────────────────────────────────────┐
│       RENDERER PROCESS              │
│                                     │
│  Reçoit 'navigate-to' event         │
│         ↓                           │
│  navigateToPage('hub')              │
│         ↓                           │
│  Update DOM                         │
│         ↓                           │
│  send('current-page-changed', 'hub')│ ← Notification
└──────────────┬──────────────────────┘
               │
               ↓ IPC: 'current-page-changed'
┌─────────────────────────────────────┐
│         MAIN PROCESS                │
│                                     │
│  ipcMain.on('current-page-changed') │
│         ↓                           │
│  currentPage = 'hub'  ✅            │
└─────────────────────────────────────┘
```

### Implémentation Correcte

**Dans main.js:**
```javascript
// Handler pour synchronisation
ipcMain.on('current-page-changed', (event, page) => {
    console.log(`Page changed to: ${page}`);
    currentPage = page;
});
```

**Dans app.html (renderer):**
```javascript
function navigateToPage(page) {
    // Update UI
    document.querySelectorAll('.page').forEach(p => {
        p.classList.remove('active');
    });
    document.getElementById(`${page}-page`).classList.add('active');

    // Notifier le main process
    if (window.electronAPI) {
        window.electronAPI.sendCurrentPage(page);  // ← Sync back
    }
}
```

**Dans preload.js:**
```javascript
contextBridge.exposeInMainWorld('electronAPI', {
    sendCurrentPage: (page) => {
        ipcRenderer.send('current-page-changed', page);
    }
});
```

## Cas d'Usage

### Use Case 1: Toggle Simple
```javascript
// État initial
currentPage = 'capture'

// User presse Ctrl+Shift+Space
smartToggle('capture')

// Check: currentPage === 'capture' ? OUI
// Action: Hide window (toggle off)
// Result: currentPage reste 'capture'
```

### Use Case 2: Navigation
```javascript
// État initial
currentPage = 'capture'

// User presse Ctrl+Shift+H
smartToggle('hub')

// Check: currentPage === 'hub' ? NON
// Action: Navigate to hub
// Result: currentPage = 'hub'
```

### Use Case 3: Rappel App
```javascript
// État initial
currentPage = 'hub'
mainWindow.isVisible() = false  // App cachée

// User presse Ctrl+Shift+F
smartToggle('reference')

// Check: Window cachée
// Action: Show window + navigate to reference
// Result: currentPage = 'reference'
```

### Use Case 4: Premier Lancement
```javascript
// État initial
mainWindow = null
currentPage = 'capture'  // Défaut

// User presse Ctrl+Shift+H
smartToggle('hub')

// Check: mainWindow === null ? OUI
// Action: Create window + navigate to hub
// Result: currentPage = 'hub'
```

## Problèmes et Limitations

### Problème 1: Désynchronisation

**Cause:**
- User peut naviguer dans l'UI (clics internes)
- `currentPage` dans Main n'est pas mis à jour
- Toggle intelligent ne fonctionne plus correctement

**Solution:**
- IPC bidirectionnel (implémenté dans [[IPC Communication]])
- Event `'current-page-changed'` du Renderer vers Main

### Problème 2: Persistance

**Actuellement:**
- La valeur est perdue au redémarrage de l'app
- Toujours initialisée à `'capture'`

**Amélioration possible:**
```javascript
// Sauvegarder dans localStorage ou config file
const Store = require('electron-store');
const store = new Store();

// Au démarrage
let currentPage = store.get('lastPage', 'capture');

// À chaque changement
function updateCurrentPage(page) {
    currentPage = page;
    store.set('lastPage', page);
}
```

### Problème 3: Validation

**Actuellement:**
- Pas de validation des valeurs
- Peut être assignée à n'importe quoi

**Amélioration possible:**
```javascript
const VALID_PAGES = ['capture', 'hub', 'reference'];

function setCurrentPage(page) {
    if (!VALID_PAGES.includes(page)) {
        console.error(`Invalid page: ${page}`);
        return false;
    }
    currentPage = page;
    return true;
}
```

## State Machine Potentiel

### Version Actuelle (Simple)
```
currentPage = string  // 'capture', 'hub', 'reference'
```

### Version Améliorée (Objet State)
```javascript
const appState = {
    currentPage: 'capture',
    previousPage: null,
    history: [],
    windowVisible: true,

    // Méthodes
    navigateTo(page) {
        this.previousPage = this.currentPage;
        this.currentPage = page;
        this.history.push(page);
    },

    goBack() {
        if (this.previousPage) {
            this.navigateTo(this.previousPage);
        }
    },

    getState() {
        return {
            current: this.currentPage,
            previous: this.previousPage,
            history: [...this.history]
        };
    }
};
```

**Avantages:**
- Historique de navigation
- Possibilité de \"back\"
- State plus riche
- Debugging plus facile

## Debug et Monitoring

### Logging Recommandé
```javascript
function updateCurrentPage(page) {
    const previous = currentPage;
    currentPage = page;
    console.log(`[State] Page changed: ${previous} → ${currentPage}`);

    // Optional: emit event pour monitoring
    mainWindow.webContents.send('state-changed', {
        previous,
        current: currentPage,
        timestamp: Date.now()
    });
}
```

### DevTools Inspection
```javascript
// Exposer pour debug (seulement en dev)
if (process.env.NODE_ENV === 'development') {
    ipcMain.handle('get-current-page', () => {
        return currentPage;
    });
}

// Dans renderer (dev tools console)
await window.electronAPI.getCurrentPage();
```

## Features Utilisant currentPage
```dataview
TABLE shortcut as \"Raccourci\", status as \"Status\", priority as \"Priorité\"
FROM \"02_Projects/PKM-SYSTEM\"
WHERE contains(dependencies, \"currentPage\")
SORT priority DESC
```

### Liste Manuelle
- [[smartToggle Function]] - Lit et écrit currentPage
- [[Ctrl+Shift+Space - Toggle Capture]] - Via smartToggle
- [[Ctrl+Shift+F - Toggle Reference]] - Via smartToggle
- [[Ctrl+Shift+H - Toggle Hub]] - Via smartToggle

## Diagramme d'État
```
┌─────────────────────────────────────────────┐
│             State Diagram                   │
│                                             │
│    ┌─────────┐   Ctrl+Shift+H  ┌─────────┐│
│    │         │─────────────────→│         ││
│    │ CAPTURE │                  │   HUB   ││
│    │         │←─────────────────│         ││
│    └────┬────┘   Ctrl+Shift+Space└────┬────┘│
│         │                              │    │
│         │ Ctrl+Shift+F                 │    │
│         │                              │    │
│         ↓                              ↓    │
│    ┌─────────┐   Ctrl+Shift+H  ┌─────────┐│
│    │         │←─────────────────│         ││
│    │REFERENCE│                  │   HUB   ││
│    │         │─────────────────→│         ││
│    └─────────┘   Ctrl+Shift+F  └─────────┘│
│                                             │
│  Note: Appuyer 2x sur même raccourci       │
│        = Hide window (pas de changement    │
│        de currentPage)                     │
└─────────────────────────────────────────────┘
```

## Tests de Validation

### Test 1: Lecture
```javascript
// Vérifier valeur initiale
console.log(currentPage);
// Expected: 'capture'
```

### Test 2: Écriture via smartToggle
```javascript
smartToggle('hub');
console.log(currentPage);
// Expected: 'hub'
```

### Test 3: Toggle off (pas de changement)
```javascript
currentPage = 'capture';
smartToggle('capture');  // Hide window
console.log(currentPage);
// Expected: 'capture' (inchangé)
```

### Test 4: Synchronisation IPC
```javascript
// Dans renderer: naviguer vers hub
navigateToPage('hub');
// Dans main: vérifier après event IPC
setTimeout(() => {
    console.log(currentPage);
    // Expected: 'hub'
}, 100);
```

## Ressources Liées

### Concepts
- [[smartToggle Function]] - Fonction principale utilisant currentPage
- [[IPC Communication]] - Synchronisation avec renderer
- [[Architecture PKM System]] - Context global

### Code
- [[main.js]] - Déclaration et utilisation
- [[app.html]] - Envoi notifications changement
- [[preload.js]] - Bridge pour notifications

### Features
- [[Global Shortcuts System]] - Tous les shortcuts utilisent cette variable
- [[MOC Raccourcis]] - Index complet

### Documentation
- [[Phase 1.5 - Refactor]] - Context développement
- [[Backlog]] - Améliorations futures

---

## 💡 Améliorations Futures

### V2: Objet State Complet
```javascript
class AppState {
    constructor() {
        this.currentPage = 'capture';
        this.previousPage = null;
        this.history = [];
        this.listeners = [];
    }

    navigateTo(page) {
        this.previousPage = this.currentPage;
        this.currentPage = page;
        this.history.push({page, timestamp: Date.now()});
        this.notify();
    }

    subscribe(listener) {
        this.listeners.push(listener);
    }

    notify() {
        this.listeners.forEach(fn => fn(this.getState()));
    }
}
```

### V3: Persistance
```javascript
// Sauvegarder state entre sessions
const state = new AppState();
state.subscribe(state => {
    store.set('appState', state);
});
```

### V4: Time Travel Debug
```javascript
// Rejouer historique de navigation
state.replayHistory();
```

---

**Dernière mise à jour:** 2025-11-01T19:50:00
**Status:** 🟡 PARTIAL - Fonctionne mais désynchronisation possible
**Prochaine action:** Implémenter sync IPC bidirectionnel complet

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-668-R668-NOTE-CONCEPTUELLE-currentPage-Variable-F]]
- ⬇️ Next: [[Card-670-R670-MFon-passe-cette-note-tags]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #python
- #obsidian
- #receipts
- #code
- #automation
