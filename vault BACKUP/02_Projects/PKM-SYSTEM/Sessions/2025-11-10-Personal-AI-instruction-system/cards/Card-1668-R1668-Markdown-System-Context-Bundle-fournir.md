---
type: chat-card
parent_export: '[[Export]]'
order: 1668
role: assistant
created: '2025-11-10T21:46:27.303353Z'
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

# 🤖 Message 1668 - Assistant

**ID:** msg-1668

## 💬 Content


**ID:** msg-1668

markdown# 🧠 PKM System - Context Bundle

> **À fournir au début de chaque nouvelle session Claude**

---

## 📁 STRUCTURE VAULT
```
vault/
├── 00_Inbox/
├── 02_Projects/
│   └── PKM-SYSTEM/
│       ├── BackLog/
│       │   ├── MOC - Backlog.md
│       │   └── Items/ (4 items)
│       ├── Concepts/ (3 notes)
│       ├── Decisions/
│       │   ├── Next Action Choice.md
│       │   ├── Options/ (6 cartes)
│       │   └── Snapshots/
│       │       ├── Meta/
│       │       └── Full/
│       ├── Shortcuts/ (8 cartes)
│       ├── Toggl/
│       │   └── Phase-1-Organisation/ (1 task)
│       └── TODO.md
├── 04_Resources/
│   └── Templates/ (6 templates)
└── 06_Meta/
    ├── TAG_REGISTRY.md
    └── Decisions/
```

---

## 🏷️ TAGS ESSENTIELS

**Types:**
- `moc`, `concept`, `feature`, `shortcut`, `backlog-item`, `toggl-task`, `decision-point`, `snapshot-index`, `snapshot-full`

**Status:**
- `todo`, `in-progress`, `done`, `archived`, `broken`, `active`

**Priority:**
- `urgent`, `high`, `medium`, `low`

**Categories:**
- `bug`, `feature`, `improvement`, `idea`, `technical-debt`

**Voir:** [[TAG_REGISTRY]] pour liste complète (100+ tags)

---

## 📝 NOTES CLÉS (MOCs)

### Décisions
- [[Next Action Choice]] - Living decision point v2.0

### Projets
- [[TODO]] - Master TODO
- [[MOC - Backlog]] - Backlog atomique

### Shortcuts
- [[MOC Raccourcis]] - Index shortcuts PKM
- [[Global Shortcuts System]] - Layer 1
- [[MOC - Tmux Shortcuts]] - Tmux commands

### Meta
- [[TAG_REGISTRY]] - Source vérité tags
- [[CONTEXT]] - Ce fichier

---

## 🎯 ÉTAT ACTUEL

**Phase:** 1.5 - Refactor + Organisation
**Dernière session:** 2025-11-02 (3h39)

**Accomplissements récents:**
- ✅ TAG_REGISTRY finalisé (100+ tags)
- ✅ Snapshots system (Meta/Full structure)
- ✅ Backlog atomique (MOC + Items)
- ✅ Templates créés (6 templates)

**En cours:**
- [ ] Fix IPC Communication (urgent)
- [ ] Continuer cartes shortcuts

**Décisions récentes:**
- Snapshots: Meta/Full au lieu de Index/Snaps
- Backlog: Atomique au lieu de monolithique
- Toggl: Versioned (privacy review planned)

---

## 📋 CONVENTIONS

### Nommage Fichiers

**Snapshots:**
```
Meta: YYYY-MM-DDTHH-mm-ss - Title vX.Y.md
Full: YYYY-MM-DDTHH-mm-ss - Title vX.Y [FULL].md
```

**Backlog Items:**
```
Item Name.md (descriptif, pas de préfixe)
```

**Decisions:**
```
Decision Name.md (pas de date dans nom)
```

### Métadonnées Standards

**Toutes notes:**
```yaml
created: YYYY-MM-DDTHH:mm:ss
updated: YYYY-MM-DDTHH:mm:ss
type: [type]
tags: [tag1, tag2]
status: [status]
```

**Toggl tasks:**
```yaml
type: toggl-task
estimated_time: \"Xh\"
estimated_time_minutes: X
actual_time: \"Xh\"
actual_time_minutes: X
```

**Backlog items:**
```yaml
type: backlog-item
category: [bug|feature|improvement|idea|technical-debt]
priority: [urgent|high|medium|low]
estimated_time_minutes: X
```

---

## 🔧 TEMPLATES DISPONIBLES

1. `BacklogItem.md` - Backlog atomique
2. `SnapshotMeta.md` - Snapshot metadata
3. `SnapshotFull-Instructions.md` - Instructions Full
4. `DecisionPoint.md` - Point de décision
5. `LivingDocument.md` - Document évolutif
6. `TogglTaskNote.md` - Tâche Toggl

---

## 🎨 STYLE & APPROCHE

**Principes:**
- **Atomicité** - Une note = un concept
- **Liens > Duplication** - [[Référencer]] au lieu de copier
- **Dataview > Listes** - Queries dynamiques
- **YAML > Texte** - Métadonnées queryables
- **MOC style** - Index avec queries, pas monolithes

**Queries préférées:**
```dataview
TABLE/LIST avec WHERE et SORT
Éviter TASK (sauf vraies checkboxes)
GROUP BY pour catégories
```

---

## 💬 COMMUNICATION

**Commits:**
- Fréquents (10+ par session)
- Messages détaillés
- Format: `type: description`

**Rappels automatiques:**
- Toggl start/stop
- Commits réguliers
- Création cartes pour décisions

**Ton:**
- Direct, pas de blabla
- Émojis pertinents
- Structuré mais pas over-formaté

---

## 🔗 LIENS RAPIDES

**Documentation:**
- [[TAG_REGISTRY]] - Tags canoniques
- [[SNAPSHOT_PROCESS]] - Process snapshots
- [[TODO]] - Tâches actuelles

**Projets:**
- [[MOC - Backlog]] - Backlog items
- [[Next Action Choice]] - Décisions

**Templates:**
- `04_Resources/Templates/` - Tous templates

---

**Dernière mise à jour:** 2025-11-02T16:40:00
**Maintenir:** À chaque changement majeur structure/conventions

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-1667-R1667-DataviewSUM-FROM-Toggl-WHERE-type]]
- ⬇️ Next: [[Card-1669-R1669-Markdown-Context-System-Phase-Refactor]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #python
- #obsidian
- #receipts
- #code
- #git
- #automation
