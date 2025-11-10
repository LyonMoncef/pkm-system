---
type: chat-card
parent_export: '[[Export]]'
order: 403
role: assistant
created: '2025-11-10T21:46:11.402508Z'
tags:
- chat-card
- python
- obsidian
- receipts
- code
- automation
attachments_count: 0
---

# 🤖 Message 403 - Assistant

**ID:** msg-403

## 💬 Content


**ID:** msg-403

Orchestrated native Obsidian tag solutions et MOC personnalisé.L'utilisateur veut savoir comment gérer et visualiser les tags dans Obsidian. C'est une question importante pour la navigation dans son PKM. Je dois lui expliquer les différentes méthodes disponibles dans Obsidian pour trouver et filtrer par tags.
Il demande:

Où retrouver tous les tags
S'il y a un MOC pour les tags
Comment voir toutes les notes avec un tag spécifique

Je vais lui donner les solutions natives d'Obsidian + proposer de créer un MOC Tags pour avoir une vue d'ensemble organisée.🏷️ GESTION DES TAGS DANS OBSIDIAN
🔍 MÉTHODES NATIVES OBSIDIAN
1. Tag Pane (Panneau Tags) ⭐ Le plus simple
Activer :

Ctrl+P → \"Tags: Show tag pane\"
Ou Sidebar droite → Icône #

Résultat :

Liste de TOUS tes tags
Avec nombre d'occurrences
Clique sur un tag → Voir toutes les notes

Exemple :
#pkm-system (15)
#feature (8)
#shortcut (5)
#global (3)
#layer-1 (3)

2. Recherche par Tag ⭐⭐
Dans la barre de recherche :
tag:#pkm-system
Ou multiple tags :
tag:#pkm-system tag:#shortcut
Ou hiérarchique :
tag:#feature/shortcut

3. Graph View avec Filtres
View → Open Graph View
Puis filtre par tag :
tag:#pkm-system
Affiche uniquement les notes avec ce tag + leurs connexions.

📋 CRÉER UN MOC TAGS
Fichier : 06_Meta/MOC - Tags System.md
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

🚀 UTILISATION PRATIQUE
Scénario 1 : Voir toutes les features cassées
Méthode rapide :

Ouvre Tag Pane
Clique #broken
Voir toutes les notes

Ou dans une note :
dataviewLIST
FROM #feature AND #broken
```

---

### **Scénario 2 : Voir tous les shortcuts Layer 1**

**Méthode recherche :**
```
tag:#layer-1 tag:#shortcut
Ou Dataview :
dataviewTABLE status
FROM #shortcut AND #layer-1

Scénario 3 : Timeline des notes PKM System
dataviewCALENDAR created
FROM #pkm-system
Ou par jour :
dataviewTABLE created, type
FROM #pkm-system
WHERE created = date(2025-10-24)

✅ ACTIONS IMMÉDIATES
1. Active le Tag Pane

Sidebar droite → Icône #
Pin le panneau pour le garder visible

2. Crée le MOC Tags

Copie le contenu ci-dessus
Place dans 06_Meta/MOC - Tags System.md

3. Test rapide

Cherche tag:#pkm-system
Vois toutes tes notes du projet


🤔 QUESTIONS
Pour affiner ton système de tags :

Tu veux une hiérarchie de tags ?

#project/pkm-system/shortcuts
Ou tags plats : #pkm-system, #shortcuts


Tags par émotion (on en avait parlé) :

#emotion/joie, #emotion/frustration ?
Ou array dans frontmatter : emotions: [joie, excitation] ?


Le MOC Tags te convient ?

À ajuster ?
Queries Dataview à ajouter ?


Dis-moi et on affine ! 🚀

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-402-R402-Orchestrated-native-Obsidian-solutions-p]]
- ⬇️ Next: [[Card-404-R404-Orchestrated-native-Obsidian-solutions-p]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #python
- #obsidian
- #receipts
- #code
- #automation
