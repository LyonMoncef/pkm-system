---
created: 2025-11-02T21:15:00
updated: 2025-11-02T21:15:00
type: task-list
status: active
tags:
  - project
  - pkm-system
  - todo
  - priorities
related:
  - "[[02_Projects/PKM-SYSTEM/BackLog/Backlog]]"
  - "[[Toggl Tasks - Refactor Plan]]"
  - "[[MOC Raccourcis]]"
---

# 📋 TODO - PKM System

> **Master TODO List** - Toutes les tâches en attente

---

## 🔴 URGENT - Bloquants

### 1. Finaliser TAG_REGISTRY (30-45min)
**Pourquoi urgent:** Bloque création/modification de toutes les notes

- [ ] Intégrer mapping de normalisation des 75 tags existants
- [ ] Ajouter tags manquants identifiés
- [ ] Valider conventions finales
- [ ] Commit `TAG_REGISTRY.md` dans `06_Meta/`

**Fichier:** `06_Meta/TAG_REGISTRY.md`

---

### 2. Migration Tags (1-2h)
**Pourquoi urgent:** Nettoyer incohérences avant de continuer

- [ ] Script Python de migration (optionnel mais recommandé)
- [ ] OU Migration manuelle tag par tag
- [ ] Vérifier avec Dataview après migration
- [ ] Commit "chore: normalize all tags"

**Migrations prioritaires:**
```
Electron → electron (3 notes)
BuildInPublic → build-in-public (6 notes)
shortcuts → shortcut (4 notes)
```

---

## 🟠 HIGH - Important

### 3. Finaliser Instructions Claude (30min)

- [ ] Arbitrer derniers points v1.0 vs v2.0
- [ ] Intégrer décisions Toggl + Git aliases + Mood
- [ ] Sauvegarder version finale dans Project
- [ ] OU créer `06_Meta/Claude-Instructions.md`

---

### 4. Structure Toggl (1h)

- [ ] Créer `02_Projects/PKM-SYSTEM/Toggl/`
- [ ] Créer sous-dossiers par phase (Phase-1, Phase-2, etc.)
- [ ] Créer MOC - Toggl Tasks.md avec Dataview
- [ ] Créer template TogglTaskNote.md dans `04_Resources/Templates/`
- [ ] Créer 5 premières notes tasks Phase 1 (exemple)

**Structure:**
```
02_Projects/PKM-SYSTEM/Toggl/
├── MOC - Toggl Tasks.md
├── Phase-1-Documentation/
├── Phase-2-Extraction-CSS-JS/
├── Phase-3-Refactor-Shortcuts/
└── Phase-4-Polish-Cleanup/
```

---

### 5. Fix IPC Communication (2-3h) ⚠️ TECHNIQUE

**Bloque:** Tous les raccourcis Layer 1

- [ ] Fixer preload.js (ajouter handlers IPC)
- [ ] Fixer app.html (event listeners)
- [ ] Tester event 'navigate-to'
- [ ] Tester Ctrl+Shift+Space
- [ ] Tester Ctrl+Shift+F
- [ ] Tester Ctrl+Shift+H
- [ ] Update status notes à "active"
- [ ] Commit "fix: IPC communication working"

**Référence:** [[IPC Communication]]

---

## 🟡 MEDIUM - Compléter Documentation

### 6. Cartes Shortcuts Manquantes (30min)

**Layer 1 - Global:**
- [ ] Créer `Ctrl+W - Quick Save & Hide - BROKEN.md`
- [ ] Créer `Ctrl+Shift+W - Force Quit - BROKEN.md`

**Layer 2 - Internal:**
- [ ] Créer `Ctrl+1 - Navigate to Capture - PARTIAL.md`
- [ ] Créer `Ctrl+2 - Navigate to Hub - PARTIAL.md`
- [ ] Créer `Ctrl+3 - Navigate to Reference - PARTIAL.md`
- [ ] Créer `Ctrl+B - Toggle Sidebar - ACTIVE.md`
- [ ] Créer `F1 - Show Shortcuts Help - BROKEN.md`
- [ ] Créer `Ctrl+Slash - Show Shortcuts Help - BROKEN.md`

**Layer 3 - Page-Specific:**
- [ ] Créer `Esc - Exit Insert Mode - ACTIVE.md`
- [ ] Créer `Ctrl+I - Enter Insert Mode - ACTIVE.md`
- [ ] Créer `Ctrl+S - Save to Vault - ACTIVE.md`
- [ ] Créer `Ctrl+K - Clear Editor - ACTIVE.md`

---

### 7. Structure Environnement Complète (1h)

- [ ] Créer `04_Resources/Environnement/Terminal/`
- [ ] Créer `04_Resources/Environnement/Editors/`
- [ ] Créer `04_Resources/Environnement/Version-Control/`
- [ ] Créer `04_Resources/Environnement/System/`

**Git Aliases:**
- [ ] Créer `Version-Control/Git/MOC - Git Workflows.md`
- [ ] Créer `Version-Control/Git/Aliases.md`
- [ ] Documenter: comt, gs, gl, gd

**Nvim:**
- [ ] Créer `Editors/Nvim/MOC - Nvim Commands.md`
- [ ] Créer 10 commandes les plus utilisées (dd, yy, etc.)

---

### 8. Refacto Notes PKM-SYSTEM Existantes (1-2h)

**Notes à traiter:**
- [ ] `VisuMethode.md` - Standardiser métadonnées
- [ ] `Backlog.md` - Convertir en format actuel
- [ ] Notes LinkedIn (4 notes) - Uniformiser
- [ ] `2025-10-18 1st note.md` - Archiver ou refacto
- [ ] `2025-10-18 Note saved.md` - Archiver ou refacto
- [ ] Autres notes 2025-10-20 - Trier

---

## 🟢 LOW - Nice to Have

### 9. Compléter Shortcuts Tmux (30min)

**Ajouter:**
- [ ] Ctrl+B c - New Window
- [ ] Ctrl+B n/p - Navigate Windows
- [ ] Ctrl+B , - Rename Window
- [ ] Ctrl+B arrows - Navigate Panes
- [ ] Ctrl+B z - Toggle Fullscreen
- [ ] Ctrl+B [ - Copy Mode

---

### 10. MOC Global (30min)

- [ ] Créer `02_Projects/PKM-SYSTEM/MOC - PKM System.md`
- [ ] Index de tous les sous-MOCs
- [ ] Vue d'ensemble du projet
- [ ] Liens vers phases, milestones, etc.

---

### 11. Script Automation (Futur)

**Idées:**
- [ ] Script validation tags pre-commit
- [ ] Script génération notes Toggl depuis CSV
- [ ] Script sync Toggl → Obsidian
- [ ] Script backup vault

---
### 12. Système Git Miroir + Commits Cards (Futur)

**Structure Git dans Vault:**
- [ ] Créer `07_Git/` pour structure miroir repos
- [ ] Créer `07_Git/pkm-system/` (miroir repo actuel)
- [ ] Sous-structure: `Branches/`, `Commits/`, `PRs/`
- [ ] Template CommitCard.md
- [ ] Script auto-génération carte par commit (git hook)

**TODO Centralisé:**
- [ ] Créer `06_Meta/TODO.md` avec Dataview global
- [ ] Query toutes notes avec checkboxes
- [ ] Vue par projet, priorité, status

**Workflow Git Strict:**
- [ ] Rappels commits automatiques entre tâches
- [ ] Proposition branches pour nouveaux sujets
- [ ] 1 commit = 1 carte obligatoire
```

---

## 2️⃣ Structure Git Miroir Proposée
```
07_Git/                              ← NOUVEAU dossier
│
├── pkm-system/                      ← 1 dossier = 1 repo
│   ├── README.md                    ← Infos repo
│   │
│   ├── Branches/
│   │   ├── main.md
│   │   ├── feature-git-mirror-structure.md
│   │   └── phase-1-5-refactor.md
│   │
│   ├── Commits/
│   │   ├── 2025-11/
│   │   │   ├── 2025-11-01T20-30-00 - docs add master TODO.md
│   │   │   ├── 2025-11-02T14-15-22 - fix IPC communication.md
│   │   │   └── ...
│   │   └── 2025-10/
│   │
│   ├── Pull-Requests/
│   │   └── PR-001 - Refactor shortcuts.md
│   │
│   └── Issues/
│       └── Issue-001 - IPC broken.md
│
└── autre-repo/
    └── ...

---
## 📊 Statistiques

**Total tâches:** 50+

| Priorité | Tâches | Temps Estimé |
|----------|--------|--------------|
| 🔴 URGENT | 2 | 2-3h |
| 🟠 HIGH | 3 | 4-6h |
| 🟡 MEDIUM | 4 | 3-5h |
| 🟢 LOW | 4 | 2-3h |
| **TOTAL** | **13 blocs** | **11-17h** |

---

## 🎯 Ordre Recommandé

### Session 1 (2-3h) - Débloquer
1. ✅ Finaliser TAG_REGISTRY (30min)
2. ✅ Migration tags (1-2h)
3. ✅ Instructions Claude finales (30min)

### Session 2 (2-3h) - Structure
4. ✅ Structure Toggl (1h)
5. ✅ Structure Environnement (1h)
6. ✅ Git Aliases + Nvim basics (1h)

### Session 3 (2-3h) - Refacto
7. ✅ Refacto notes PKM-SYSTEM (1-2h)
8. ✅ Cartes shortcuts manquantes (1h)

### Session 4 (2-3h) - Technique
9. ✅ Fix IPC Communication (2-3h)

### Session 5+ - Polish
10. Compléter Tmux, MOC Global, etc.

---

## 🔗 Liens Rapides

**Documentation:**
- [[TAG_REGISTRY]] - Source de vérité tags
- [[Claude Instructions v2.0]] - Instructions projet
- [[MOC Raccourcis]] - Index shortcuts

**Technique:**
- [[IPC Communication]] - Fix prioritaire
- [[Global Shortcuts System]] - Vue Layer 1
- [[Architecture PKM System]] - Vue globale

**Suivi:**
- [[02_Projects/PKM-SYSTEM/BackLog/Backlog]] - Backlog général
- [[Toggl Tasks - Refactor Plan]] - Plan refactor
- [[2025-10-16 Le Pari PKM System]] - Vision

---

## 📅 Tracking

**Créé:** 2025-11-02T21:15:00  
**Session actuelle:** Refacto + Organisation  
**Prochaine session:** TAG_REGISTRY + Migration tags

---

**💡 TIP:** Cocher les tâches au fur et à mesure. Commit régulièrement !