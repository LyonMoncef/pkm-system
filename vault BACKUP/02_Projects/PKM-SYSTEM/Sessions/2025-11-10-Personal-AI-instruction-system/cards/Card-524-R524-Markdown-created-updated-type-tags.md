---
type: chat-card
parent_export: '[[Export]]'
order: 524
role: assistant
created: '2025-11-10T21:46:13.147878Z'
tags:
- chat-card
- python
- obsidian
- receipts
- code
- git
- automation
attachments_count: 0
---

# 🤖 Message 524 - Assistant

**ID:** msg-524

## 💬 Content


**ID:** msg-524

markdown---
created: 2025-11-01T15:30:00
updated: 2025-11-01T15:30:00
type: moc
tags: [moc, pkm-system, shortcuts, global, layer-1]
related:
 - \"[[MOC Raccourcis]]\"
 - \"[[Architecture PKM System]]\"
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

| Raccourci | Description | Status | Priorité | Dernière MAJ |
|-----------|-------------|--------|----------|--------------|
| [[Ctrl+Shift+Space - Toggle Capture\\|Ctrl+Shift+Space]] | Toggle fenêtre Capture depuis n'importe où | 🔴 BROKEN | HIGH | 2025-11-01T15:30 |
| [[Ctrl+W - Quick Save & Hide\\|Ctrl+W]] | Sauvegarde rapide et cache la fenêtre | 🔴 BROKEN | HIGH | 2025-11-01T15:30 |
| [[Ctrl+Shift+F - Toggle Reference\\|Ctrl+Shift+F]] | Toggle fenêtre Reference depuis n'importe où | 🔴 BROKEN | MEDIUM | 2025-11-01T15:30 |
| [[Ctrl+Shift+H - Toggle Hub\\|Ctrl+Shift+H]] | Toggle fenêtre Hub depuis n'importe où | 🔴 BROKEN | MEDIUM | 2025-11-01T15:30 |
| [[Ctrl+Shift+W - Force Quit\\|Ctrl+Shift+W]] | Quitte l'application complètement | 🔴 BROKEN | LOW | 2025-11-01T15:30 |

---

## 🔧 Architecture Technique

### Implémentation

**Fichier:** `src/main/main.js`
**Fonction:** `registerGlobalShortcuts()`
**Chemin:** `C:\\Users\\idsmf\\Projects\\pkm-system\\electron\\src\\main\\main.js`

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
Voir [[Backlog]] - Refactor IPC architecture

---

## 🎯 Raccourcis par Catégorie

### Window Toggle (3)

- [[Ctrl+Shift+Space - Toggle Capture]] - Toggle fenêtre Capture depuis n'importe où
- [[Ctrl+Shift+F - Toggle Reference]] - Toggle fenêtre Reference depuis n'importe où
- [[Ctrl+Shift+H - Toggle Hub]] - Toggle fenêtre Hub depuis n'importe où

### Window Management (2)

- [[Ctrl+W - Quick Save & Hide]] - Sauvegarde rapide et cache la fenêtre
- [[Ctrl+Shift+W - Force Quit]] - Quitte l'application complètement

---

## 📋 Actions Prioritaires

- [ ] Fix IPC communication (HIGH priority)
- [ ] Test chaque raccourci individuellement
- [ ] Documenter le fix dans les cartes
- [ ] Update status à \"active\"
- [ ] Créer tests de régression

---

## 📚 Ressources Liées

### Documentation
- [[MOC Raccourcis]] - Index complet de tous les raccourcis
- [[IPC Communication]] - Architecture de communication
- [[smartToggle Function]] - Implémentation du toggle

### Fichiers Code
- [[main.js]] - Implémentation des shortcuts
- [[preload.js]] - IPC bridge
- [[app.html]] - Réception des events

### Contexte Projet
- [[Phase 1.5 - Refactor]] - Contexte refactoring
- [[Backlog]] - Tâches en cours
- [[Architecture PKM System]] - Vue d'ensemble

---

**Dernière mise à jour:** 2025-11-01T15:30:00
**Maintenance:** Review hebdomadaire des status - Mise à jour manuelle nécessaire sans Dataview

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-523-R523-DATAVIEW-ACTIVÉ-PROBLÈME-plugin-Dataview]]
- ⬇️ Next: [[Card-525-R525-DataviewTABLE-status-priority-FROM-featu]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #python
- #obsidian
- #receipts
- #code
- #git
- #automation
