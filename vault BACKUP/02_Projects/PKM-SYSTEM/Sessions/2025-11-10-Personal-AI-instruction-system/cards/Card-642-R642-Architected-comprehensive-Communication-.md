---
type: chat-card
parent_export: '[[Export]]'
order: 642
role: assistant
created: '2025-11-10T21:46:14.577327Z'
tags:
- chat-card
- python
- obsidian
- receipts
- code
- automation
attachments_count: 0
---

# 🤖 Message 642 - Assistant

**ID:** msg-642

## 💬 Content


**ID:** msg-642

Architected comprehensive IPC Communication note addressing technical foundations.L'utilisateur veut créer la note conceptuelle sur IPC Communication. C'est un sujet technique important pour comprendre pourquoi les raccourcis sont cassés. Je vais créer une note détaillée qui explique l'architecture IPC dans Electron, le problème actuel, et comment ça devrait fonctionner.📝 NOTE CONCEPTUELLE: IPC Communication
Fichier: 02_Projects/PKM-SYSTEM/Concepts/IPC Communication.md
markdown---
created: 2025-10-24T18:30:00
updated: 2025-11-01T19:40:00
type: concept
tags: [concept, architecture, pkm-system, ipc, electron, communication]
tech_stack: [electron, ipc, javascript]
status: broken
implemented_in: [main.js, preload.js, app.html]
related:
 - \"[[smartToggle Function]]\"
 - \"[[Global Shortcuts System]]\"
 - \"[[Architecture PKM System]]\"
 - \"[[Backlog]]\"
source: \"développement pkm-system phase 1.5\"
---

# 🔌 IPC Communication

> **Inter-Process Communication** - Architecture de communication entre Main et Renderer process

## Description

IPC (Inter-Process Communication) est le système de messagerie qui permet aux différents processus d'Electron de communiquer entre eux. Dans le PKM System, l'IPC est crucial pour faire fonctionner les raccourcis globaux.

## Problème Central

❌ **L'IPC est actuellement cassé**

**Impact:** Tous les raccourcis globaux (Layer 1) ne fonctionnent pas car les events ne sont pas transmis correctement du Main process au Renderer.

## Architecture Electron - Les 3 Processus

### Main Process
**Fichier:** `main.js`
**Rôle:**
- Gestion OS (fenêtres, raccourcis globaux, tray)
- Point d'entrée de l'app
- Contrôle du cycle de vie

**Capacités:**
- Accès complet Node.js
- APIs Electron (globalShortcut, BrowserWindow)
- Ne peut PAS manipuler le DOM

---

### Renderer Process
**Fichier:** `app.html` + scripts internes
**Rôle:**
- Affichage de l'interface utilisateur
- Manipulation du DOM
- Logique UI

**Capacités:**
- Accès DOM/CSS
- JavaScript frontend
- PAS d'accès direct Node.js (pour sécurité)

---

### Preload Process
**Fichier:** `preload.js`
**Rôle:** **BRIDGE** entre Main et Renderer
**Contexte:** Isolated context avec accès contrôlé

**Capacités:**
- Expose APIs sécurisées au Renderer
- Fait le pont IPC
- Context isolation pour sécurité

## Flow de Communication Actuel (CASSÉ)

### Ce qui devrait se passer
```
┌─────────────────────────────────────┐
│       MAIN PROCESS (main.js)        │
│                                     │
│  User presse Ctrl+Shift+Space      │
│         ↓                           │
│  globalShortcut callback           │
│         ↓                           │
│  smartToggle('capture')            │
│         ↓                           │
│  mainWindow.webContents.send(      │
│    'navigate-to',                  │
│    'capture'                       │
│  )                                 │
└──────────────┬──────────────────────┘
               │
               │ IPC Channel: 'navigate-to'
               │
               ↓
┌─────────────────────────────────────┐
│    PRELOAD PROCESS (preload.js)     │
│                                     │
│  ipcRenderer.on('navigate-to')     │
│         ↓                           │
│  Relay via contextBridge.expose    │
│         ↓                           │
│  window.electronAPI.onNavigate     │
└──────────────┬──────────────────────┘
               │
               │ postMessage / Custom Event
               │
               ↓
┌─────────────────────────────────────┐
│   RENDERER PROCESS (app.html)       │
│                                     │
│  window.electronAPI.onNavigate(    │
│    (page) => {                     │
│      navigateToPage(page);         │
│      updateUI();                   │
│    }                               │
│  )                                 │
└─────────────────────────────────────┘
```

### Ce qui se passe actuellement
```
MAIN PROCESS
    ↓
smartToggle('capture')
    ↓
webContents.send('navigate-to', 'capture')
    ↓
    ❌ RIEN - Event perdu dans le vide
    ↓
RENDERER ne reçoit jamais l'event
```

## Implémentation Actuelle (Cassée)

### main.js (OK)
```javascript
// Envoie l'event IPC
mainWindow.webContents.send('navigate-to', targetPage);
```

**Status:** ✅ Fonctionne - L'event est bien envoyé

---

### preload.js (CASSÉ)

**Chemin:** `C:\\Users\\idsmf\\Projects\\pkm-system\\electron\\src\\preload\\preload.js`

**Problème:** Handlers IPC manquants ou incomplets

**Ce qu'il devrait contenir:**
```javascript
const { contextBridge, ipcRenderer } = require('electron');

// Expose APIs sécurisées au renderer
contextBridge.exposeInMainWorld('electronAPI', {
    // Recevoir events du main process
    onNavigate: (callback) => {
        ipcRenderer.on('navigate-to', (event, page) => {
            callback(page);
        });
    },

    // Envoyer events au main process
    sendCurrentPage: (page) => {
        ipcRenderer.send('current-page-changed', page);
    },

    hideWindow: () => {
        ipcRenderer.send('hide-window');
    }
});
```

**Status:** ❌ Handlers manquants ou mal configurés

---

### app.html (CASSÉ)

**Problème:** Event listeners non configurés ou mal implémentés

**Ce qu'il devrait contenir:**
```javascript
// Écouter les events de navigation
if (window.electronAPI) {
    window.electronAPI.onNavigate((page) => {
        console.log(`Navigation vers: ${page}`);
        navigateToPage(page);
    });
} else {
    console.error('electronAPI non disponible!');
}

// Fonction de navigation
function navigateToPage(page) {
    // Cacher toutes les pages
    document.querySelectorAll('.page').forEach(p => {
        p.style.display = 'none';
    });

    // Afficher la page demandée
    const targetPage = document.getElementById(`${page}-page`);
    if (targetPage) {
        targetPage.style.display = 'block';

        // Notifier le main process du changement
        window.electronAPI.sendCurrentPage(page);
    }
}
```

**Status:** ❌ Listeners manquants ou event non capturé

## Diagnostic du Problème

### Checklist de Débuggage

**Main Process:**
- [x] `webContents.send()` est appelé
- [ ] Event name correct ('navigate-to')
- [ ] mainWindow existe et est ready

**Preload:**
- [ ] `contextBridge.exposeInMainWorld()` est appelé
- [ ] `ipcRenderer.on()` enregistré pour 'navigate-to'
- [ ] API exposée comme `window.electronAPI`

**Renderer:**
- [ ] `window.electronAPI` existe
- [ ] Event listener enregistré
- [ ] Fonction `navigateToPage()` définie

### Tests de Validation

#### Test 1: Vérifier preload chargé

**Dans app.html console:**
```javascript
console.log(window.electronAPI);
// Expected: Object avec méthodes onNavigate, etc.
// Actual: undefined ❌
```

#### Test 2: Vérifier event envoyé

**Dans main.js, ajouter:**
```javascript
mainWindow.webContents.send('navigate-to', targetPage);
console.log(`IPC sent: navigate-to → ${targetPage}`);
```

#### Test 3: Vérifier event reçu

**Dans preload.js, ajouter:**
```javascript
ipcRenderer.on('navigate-to', (event, page) => {
    console.log(`IPC received: ${page}`);
    callback(page);
});
```

## Solution Proposée

### Étape 1: Fixer preload.js
```javascript
// preload.js COMPLET
const { contextBridge, ipcRenderer } = require('electron');

console.log('Preload script loaded');

contextBridge.exposeInMainWorld('electronAPI', {
    // Navigation
    onNavigate: (callback) => {
        ipcRenderer.on('navigate-to', (event, page) => {
            console.log('[Preload] Navigate event:', page);
            callback(page);
        });
    },

    // Communication vers main
    sendCurrentPage: (page) => {
        ipcRenderer.send('current-page-changed', page);
    },

    hideWindow: () => {
        ipcRenderer.send('hide-window');
    },

    // Utilitaire pour debug
    ping: () => {
        console.log('electronAPI is alive!');
        return true;
    }
});

console.log('electronAPI exposed to window');
```

---

### Étape 2: Fixer app.html
```javascript
// app.html - Script d'initialisation
document.addEventListener('DOMContentLoaded', () => {
    console.log('DOM loaded');

    // Vérifier electronAPI
    if (!window.electronAPI) {
        console.error('❌ electronAPI not available!');
        return;
    }

    console.log('✅ electronAPI available');
    window.electronAPI.ping();

    // Enregistrer listener de navigation
    window.electronAPI.onNavigate((page) => {
        console.log(`📍 Navigation request: ${page}`);
        navigateToPage(page);
    });
});

function navigateToPage(page) {
    console.log(`Navigating to: ${page}`);

    // Cacher toutes pages
    document.querySelectorAll('.page').forEach(p => {
        p.classList.remove('active');
    });

    // Afficher page cible
    const targetPage = document.getElementById(`${page}-page`);
    if (targetPage) {
        targetPage.classList.add('active');

        // Notifier main du changement
        window.electronAPI.sendCurrentPage(page);
    } else {
        console.error(`Page not found: ${page}`);
    }
}
```

---

### Étape 3: Vérifier main.js handlers
```javascript
// main.js - Handlers IPC
ipcMain.on('current-page-changed', (event, page) => {
    console.log(`Current page changed: ${page}`);
    currentPage = page;
});

ipcMain.on('hide-window', () => {
    console.log('Hide window requested');
    if (mainWindow) {
        mainWindow.hide();
    }
});
```

## Architecture IPC Corrigée
```
┌──────────────────────────────────────────────┐
│              MAIN PROCESS                    │
│                                              │
│  ┌────────────────────────────────────┐     │
│  │  Global Shortcuts                  │     │
│  │  Ctrl+Shift+Space/F/H              │     │
│  └────────┬───────────────────────────┘     │
│           │                                  │
│           ↓                                  │
│  ┌────────────────────────────────────┐     │
│  │  smartToggle(page)                 │     │
│  └────────┬───────────────────────────┘     │
│           │                                  │
│           ↓                                  │
│  ┌────────────────────────────────────┐     │
│  │  webContents.send(                 │     │
│  │    'navigate-to', page             │     │
│  │  )                                 │     │
│  └────────┬───────────────────────────┘     │
└───────────┼──────────────────────────────────┘
            │
            │ IPC Channel: 'navigate-to'
            │
┌───────────▼──────────────────────────────────┐
│           PRELOAD PROCESS                    │
│                                              │
│  ┌────────────────────────────────────┐     │
│  │  ipcRenderer.on('navigate-to')     │     │
│  │      ↓                             │     │
│  │  contextBridge.exposeInMainWorld   │     │
│  │      ↓                             │     │
│  │  window.electronAPI.onNavigate     │     │
│  └────────┬───────────────────────────┘     │
└───────────┼──────────────────────────────────┘
            │
            │ Exposed API
            │
┌───────────▼──────────────────────────────────┐
│          RENDERER PROCESS                    │
│                                              │
│  ┌────────────────────────────────────┐     │
│  │  window.electronAPI.onNavigate()   │     │
│  │      ↓                             │     │
│  │  navigateToPage(page)              │     │
│  │      ↓                             │     │
│  │  Update DOM / UI                   │     │
│  └────────────────────────────────────┘     │
│                                              │
│  ┌────────────────────────────────────┐     │
│  │  window.electronAPI.sendCurrentPage│     │
│  │      ↓                             │     │
│  └────────┬───────────────────────────┘     │
└───────────┼──────────────────────────────────┘
            │
            │ IPC Channel: 'current-page-changed'
            │
┌───────────▼──────────────────────────────────┐
│           MAIN PROCESS                       │
│                                              │
│  ┌────────────────────────────────────┐     │
│  │  ipcMain.on('current-page-changed')│     │
│  │      ↓                             │     │
│  │  currentPage = page                │     │
│  └────────────────────────────────────┘     │
└──────────────────────────────────────────────┘
```

## Channels IPC Utilisés

| Channel | Direction | Data | Description |
|---------|-----------|------|-------------|
| `navigate-to` | Main → Renderer | `string` (page) | Demande navigation vers page |
| `current-page-changed` | Renderer → Main | `string` (page) | Notification changement page |
| `hide-window` | Renderer → Main | `void` | Demande masquage fenêtre |

## Sécurité Context Isolation

**Principe:** Le renderer ne doit JAMAIS avoir accès direct à `ipcRenderer` ou modules Node.js.

**Pourquoi:**
- Protection contre injection de code malveillant
- Sandboxing du renderer process
- Best practice Electron

**Comment:**
```javascript
// ❌ DANGEREUX - Ne JAMAIS faire ça
nodeIntegration: true
contextIsolation: false

// ✅ SÉCURISÉ - Configuration actuelle
nodeIntegration: false
contextIsolation: true
preload: path.join(__dirname, 'preload.js')
```

## Features Dépendantes
```dataview
TABLE shortcut as \"Raccourci\", status as \"Status\", priority as \"Priorité\"
FROM \"02_Projects/PKM-SYSTEM\"
WHERE contains(dependencies, \"IPC\") OR contains(dependencies, \"ipc\") OR contains(tech_stack, \"ipc\")
SORT priority DESC
```

### Liste Manuelle
- [[Ctrl+Shift+Space - Toggle Capture]] - Dépend IPC pour navigation
- [[Ctrl+Shift+F - Toggle Reference]] - Dépend IPC pour navigation
- [[Ctrl+Shift+H - Toggle Hub]] - Dépend IPC pour navigation
- [[smartToggle Function]] - Utilise IPC pour communiquer

## Plan de Fix

### Phase 1: Diagnostic (1h)
- [ ] Vérifier preload.js est bien chargé
- [ ] Logger tous les IPC sends/receives
- [ ] Tester `window.electronAPI` dans console

### Phase 2: Implémentation (2h)
- [ ] Compléter preload.js avec tous handlers
- [ ] Ajouter listeners dans app.html
- [ ] Tester chaque channel individuellement

### Phase 3: Validation (1h)
- [ ] Tester Ctrl+Shift+Space
- [ ] Tester Ctrl+Shift+F
- [ ] Tester Ctrl+Shift+H
- [ ] Vérifier tracking currentPage

### Phase 4: Documentation (30min)
- [ ] Mettre à jour status des cartes raccourcis
- [ ] Documenter fix dans cette note
- [ ] Créer tests de régression

## Ressources Liées

### Concepts
- [[smartToggle Function]] - Utilise IPC
- [[currentPage Variable]] - Synchronisé via IPC
- [[Architecture PKM System]] - Vue globale

### Code
- [[main.js]] - IPC sender (Main process)
- [[preload.js]] - IPC bridge ⚠️ À FIXER
- [[app.html]] - IPC receiver (Renderer)

### Features Impactées
- [[Global Shortcuts System]] - Tous cassés à cause IPC
- [[MOC Raccourcis]] - Index complet

### Documentation
- [[Phase 1.5 - Refactor]] - Contexte fix
- [[Backlog]] - Tâche prioritaire

---

## 📚 Références Electron

**Documentation officielle:**
- [IPC Tutorial](https://www.electronjs.org/docs/latest/tutorial/ipc)
- [Context Isolation](https://www.electronjs.org/docs/latest/tutorial/context-isolation)
- [Context Bridge](https://www.electronjs.org/docs/latest/api/context-bridge)
- [IpcMain](https://www.electronjs.org/docs/latest/api/ipc-main)
- [IpcRenderer](https://www.electronjs.org/docs/latest/api/ipc-renderer)

---

**Dernière mise à jour:** 2025-11-01T19:40:00
**Status:** ❌ BROKEN - Cause racine de tous les raccourcis Layer 1
**Priorité:** 🔴 CRITICAL
**Prochaine action:** Fix preload.js + app.html event listeners

✅ RÉSUMÉ DE LA NOTE
Type: Concept architecture
Sujet: Communication inter-processus Electron
Contenu:

✅ Explication des 3 processus Electron
✅ Flow de communication actuel (cassé)
✅ Diagnostic précis du problème
✅ Code de fix proposé (preload.js + app.html)
✅ Architecture IPC corrigée (diagramme)
✅ Liste des channels utilisés
✅ Explications sécurité
✅ Plan de fix étape par étape
✅ Références Electron officielles
✅ Liens vers toutes les notes reliées


🎯 ÉTAT ACTUEL DU PKM SYSTEM
Notes créées aujourd'hui:
Shortcuts (3)

✅ Ctrl+Shift+Space - Toggle Capture
✅ Ctrl+Shift+F - Toggle Reference
✅ Ctrl+Shift+H - Toggle Hub

Concepts (2)

✅ smartToggle Function
✅ IPC Communication

MOCs (2)

✅ MOC Raccourcis (avec Dataview)
✅ Global Shortcuts System


🚀 PROCHAINES ÉTAPES POSSIBLES
Option A: Créer la 3ème note conceptuelle [[currentPage Variable]]
Option B: Créer les 2 cartes Layer 1 manquantes (Ctrl+W, Ctrl+Shift+W)
Option C: Passer aux raccourcis Layer 2 (Ctrl+1/2/3, Ctrl+B)
Option D: Faire un bilan complet de ce qu'on a accompli
Option E: Commencer à parcourir les chats pour extraire des cartes
Ton choix ? 🚀

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-641-R641-Architected-comprehensive-Communication-]]
- ⬇️ Next: [[Card-643-R643-Architected-comprehensive-Communication-]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #python
- #obsidian
- #receipts
- #code
- #automation
