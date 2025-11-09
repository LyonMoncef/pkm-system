---
created: 2025-11-01 15:30:00
updated: '2025-11-02T04:34:51'
'type:': MOC
tags:
- layer-1
- moc
- pkm-system
- shortcut
related:
- '[[_Raccourcis]]'
- '[[Architecture PKM System]]'
---

# 🌍 Global Shortcuts System - Layer 1

> **Raccourcis OS Level** - Fonctionnent même quand l'app est cachée ou minimisée

## 📊 Vue d'Ensemble

**Total:** 5 raccourcis globaux  
**Actifs:** 0  
**Cassés:** 5  
**Layer:** 1 (OS Level)

---

## 🎹 Liste des Raccourcis Globaux
```dataview
TABLE
  shortcut as "Raccourci",
  quicksummary as "Description",
  status as "Status",
  priority as "Priorité",
  updated as "Dernière MAJ"
FROM "02_Projects/PKM-SYSTEM/Shortcuts"
WHERE contains(tags, "layer-1")
SORT priority DESC, status ASC, shortcut ASC
```

---

## 🔧 Architecture Technique

### Implémentation

**Fichier:** `src/main/main.js`  
**Fonction:** `registerGlobalShortcuts()`  
**Chemin:** `C:\Users\idsmf\Projects\pkm-system\electron\src\main\main.js`

### Dépendances Système

- `electron.globalShortcut` - API Electron pour shortcuts OS
- `smartToggle()` - Logique de toggle window
- `currentPage` - Variable de tracking
- IPC bridge via `preload.js`

### Flow d'Exécution
```
User presse raccourci
    ↓
OS détecte (globalShortcut)
    ↓
main.js callback
    ↓
smartToggle(page)
    ↓
IPC → renderer
    ↓
Navigation + show/hide
```

---

## ⚠️ Problème Actuel

❌ **Tous les raccourcis globaux sont BROKEN**

**Cause racine:**
- Communication IPC cassée entre main process et renderer
- `postMessage` non configuré correctement
- Event listeners manquants dans preload.js

**Impact:**
- Les raccourcis sont définis mais ne répondent pas
- L'app ne réagit pas aux keypresses globaux
- Workflow principal du système non fonctionnel

**Fix en cours:**
Voir [[02_Projects/PKM-SYSTEM/BackLog/Backlog]] - Refactor IPC architecture

---

## 🎯 Raccourcis par Catégorie

### Window Toggle (3)
```dataview
LIST quicksummary
FROM "02_Projects/PKM-SYSTEM/Shortcuts"
WHERE contains(tags, "toggle-window") AND contains(tags, "layer-1")
SORT shortcut ASC
```

### Window Management (2)
```dataview
LIST quicksummary
FROM "02_Projects/PKM-SYSTEM/Shortcuts"
WHERE contains(tags, "window-management") AND contains(tags, "layer-1")
SORT shortcut ASC
```

---

## 📋 Actions Prioritaires

- [ ] Fix IPC communication (HIGH priority)
- [ ] Test chaque raccourci individuellement
- [ ] Documenter le fix dans les cartes
- [ ] Update status à "active"
- [ ] Créer tests de régression

---

## 📚 Ressources Liées

### Documentation
- [[_Raccourcis]] - Index complet de tous les raccourcis
- [[IPC Communication]] - Architecture de communication
- [[smartToggle Function]] - Implémentation du toggle

### Fichiers Code
- [[main.js]] - Implémentation des shortcuts
- [[preload.js]] - IPC bridge
- [[app.html]] - Réception des events

### Contexte Projet
- [[Phase 1.5 - Refactor]] - Contexte refactoring
- [[02_Projects/PKM-SYSTEM/BackLog/Backlog]] - Tâches en cours
- [[Architecture PKM System]] - Vue d'ensemble

---

## 🔍 Recherches Utiles

**Par status:**
```dataview
TABLE shortcut, quicksummary, updated
FROM "02_Projects/PKM-SYSTEM/Shortcuts"
WHERE contains(tags, "layer-1") AND status = "broken"
```

**Par priorité:**
```dataview
TABLE shortcut, status, quicksummary
FROM "02_Projects/PKM-SYSTEM/Shortcuts"
WHERE contains(tags, "layer-1") AND priority = "high"
```

---

**Dernière mise à jour:** 2025-11-01T15:30:00  
**Maintenance:** Review hebdomadaire des status