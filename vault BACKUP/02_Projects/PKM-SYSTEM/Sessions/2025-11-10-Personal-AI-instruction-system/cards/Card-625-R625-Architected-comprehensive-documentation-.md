---
type: chat-card
parent_export: '[[Export]]'
order: 625
role: assistant
created: '2025-11-10T21:46:14.383673Z'
tags:
- chat-card
- python
- obsidian
- receipts
- code
- automation
attachments_count: 0
---

# 🤖 Message 625 - Assistant

**ID:** msg-625

## 💬 Content


**ID:** msg-625

Architected comprehensive documentation structure for smartToggle function.L'utilisateur veut créer une note conceptuelle pour la fonction smartToggle. C'est une note qui va documenter un concept technique/une fonction du code.
Ça devrait être dans 04_Resources/Code/ puisque c'est du code, ou peut-être dans 02_Projects/PKM-SYSTEM/ dans un sous-dossier \"Concepts\" ou \"Functions\".
Cette note doit :

Avoir les bonnes métadonnées (created, updated, type, tags, etc.)
Expliquer ce qu'est smartToggle
Son rôle dans l'architecture
Où elle est implémentée
Comment elle fonctionne
Quelles features l'utilisent
Liens vers les cartes de raccourcis qui en dépendent

Type: concept ou code-concept
Tags: [concept, code, pkm-system, function, window-management]📝 NOTE CONCEPTUELLE: smartToggle Function
Fichier: 02_Projects/PKM-SYSTEM/Concepts/smartToggle Function.md
markdown---
created: 2025-10-24T15:45:00
updated: 2025-11-01T19:30:00
type: concept
tags: [concept, code, pkm-system, function, window-management, electron]
tech_stack: [electron, javascript]
implemented_in: main.js
related:
 - \"[[Global Shortcuts System]]\"
 - \"[[Ctrl+Shift+Space - Toggle Capture]]\"
 - \"[[Ctrl+Shift+F - Toggle Reference]]\"
 - \"[[Ctrl+Shift+H - Toggle Hub]]\"
 - \"[[IPC Communication]]\"
 - \"[[currentPage Variable]]\"
source: \"développement pkm-system phase 1.5\"
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

**Fichier:** `main.js`
**Chemin:** `C:\\Users\\idsmf\\Projects\\pkm-system\\electron\\src\\main\\main.js`
**Ligne approximative:** ~78

### Code Actuel
```javascript
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
    } else if (currentPage === targetPage) {
        // On same page → Hide (toggle off)
        mainWindow.hide();
    } else {
        // On different page → Navigate
        mainWindow.webContents.send('navigate-to', targetPage);
        currentPage = targetPage;
    }
}
```

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
TABLE shortcut as \"Raccourci\", status as \"Status\", priority as \"Priorité\"
FROM \"02_Projects/PKM-SYSTEM\"
WHERE contains(dependencies, \"smartToggle\")
SORT priority DESC, shortcut ASC
```

### Liste Manuelle (si Dataview ne marche pas)
- [[Ctrl+Shift+Space - Toggle Capture]] - Toggle fenêtre Capture
- [[Ctrl+Shift+F - Toggle Reference]] - Toggle fenêtre Reference
- [[Ctrl+Shift+H - Toggle Hub]] - Toggle fenêtre Hub

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
│ ├── Ctrl+Shift+Space - Toggle Capture - BROKEN.md
│ ├── Ctrl+Shift+F - Toggle Reference - BROKEN.md
│ └── Ctrl+Shift+H - Toggle Hub - BROKEN.md
├── Concepts/ ← NOUVEAU
│ └── smartToggle Function.md
└── Global Shortcuts System.md

✅ RÉSUMÉ DE LA NOTE
Type: Concept technique
Sujet: Fonction centrale de window management
Contenu:

✅ Description et rôle
✅ Code actuel documenté
✅ Logique de décision (4 états)
✅ Dépendances claires
✅ Features qui l'utilisent
✅ Problème actuel (IPC)
✅ Tests de validation
✅ Améliorations futures
✅ Diagramme architecture
✅ Liens vers cartes reliées


🎯 PROCHAINE ÉTAPE
Option A: Créer la 2ème note conceptuelle [[IPC Communication]]
Option B: Créer la 3ème note conceptuelle [[currentPage Variable]]
Option C: Créer les 2 cartes Layer 1 manquantes (Ctrl+W, Ctrl+Shift+W)
Option D: Faire un bilan et voir ce qu'on a accompli aujourd'hui
Ton choix ? 🚀

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-624-R624-Architected-comprehensive-documentation-]]
- ⬇️ Next: [[Card-626-R626-Architected-comprehensive-documentation-]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #python
- #obsidian
- #receipts
- #code
- #automation
