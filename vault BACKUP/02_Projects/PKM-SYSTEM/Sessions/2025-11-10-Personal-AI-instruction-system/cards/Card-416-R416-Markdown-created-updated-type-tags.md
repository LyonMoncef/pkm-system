---
type: chat-card
parent_export: '[[Export]]'
order: 416
role: assistant
created: '2025-11-10T21:46:11.577913Z'
tags:
- chat-card
- python
- obsidian
- code
- automation
attachments_count: 0
---

# 🤖 Message 416 - Assistant

**ID:** msg-416

## 💬 Content


**ID:** msg-416

markdown---
created: 2025-11-01T15:10:00
updated: 2025-11-01T15:10:00
type: moc
tags: [moc, meta, tags, index]
---

# 🏷️ MOC - Système de Tags

> **Map of Content** - Index et organisation des tags du vault

## 📊 Vue d'Ensemble
```dataview
TABLE length(file.tags) as \"Nombre de tags\"
FROM \"\"
SORT length(file.tags) DESC
LIMIT 10
```

---

## 🗂️ TAXONOMIE DES TAGS

### **Par Type de Contenu**

#### 📝 Types de Notes
- `#fleeting` - Captures rapides à traiter
- `#concept` - Idées développées
- `#project` - Notes projet
- `#feature` - Features/fonctionnalités
- `#moc` - Maps of Content
- `#chat-card` - Cartes extraites de chats

#### 📁 Projets
- `#pkm-system` - Projet PKM System
 - `#pkm-system/shortcuts` - Raccourcis
 - `#pkm-system/architecture` - Architecture
 - `#pkm-system/ui` - Interface utilisateur

#### 🏷️ Catégories Techniques
- `#electron` - Technologie Electron
- `#javascript` - Code JavaScript
- `#architecture` - Décisions d'architecture
- `#bug` - Bugs identifiés
- `#refactor` - Refactorings

#### 📍 Status
- `#inbox` - À traiter
- `#active` - En cours
- `#done` - Terminé
- `#archived` - Archivé
- `#broken` - Cassé/non fonctionnel

#### 🎨 Layers (Architecture)
- `#global` - Layer 1 - OS Level
- `#internal` - Layer 2 - App Level
- `#page-specific` - Layer 3 - Page Level

---

## 🔍 RECHERCHES RAPIDES

### Features par Status

**Broken Features:**
```dataview
TABLE status, updated
FROM #feature
WHERE status = \"broken\"
SORT updated DESC
```

**Active Features:**
```dataview
TABLE status, updated
FROM #feature
WHERE status = \"active\"
SORT updated DESC
```

**Planned Features:**
```dataview
TABLE status, created
FROM #feature
WHERE status = \"planned\"
SORT created DESC
```

---

### Shortcuts par Layer

**Global Shortcuts (Layer 1):**
```dataview
TABLE status, updated
FROM #shortcut AND #layer-1
SORT status, updated DESC
```

**Internal Shortcuts (Layer 2):**
```dataview
TABLE status, updated
FROM #shortcut AND #layer-2
SORT status, updated DESC
```

---

### Notes PKM System

**Toutes les notes du projet:**
```dataview
TABLE type, status, updated
FROM #pkm-system
SORT updated DESC
```

**Notes modifiées aujourd'hui:**
```dataview
TABLE type, updated
FROM #pkm-system
WHERE updated = date(today)
SORT updated DESC
```

---

## 📈 STATISTIQUES

### Notes par Type
```dataview
TABLE length(rows) as \"Count\"
FROM \"\"
GROUP BY type
SORT length(rows) DESC
```

### Tags les plus utilisés
```dataview
TABLE length(rows) as \"Utilisations\"
FROM \"\"
FLATTEN file.tags as tag
GROUP BY tag
SORT length(rows) DESC
LIMIT 20
```

---

## 🎯 CONVENTIONS DE NOMMAGE

### Hiérarchie
```
#parent/enfant/petit-enfant
```

**Exemple:**
```
#project/pkm-system/shortcuts
#status/active
#type/feature
```

### Kebab-case
```
#pkm-system ✅
#pkm_system ❌
#PKMSystem ❌
```

### Minuscules
```
#electron ✅
#Electron ❌
```

---

## 🔗 MOCs Liés

- [[MOC Raccourcis]] - Index des raccourcis
- [[MOC Projets]] - Index des projets
- [[MOC Code]] - Index des fichiers code

---

**Dernière mise à jour:** 2025-11-01T15:10:00

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-415-R415-Feature-shortcut]]
- ⬇️ Next: [[Card-417-R417-DataviewLIST-FROM-feature-broken-Scénari]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #python
- #obsidian
- #code
- #automation
