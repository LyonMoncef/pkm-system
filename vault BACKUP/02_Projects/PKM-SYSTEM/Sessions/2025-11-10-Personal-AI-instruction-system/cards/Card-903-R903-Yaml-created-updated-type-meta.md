---
type: chat-card
parent_export: '[[Export]]'
order: 903
role: assistant
created: '2025-11-10T21:46:18.250874Z'
tags:
- chat-card
- obsidian
- code
- git
- automation
attachments_count: 0
---

# 🤖 Message 903 - Assistant

**ID:** msg-903

## 💬 Content


**ID:** msg-903

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

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-902-R902-Markdown-Workflow-Strict-RÈGLE-ABSOLUE]]
- ⬇️ Next: [[Card-904-R904-Bashgit-SYSTEM-TODO-commit-docs]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #obsidian
- #code
- #git
- #automation
