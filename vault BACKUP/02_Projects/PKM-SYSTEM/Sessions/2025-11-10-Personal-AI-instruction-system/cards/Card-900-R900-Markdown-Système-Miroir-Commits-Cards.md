---
type: chat-card
parent_export: '[[Export]]'
order: 900
role: assistant
created: '2025-11-10T21:46:18.215961Z'
tags:
- chat-card
- python
- obsidian
- code
- git
- automation
attachments_count: 0
---

# 🤖 Message 900 - Assistant

**ID:** msg-900

## 💬 Content


**ID:** msg-900

markdown### 12. Système Git Miroir + Commits Cards (Futur)

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
07_Git/ ← NOUVEAU dossier
│
├── pkm-system/ ← 1 dossier = 1 repo
│ ├── README.md ← Infos repo
│ │
│ ├── Branches/
│ │ ├── main.md
│ │ ├── feature-git-mirror-structure.md
│ │ └── phase-1-5-refactor.md
│ │
│ ├── Commits/
│ │ ├── 2025-11/
│ │ │ ├── 2025-11-01T20-30-00 - docs add master TODO.md
│ │ │ ├── 2025-11-02T14-15-22 - fix IPC communication.md
│ │ │ └── ...
│ │ └── 2025-10/
│ │
│ ├── Pull-Requests/
│ │ └── PR-001 - Refactor shortcuts.md
│ │
│ └── Issues/
│ └── Issue-001 - IPC broken.md
│
└── autre-repo/
 └── ...

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-899-R899-Bashgit-checkout-feature-mirror-structur]]
- ⬇️ Next: [[Card-901-R901-Yaml-created-date-YYYY-time]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #python
- #obsidian
- #code
- #git
- #automation
