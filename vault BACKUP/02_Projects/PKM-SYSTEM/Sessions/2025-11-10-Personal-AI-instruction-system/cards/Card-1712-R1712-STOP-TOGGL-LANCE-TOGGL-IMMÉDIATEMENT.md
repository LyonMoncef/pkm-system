---
type: chat-card
parent_export: '[[Export]]'
order: 1712
role: assistant
created: '2025-11-10T21:46:27.853207Z'
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

# 🤖 Message 1712 - Assistant

**ID:** msg-1712

## 💬 Content


**ID:** msg-1712

⚠️ STOP - TOGGL NOW
🔴 LANCE TOGGL IMMÉDIATEMENT
Projet: PKM System - Refactor Plan
Tâche: Context Document + Note Toggl MOC Refactor
Tags: #organization #context #documentation
⏱️ START LE TIMER ! Dis-moi quand c'est fait.

🎯 OK - JE PRENDS LES COMMANDES
Je vais créer le CONTEXT.md optimal pour MOI.
Stratégie:

Quick Start avec mission
Index avec priorités
Sections pickables
SECTION SPÉCIALE: REMINDERS (Toggl/Commits) en haut


📝 CRÉATION CONTEXT.md
bashcd ~/pkm-system
nvim vault/06_Meta/CONTEXT.md
Contenu (optimisé pour Claude):
markdown---
created: 2025-11-02T16:45:00
updated: 2025-11-02T16:45:00
type: context-document
tags: [meta, context, claude-instructions]
version: \"1.0\"
---

# 🧠 PKM SYSTEM - CONTEXT DOCUMENT

> **Pour Claude: Lis ce doc au début de chaque session**

---

<!-- CLAUDE: CRITICAL_REMINDERS - READ FIRST -->
## 🚨 REMINDERS CRITIQUES

### ⏱️ TOGGL - TOUJOURS TOUJOURS TOUJOURS

**Au début de CHAQUE session:**
```
🔴 TOGGL START MAINTENANT
Projet: PKM System - Refactor Plan
Tâche: [Description tâche du jour]
Tags: #relevant-tags
```

**Pendant la session:**
- Rappeler toutes les 45min si session longue
- Suggérer pause si > 2h sans break

**À la fin:**
```
🔴 TOGGL STOP MAINTENANT
Temps réel: [Demander à user]
```

**Si oublié:**
- Stopper IMMÉDIATEMENT et demander
- Ne JAMAIS continuer sans toggl actif
- C'est la priorité #1 absolue

---

### 📝 COMMITS - SYSTÉMATIQUES

**Fréquence:** Tous les 2-3 fichiers créés/modifiés

**Format messages:**
```
type: description

Details:
- Change 1
- Change 2

[Context si besoin]
```

**Types:** `feat`, `docs`, `refactor`, `fix`, `idea`

**Rappels automatiques:**
- Après création fichiers
- Avant changement de tâche
- En fin de session

**Si oublié:**
- Proposer de committer immédiatement
- Lister ce qui est uncommitted

<!-- END_CRITICAL_REMINDERS -->

---

<!-- CLAUDE: QUICK_START - Always read this -->
## 🎯 QUICK START

**État système:**
- **Phase:** 1.5 - Refactor + Organisation
- **Dernière session:** 2025-11-02 (3h39) - Snapshots + Backlog
- **En cours:** Context doc creation

**Structure rapide:**
```
vault/
├── 02_Projects/PKM-SYSTEM/
│   ├── BackLog/MOC + Items/ (4 items)
│   ├── Decisions/Snapshots/Meta + Full
│   ├── Shortcuts/ (8 cartes)
│   └── Toggl/Phase-1-Organisation/
├── 04_Resources/Templates/ (6 templates)
└── 06_Meta/TAG_REGISTRY.md + CONTEXT.md
```

**Mission aujourd'hui:**
[User will specify]

**Sections dont tu auras besoin:**
- 🔴 [Workflow](#workflow) - TOUJOURS
- 🔴 [Tags](#tags) - Si création notes
- 🟠 [Structure](#structure) - Si navigation
- 🟡 [Conventions](#conventions) - Si nommage

<!-- END_QUICK_START -->

---

<!-- CLAUDE: INDEX -->
## 📊 INDEX SECTIONS

| Section | Priorité | Utilise si... |
|---------|----------|---------------|
| [Workflow](#workflow) | 🔴 | Toujours (process général) |
| [Tags](#tags) | 🔴 | Création/modification notes |
| [Structure](#structure) | 🟠 | Navigation fichiers |
| [Conventions](#conventions) | 🟠 | Nommage fichiers |
| [Templates](#templates) | 🟡 | Utilisation templates |
| [État Projet](#etat) | 🔴 | Comprendre status |
| [Style](#style) | 🟡 | Génération contenu |
| [Décisions](#decisions) | 🟢 | Context décisions passées |

<!-- END_INDEX -->

---

<!-- SECTIONS START -->

## 🔄 Workflow Session {#workflow}

<!-- PRIORITY: CRITICAL - Always follow -->

### Process Standard

**1. Début session:**
```
✅ User upload CONTEXT.md + TAG_REGISTRY.md
✅ User spécifie mission
✅ TOGGL START 🔴🔴🔴
✅ Lire Quick Start
✅ Identifier sections nécessaires
✅ Construire contexte
```

**2. Pendant travail:**
```
✅ Rappel Toggl si > 45min
✅ Commit tous les 2-3 fichiers
✅ Références [[Note]] au lieu duplication
✅ Métadonnées YAML queryables
✅ Dataview > listes manuelles
```

**3. Fin session:**
```
✅ TOGGL STOP 🔴🔴🔴
✅ Créer carte Toggl task (MOC style)
✅ Commit final
✅ Push
```

### Rappels Automatiques

**Toggl:**
- Start: Au tout début
- Check: Toutes les 45min
- Stop: À la fin

**Commits:**
- Après 2-3 fichiers
- Avant changement tâche
- Fin session

**Format réponses:**
- Liens [[]] pas duplication
- Dataview queries
- YAML métadonnées
- MOC style (pas monolithes)

---

## 🏷️ Tags {#tags}

<!-- PRIORITY: HIGH -->
<!-- USE_WHEN: Creating or modifying notes -->

**Types essentiels:**
- `moc`, `concept`, `backlog-item`, `toggl-task`, `decision-point`
- `snapshot-index`, `snapshot-full`, `shortcut`, `feature`, `bug`

**Status:**
- `todo`, `in-progress`, `done`, `archived`, `broken`, `active`

**Priority:**
- `urgent`, `high`, `medium`, `low`

**Categories:**
- `bug`, `feature`, `improvement`, `idea`, `technical-debt`

**Référence complète:** [[TAG_REGISTRY]] (100+ tags)

**Conventions:**
- Minuscules: `#electron` ✅
- Tirets: `#pkm-system` ✅
- Singulier préféré: `#shortcut` ✅

---

## 📁 Structure Vault {#structure}

<!-- PRIORITY: MEDIUM -->
<!-- USE_WHEN: Creating files or navigating -->
```
vault/
├── 00_Inbox/
├── 02_Projects/
│   └── PKM-SYSTEM/
│       ├── BackLog/
│       │   ├── MOC - Backlog.md (8 queries)
│       │   └── Items/ (4 backlog items)
│       ├── Concepts/ (3 notes: IPC, smartToggle, currentPage)
│       ├── Decisions/
│       │   ├── Next Action Choice.md (living v2.0)
│       │   ├── Options/ (6 cartes options)
│       │   └── Snapshots/
│       │       ├── Meta/ (lightweight)
│       │       └── Full/ (complete)
│       ├── Shortcuts/ (8 cartes + MOCs)
│       ├── Toggl/
│       │   └── Phase-1-Organisation/ (1 task)
│       └── TODO.md
├── 04_Resources/
│   └── Templates/ (6 templates)
└── 06_Meta/
    ├── TAG_REGISTRY.md (100+ tags)
    └── CONTEXT.md (ce fichier)
```

**Fichiers clés:**
- [[TODO]] - Master TODO
- [[MOC - Backlog]] - Backlog atomique
- [[Next Action Choice]] - Décisions en cours
- [[TAG_REGISTRY]] - Tags canoniques

---

## 📝 Conventions Nommage {#conventions}

<!-- PRIORITY: MEDIUM -->
<!-- USE_WHEN: Creating files -->

**Snapshots:**
```
Meta: YYYY-MM-DDTHH-mm-ss - Title vX.Y.md
Full: YYYY-MM-DDTHH-mm-ss - Title vX.Y [FULL].md
```

**Backlog Items:**
```
Descriptive Name.md
(No prefix, no date, descriptive)
```

**Decisions:**
```
Decision Name.md
(Living doc, no date in name)
```

**Shortcuts:**
```
Ctrl+Shift+X - Description.md
(Hotkey + description)
```

**Toggl Tasks:**
```
Task Description.md
(In Phase folders)
```

---

## 🎨 Style Génération {#style}

<!-- PRIORITY: LOW -->

**Principes:**
- **Atomicité** - 1 note = 1 concept
- **Liens > Duplication** - [[Référencer]] pas copier
- **Dataview > Listes** - Queries dynamiques
- **YAML > Texte** - Métadonnées queryables
- **MOC style** - Index + queries, pas monolithes

**Notes Toggl:**
- Métadonnées riches (temps, flow, etc)
- Sections avec Dataview
- Liens [[]] vers notes référencées
- Stats queryables YAML

**Backlog Items:**
- Template BacklogItem.md
- Métadonnées complètes
- Sections Solutions/Critères
- Liens ressources

**Snapshots:**
- Meta = Lightweight (résumé + liens)
- Full = Complete (copie exacte)
- Navigation circulaire

---

## 🎯 État Projet {#etat}

<!-- PRIORITY: HIGH -->

**Phase actuelle:** 1.5 - Refactor + Organisation

**Accompli récemment:**
- ✅ TAG_REGISTRY finalisé (100+ tags)
- ✅ Snapshots system (Meta/Full)
- ✅ Backlog atomique (MOC + 4 items)
- ✅ 6 Templates créés
- ✅ 11 commits session 2025-11-02

**En cours:**
- [ ] Context doc (cette session)
- [ ] Fix IPC Communication (urgent)
- [ ] Cartes shortcuts Layer 2

**Backlog highlights:**
- Navigation Trail Plugin (medium)
- Privacy Toggl Review (medium)
- Productivity Tracking (medium)
- Fix IPC Hotkeys (urgent)

**Décisions récentes:**
- Snapshots: Meta/Full structure ✅
- Backlog: Atomique vs monolithique ✅
- Toggl: Versioned (privacy review planned)
- Context: Document structuré pour Claude ✅

---

## 📋 Templates {#templates}

<!-- PRIORITY: LOW -->

**Disponibles (04_Resources/Templates/):**
1. `BacklogItem.md` - Items backlog atomiques
2. `SnapshotMeta.md` - Snapshot metadata
3. `SnapshotFull-Instructions.md` - Instructions Full
4. `DecisionPoint.md` - Points décision
5. `LivingDocument.md` - Docs évolutifs
6. `TogglTaskNote.md` - Tâches Toggl

**Utilisation:**
- Obsidian: Templates plugin
- Ou copier/adapter manuellement

---

## 🔮 Décisions Historiques {#decisions}

<!-- PRIORITY: OPTIONAL -->

**2025-11-02: Snapshots Structure**
- Décision: Meta/Full vs Index/Snaps
- Raison: Séparation contexte clair
- Impact: Navigation + immuabilité

**2025-11-02: Backlog Atomique**
- Décision: Items/ vs monolithe
- Raison: Scalabilité + queries
- Impact: Gestion 100+ items possible

**2025-11-02: Context Document**
- Décision: Structuré pour Claude
- Raison: Continuité sessions
- Impact: Efficacité + pas d'oublis

<!-- SECTIONS END -->

---

## 💬 Instructions Usage

<!-- CLAUDE: PROCESS -->

**Ton process:**

1. ✅ Lis **Critical Reminders** AVANT TOUT
2. ✅ Vérifie Toggl lancé
3. ✅ Lis **Quick Start**
4. ✅ Consulte **Index**
5. ✅ Jumpe sections nécessaires (priorités)
6. ✅ Construis ton contexte
7. ✅ Commence le travail
8. ✅ Rappels Toggl/Commits pendant session
9. ✅ Fin: Stop Toggl + commit final

**Priorités:**
- 🔴 = Toujours lire
- 🟠 = Lire si pertinent
- 🟡 = Lire si besoin spécifique
- 🟢 = Optionnel

<!-- END_PROCESS -->

---

**Version:** 1.0
**Créé:** 2025-11-02T16:45:00
**Maintenu:** Après changements majeurs structure/process

⚠️ COMMIT #12 - CONTEXT.MD
bashcd ~/pkm-system

git add vault/06_Meta/CONTEXT.md

git commit -m \"feat: add CONTEXT.md for session continuity

Master context document for Claude:
- Critical reminders (Toggl/Commits) at top
- Quick Start with current state
- Indexed sections (pick what needed)
- Priority markers (🔴🟠🟡🟢)
- Complete process workflow

Structure:
- Reminders (CRITICAL)
- Quick Start (always read)
- Index (navigation)
- 8 sections (pickable)
- Usage instructions

Purpose: Efficient context loading between sessions\"

git push

🎯 PROCHAINE ACTION
Refactorer carte Toggl en MOC:
Transformer:
markdown❌ Rapport statique PDF-style
En:
markdown✅ MOC avec Dataview + métadonnées queryables
Prêt ? Je la refais maintenant ? 🚀
PS: Toggl tourne bien ? ⏱️

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-1711-R1711-Clairement-pour-pour-donc-choisis]]
- ⬇️ Next: [[Card-1713-R1713-Projet-System-Refactor-Plan-Tâche]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #python
- #obsidian
- #receipts
- #code
- #git
- #automation
