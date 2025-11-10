---
type: chat-card
parent_export: '[[Export]]'
order: 887
role: assistant
created: '2025-11-10T21:46:18.057777Z'
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

# 🤖 Message 887 - Assistant

**ID:** msg-887

## 💬 Content


**ID:** msg-887

Internalisé directives critiques : commits obligatoires, structure Git miroir, cartes par commit.L'utilisateur me donne des instructions très importantes :

TODO.md dans 06_Meta/ avec Dataview pour centraliser toutes les TODOs - à ajouter au backlog
Garder les TODO locales aux projets aussi (comme actuellement)
RÈGLE CRITIQUE : Entre CHAQUE tâche et à CHAQUE modif, lui rappeler EN GROS EN GRAS EN ITALIQUE de faire des commits
Même si on enchaîne sur autre chose, toujours lui dire de committer avant
Proposer de créer une nouvelle branche pour le nouveau sujet
Chaque commit doit avoir sa carte dans le vault
Répliquer structure GitHub dans le vault : 1 dossier = 1 repo

Branches
Commits
Structure miroir


C'est une consigne ABSOLUE à respecter. Je dois l'intégrer dans les instructions Claude et ne JAMAIS l'oublier.
Je dois maintenant :

Mettre à jour TODO.md avec cette idée de 06_Meta/TODO.md + Dataview
Ajouter cette consigne commits dans les Instructions Claude
Proposer structure Git miroir dans vault
⚠️ COMMIT URGENT - AVANT DE CONTINUER
🔴 STOP - COMMIT TES CHANGEMENTS ACTUELS
Tu as créé/modifié :

02_Projects/PKM-SYSTEM/TODO.md
Instructions Claude v2.0 (discussions)
TAG_REGISTRY discussions
Notes Toggl, Git aliases, etc.

ACTION IMMÉDIATE :
bashcd ~/vault
git add -A
git commit -m \"docs: add master TODO list + Claude instructions v2.0 discussion\"
git push

🌿 NOUVELLE BRANCHE POUR SUJET SUIVANT ?
On va parler de :

Structure Git miroir dans vault
Système commits → cartes
06_Meta/TODO.md centralisé

Tu veux créer une branche ?
bashgit checkout -b feature/git-mirror-structure
OU on continue sur main ?


📝 MISE À JOUR TODO + NOUVELLES RÈGLES
1️⃣ Ajout au TODO.md
Ajouter dans section 🟢 LOW:
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

3️⃣ Template CommitCard.md
Fichier: 04_Resources/Templates/CommitCard.md
yaml---
created: {{date:YYYY-MM-DD}}T{{time:HH:mm:ss}}
updated: {{date:YYYY-MM-DD}}T{{time:HH:mm:ss}}
type: git-commit
tags: [git, commit, repo-name]
commit_hash: \"\"
commit_date: \"\"
branch: \"\"
author: \"\"
related: []
---

# {{commit_message}}

## 📊 Commit Info

**Hash:** `{{hash}}`
**Date:** {{date}}
**Branch:** {{branch}}
**Author:** {{author}}

## 📝 Changements

### Fichiers Modifiés
- `file1.js` - Description changement
- `file2.md` - Description changement

### Type
- [ ] feat - Nouvelle feature
- [ ] fix - Bug fix
- [ ] docs - Documentation
- [ ] refactor - Refactoring
- [ ] test - Tests
- [ ] chore - Maintenance

## 💡 Contexte

Pourquoi ce commit ? Quel problème résout-il ?

## 🔗 Liens

- [[Issue reliée]]
- [[PR reliée]]
- [[Note technique]]

---

**Status:** Merged/Open

4️⃣ RÈGLE ABSOLUE - Instructions Claude v2.0
À ajouter dans section ⚠️ RÈGLES CRITIQUES:
markdown### Git Workflow Strict - RÈGLE ABSOLUE

**Entre CHAQUE tâche et à CHAQUE modification:**

1. ***🔴 RAPPELER EN GROS GRAS ITALIQUE de committer***
2. ***Proposer message de commit approprié***
3. ***Si changement de sujet → Proposer nouvelle branche***
4. ***Après commit → Créer CommitCard.md correspondante***

**Format rappel obligatoire:**
```
# ⚠️ ***COMMIT URGENT - AVANT DE CONTINUER***

## ***🔴 STOP - COMMIT TES CHANGEMENTS ACTUELS***

**Tu as créé/modifié :**
- Fichier 1
- Fichier 2

### ***ACTION IMMÉDIATE :***
git add -A
git commit -m \"type: message\"
git push

## 🌿 ***NOUVELLE BRANCHE POUR SUJET SUIVANT ?***
[Proposer si changement contexte]
```

**NE JAMAIS continuer sans avoir fait ce rappel si des fichiers ont changé.**

5️⃣ 06_Meta/TODO.md Centralisé (Futur)
Fichier: 06_Meta/TODO.md
yaml---
created: 2025-11-02T21:30:00
updated: 2025-11-02T21:30:00
type: meta-todo
tags: [meta, todo, centralized, dataview]
---

# 📋 TODO - Vue Globale

> **Toutes les TODOs du vault** - Centralisé via Dataview

---

## 🔴 Par Priorité

### Urgent
```dataview
TASK
FROM \"\"
WHERE contains(text, \"🔴\") OR contains(text, \"URGENT\")
SORT file.ctime DESC
```

### High Priority
```dataview
TASK
FROM \"\"
WHERE contains(text, \"🟠\") OR contains(text, \"HIGH\")
SORT file.ctime DESC
```

---

## 📁 Par Projet

### PKM System
```dataview
TASK
FROM \"02_Projects/PKM-SYSTEM\"
WHERE !completed
SORT file.ctime DESC
```

### Autres Projets
```dataview
TASK
FROM \"02_Projects\" AND !\"02_Projects/PKM-SYSTEM\"
WHERE !completed
GROUP BY file.folder
```

---

## 📅 Par Date

### Aujourd'hui
```dataview
TASK
WHERE file.cday = date(today)
```

### Cette Semaine
```dataview
TASK
WHERE file.cday >= date(today) - dur(7 days)
SORT file.ctime DESC
```

---

## ✅ Complétées Récemment
```dataview
TASK
WHERE completed
SORT completion DESC
LIMIT 20
```
```

---

## 🎯 WORKFLOW AVEC COMMITS

### Exemple Session Type
```
1. User: \"On commence TAG_REGISTRY\"
 Claude: \"***COMMIT d'abord si changements en cours***\"
 User: [fait commit]

2. Claude: Propose création TAG_REGISTRY.md
 User: Travaille dessus

3. User: \"Attends, j'ai une question sur les tags\"
 Claude: \"***STOP - COMMIT TAG_REGISTRY avant de dévier***\"
 \"***Créer branche feature/tag-question ?***\"
 User: [commit + branche]

4. User finit tag question
 Claude: \"***COMMIT cette discussion***\"
 \"***Créer CommitCard.md***\"
 \"***Merger dans main ?***\"

⚠️ TON ACTION MAINTENANT
1. COMMIT CE QU'ON VIENT DE FAIRE
bashgit add 02_Projects/PKM-SYSTEM/TODO.md
git commit -m \"docs: update TODO with git mirror structure + commit rules\"
git push
2. CRÉER BRANCHE POUR GIT MIRROR ?
bashgit checkout -b feature/git-mirror-structure
OU continuer sur main ?

Dis-moi et on continue ! 🚀Réessayer

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-886-S886-ID-msg-886]]
- ⬇️ Next: [[Card-888-R888-Internalisé-directives-critiques-commits]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #python
- #obsidian
- #receipts
- #code
- #git
- #automation
