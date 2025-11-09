---
created: 2025-10-24T15:45:00
updated: 2025-11-01T19:30:00
type: concept
tags: [concept, code, pkm-system, function, window-management, electron]
tech_stack: [electron, javascript]
implemented_in: main.js
related:
  - "[[Global Shortcuts System]]"
  - "[[Ctrl+Shift+Space - Toggle Capture]]"
  - "[[Ctrl+Shift+F - Toggle Reference]]"
  - "[[Ctrl+Shift+H - Toggle Hub]]"
  - "[[IPC Communication]]"
  - "[[currentPage Variable]]"
source: "développement pkm-system phase 1.5"
---

# 🔄 smartToggle Function

> **Fonction centrale** du système de window management - Gère l'affichage intelligent des fenêtres

## Description

La fonction `smartToggle()` est le cœur du système de navigation du PKM System. Elle implémente la logique de toggle intelligent qui permet d'afficher, masquer ou naviguer vers une page en fonction de l'état actuel de l'application.

## Rôle dans l'Architecture

**Position:** Main Process (Electron)  
**Layer:** Architecture de base  
**Utilisée par:** Tous les raccourcis globaux Layer 1
```
Global Shortcuts (Layer 1)
    ↓
smartToggle(targetPage)
    ↓
Window Management + Navigation
```

## Implémentation

**Fichier:** [main.js](file:///C:/Users/idsmf/Projects/pkm-system/electron/src/main/main.js) (ligne ~78)  
**Fonction:** `smartToggle()`

### Paramètres

**`targetPage`** (string)
- Valeurs possibles: `'capture'`, `'hub'`, `'reference'`
- La page vers laquelle naviguer

## Logique de Décision

### État 1: Fenêtre n'existe pas
```
mainWindow === null
    ↓
createMainWindow()
    ↓
navigate-to targetPage
    ↓
update currentPage
```

**Use case:** Premier lancement de l'app

---

### État 2: Fenêtre cachée
```
mainWindow.isVisible() === false
    ↓
mainWindow.show()
    ↓
navigate-to targetPage
    ↓
update currentPage
```

**Use case:** App minimisée/cachée, on la rappelle

---

### État 3: Sur la même page
```
currentPage === targetPage
    ↓
mainWindow.hide()
```

**Use case:** Toggle off - masquer l'app quand déjà sur la bonne page

---

### État 4: Sur une autre page
```
currentPage !== targetPage
    ↓
navigate-to targetPage
    ↓
update currentPage
```

**Use case:** Navigation entre pages

## Dépendances

### Variables Globales
- **`mainWindow`** - Instance BrowserWindow
- **`currentPage`** - String tracking page active

### Fonctions
- **`createMainWindow()`** - Crée la fenêtre principale
- **`mainWindow.webContents.send()`** - IPC communication

### IPC Events
- **`'navigate-to'`** - Event envoyé au renderer pour navigation

## Features Utilisant smartToggle
```dataview
TABLE shortcut as "Raccourci", status as "Status", priority as "Priorité"
FROM "02_Projects/PKM-SYSTEM"
WHERE contains(dependencies, "smartToggle")
SORT priority DESC, shortcut ASC
```

## Problème Actuel

⚠️ **La fonction existe mais ne fonctionne pas**

**Cause:**
- IPC communication cassée
- Event `'navigate-to'` non reçu par le renderer
- `preload.js` ne fait pas le relay

**Impact:**
- Tous les raccourcis globaux Layer 1 sont broken
- La fonction s'exécute mais rien ne se passe côté UI

**Fix nécessaire:**
Voir [[IPC Communication]] pour résoudre le bridge

## Tests de Validation

### Test 1: Création fenêtre
```javascript
// App fermée
smartToggle('capture')
// Expected: Fenêtre créée + navigate to capture
```

### Test 2: Rappel fenêtre
```javascript
// App cachée
mainWindow.hide();
smartToggle('hub')
// Expected: Fenêtre affichée + navigate to hub
```

### Test 3: Toggle off
```javascript
// Sur page capture
currentPage = 'capture';
smartToggle('capture')
// Expected: Fenêtre masquée
```

### Test 4: Navigation
```javascript
// Sur page hub
currentPage = 'hub';
smartToggle('reference')
// Expected: Navigate to reference, fenêtre reste visible
```

## Améliorations Futures

### Version 2.0 Potentielle
```javascript
function smartToggle(targetPage, options = {}) {
    const {
        forceShow = false,      // Force show même si sur la page
        animate = true,         // Animations de transition
        focusElement = null,    // Auto-focus sur élément
        position = 'remember'   // remember|center|mouse
    } = options;
    
    // ... logique enrichie
}
```

**Nouvelles features possibles:**
- Animation de transition fluide
- Positionnement intelligent (près souris, centré, mémorisé)
- Auto-focus sur input (ex: capture textarea, search bar)
- Options de toggle (force show vs toggle)
- Callbacks/events pour tracking

### Idées d'optimisation

1. **Debouncing** - Éviter appels multiples rapides
2. **State machine** - FSM pour états de fenêtre
3. **Caching** - Mémoriser dernière position/size
4. **Async/await** - Meilleure gestion asynchrone
5. **Error handling** - Try/catch + fallbacks

## Architecture Visée
```
┌─────────────────────────────────────┐
│      Global Shortcuts (OS)          │
│  Ctrl+Shift+Space/F/H/W             │
└──────────────┬──────────────────────┘
               │
               ↓
┌─────────────────────────────────────┐
│       smartToggle(page)             │
│  • Check window state               │
│  • Decide action (show/hide/nav)    │
│  • Send IPC to renderer             │
│  • Update currentPage               │
└──────────────┬──────────────────────┘
               │
               ↓ (IPC: 'navigate-to')
┌─────────────────────────────────────┐
│         Renderer Process            │
│  app.html receives event            │
│  → Navigate to target page          │
│  → Update UI                        │
└─────────────────────────────────────┘
```

## Ressources Liées

### Concepts
- [[IPC Communication]] - Architecture communication
- [[currentPage Variable]] - Tracking état
- [[Window Management]] - Gestion fenêtres

### Code
- [[main.js]] - Fichier d'implémentation
- [[preload.js]] - IPC bridge (à fixer)
- [[app.html]] - Récepteur des events

### Features
- [[Global Shortcuts System]] - Vue d'ensemble
- [[MOC Raccourcis]] - Index complet

### Documentation
- [[Architecture PKM System]] - Vue globale
- [[Phase 1.5 - Refactor]] - Contexte développement

---

## 📚 Références Electron

**Electron API utilisée:**
- [BrowserWindow](https://www.electronjs.org/docs/latest/api/browser-window)
- [webContents.send()](https://www.electronjs.org/docs/latest/api/web-contents#contentssendchannel-args)
- [globalShortcut](https://www.electronjs.org/docs/latest/api/global-shortcut)

---

**Dernière mise à jour:** 2025-11-01T19:30:00  
**Status:** Implémentée mais non fonctionnelle (IPC cassé)  
**Prochaine action:** Fix IPC bridge pour activer la fonction
```

---

## 📁 STRUCTURE SUGGÉRÉE

**Créer le dossier Concepts:**
```
02_Projects/PKM-SYSTEM/
├── Shortcuts/
│   ├── Ctrl+Shift+Space - Toggle Capture - BROKEN.md
│   ├── Ctrl+Shift+F - Toggle Reference - BROKEN.md
│   └── Ctrl+Shift+H - Toggle Hub - BROKEN.md
├── Concepts/              ← NOUVEAU
│   └── smartToggle Function.md
└── Global Shortcuts System.md