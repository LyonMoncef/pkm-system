---
created: 2025-10-20T01:00:00
updated: 2025-11-01T20:30:00
type: task-list
status: in-progress
tags:
  - project
  - pkm-system
  - refactor
  - phase-1-5
  - tasks
  - toggl
related:
  - "[[2025-10-20 Migration Electron Terminée]]"
  - "[[2025-10-16 Le Pari PKM System]]"
  - "[[02_Projects/PKM-SYSTEM/BackLog/Backlog]]"
  - "[[MOC Raccourcis]]"
project: pkm-system
phase: 1.5
---

# 📋 Toggl Tasks - Refactor Plan

> **Liste de tâches** - Refactor architecture Phase 1.5

---

## 🎯 Objectif

Clean architecture refactor : Extraction CSS + Redesign Shortcuts

---

## 📊 Configuration Toggl

### Projet
**Nom:** PKM System - Refactor Plan  
**Description:** Clean architecture refactor - CSS extraction + Shortcuts redesign  
**Couleur:** Violet (#667eea)

### Tags Toggl

**Phases:**
- `#phase1` `#phase2` `#phase3` `#phase4`

**Catégories:**
- `#git` `#doc` `#css` `#js` `#shortcut` `#architecture`

**Actions:**
- `#setup` `#implementation` `#test` `#cleanup` `#bugfix`

**UI/UX:**
- `#ui` `#visual` `#ux`

---

## 📋 Tasks par Phase

### Phase 1 - Documentation (17min)

- [ ] [P1.1] Commit sauvegarde état actuel (5min) - `#phase1 #git #baseline`
- [ ] [P1.2] Créer SHORTCUTS.md (5min) - `#phase1 #doc #shortcut`
- [ ] [P1.3] Créer REFACTOR.md avec plan (5min) - `#phase1 #doc #architecture`
- [ ] [P1.4] Merge phase1 dans main (2min) - `#phase1 #git`

---

### Phase 2 - Extraction CSS/JS (58min)

- [ ] [P2.1] Créer structure /styles et /scripts (5min) - `#phase2 #setup #folders`
- [ ] [P2.2] Extraire variables CSS → global.css (10min) - `#phase2 #css #layer-1`
- [ ] [P2.3] Extraire app.html CSS → app.css (10min) - `#phase2 #css`
- [ ] [P2.4] Extraire capture.html CSS → capture.css (10min) - `#phase2 #css`
- [ ] [P2.5] Extraire hub.html CSS → hub.css (5min) - `#phase2 #css`
- [ ] [P2.6] Extraire reference.html CSS → reference.css (5min) - `#phase2 #css`
- [ ] [P2.7] Update <link> imports dans HTML (5min) - `#phase2 #setup`
- [ ] [P2.8] Test fonctionnel toutes pages (5min) - `#phase2 #test #visual`
- [ ] [P2.9] Commit + merge phase2 (3min) - `#phase2 #git`

---

### Phase 3 - Refactor Shortcuts (92min)

- [ ] [P3.1] Créer scripts/shortcuts.js structure (5min) - `#phase3 #setup #js`
- [ ] [P3.2] Documenter shortcuts actuels (5min) - `#phase3 #doc #shortcut`
- [ ] [P3.3] Supprimer shortcuts de app.html (5min) - `#phase3 #cleanup`
- [ ] [P3.4] Supprimer shortcuts de capture.html (5min) - `#phase3 #cleanup`
- [ ] [P3.5] Supprimer shortcuts de hub.html (3min) - `#phase3 #cleanup`
- [ ] [P3.6] Supprimer shortcuts de reference.html (3min) - `#phase3 #cleanup`
- [ ] [P3.7] Implémenter Layer 2 navigation (10min) - `#phase3 #implementation #shortcut`
- [ ] [P3.8] Test Ctrl+1/2/3/B individuellement (5min) - `#phase3 #test`
- [ ] [P3.9] Implémenter relay mechanism propre (10min) - `#phase3 #implementation #architecture`
- [ ] [P3.10] Test relay depuis chaque page (5min) - `#phase3 #test`
- [ ] [P3.11] Implémenter shortcuts help Ctrl+/ (10min) - `#phase3 #implementation #ui`
- [ ] [P3.12] Fix IPC chain global shortcuts (10min) - `#phase3 #bugfix #architecture`
- [ ] [P3.13] Test complet matrix shortcuts (10min) - `#phase3 #test`
- [ ] [P3.14] Commit + merge phase3 (3min) - `#phase3 #git`

---

### Phase 4 - Polish & Cleanup (33min)

- [ ] [P4.1] Supprimer code mort (watchdog, debug) (5min) - `#phase4 #cleanup`
- [ ] [P4.2] Update keyboard hints popup UI (5min) - `#phase4 #ui`
- [ ] [P4.3] Update status bar raccourcis (3min) - `#phase4 #ui`
- [ ] [P4.4] Checklist tests manuels complète (10min) - `#phase4 #test`
- [ ] [P4.5] Update README.md (5min) - `#phase4 #doc`
- [ ] [P4.6] Commit + merge phase4 (3min) - `#phase4 #git`
- [ ] [P4.7] Tag release v0.2.0-refactor (2min) - `#phase4 #git`

---

## 📊 Récapitulatif

**Total estimé:** ~3h20min (200min)

| Phase | Durée | Tâches |
|-------|-------|--------|
| Phase 1 | 17min | 4 |
| Phase 2 | 58min | 9 |
| Phase 3 | 92min | 14 |
| Phase 4 | 33min | 7 |

---

## 🔗 Liens

- [[MOC Raccourcis]] - Documentation shortcuts
- [[Global Shortcuts System]] - Système Layer 1
- [[IPC Communication]] - Architecture IPC
- [[02_Projects/PKM-SYSTEM/BackLog/Backlog]] - Backlog général

---

**Dernière mise à jour:** 2025-11-01T20:30:00  
**Status:** In Progress - Phase 1.5 Refactor