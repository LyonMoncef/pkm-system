---
type: chat-card
parent_export: '[[Export]]'
order: 535
role: assistant
created: '2025-11-10T21:46:13.293266Z'
tags:
- chat-card
- python
- obsidian
- receipts
- code
- automation
attachments_count: 0
---

# 🤖 Message 535 - Assistant

**ID:** msg-535

## 💬 Content


**ID:** msg-535

Architected dynamic Dataview queries remplaçant listes statiques par filtres.L'utilisateur veut que je modifie le MOC Raccourcis pour remplacer les listes en dur par des requêtes Dataview dynamiques. Il faut:

Corriger les requêtes dans \"Vue d'Ensemble\" (En développement et Dépréciés ont la même requête, c'est une erreur)
Remplacer les listes manuelles des Layers 1, 2, 3 par des requêtes Dataview qui filtrent selon:

Layer 1: tag \"layer-1\"
Layer 2: tag \"layer-2\"
Layer 3: tag \"layer-3\"
Et les sous-catégories aussi


Je dois créer des requêtes qui:

Filtrent par layer (tags)
Affichent le raccourci, le status, la description
Sont organisées par catégories

Les tags utilisés dans les cartes:

layer-1, layer-2, layer-3
toggle-window, window-management (pour Layer 1)
navigation, help (pour Layer 2)
Les pages spécifiques pour Layer 3

Je vais créer des requêtes LIST ou TABLE selon ce qui est le plus approprié.🎹 MOC - RACCOURCIS PKM SYSTEM (VERSION DATAVIEW)
markdown---
created: 2025-10-24T15:45:00
updated: 2025-11-01T18:45:00
type: moc
tags:
 - pkm-system
 - shortcuts
 - moc
 - index
related:
 - \"[[Architecture PKM System]]\"
 - \"[[Backlog]]\"
 - \"[[Global Shortcuts System]]\"
source: développement pkm-system phase 1.5
---

# 🎹 MOC - Raccourcis PKM System

> **Map of Content** - Index des raccourcis clavier du système

---

## 📊 Vue d'Ensemble

### Raccourcis Actifs
```dataview
TABLE shortcut as \"Raccourci\", quicksummary as \"Description\"
FROM \"02_Projects/PKM-SYSTEM/Shortcuts\"
WHERE type = \"feature\" AND status = \"active\"
SORT shortcut ASC
```

### En Développement
```dataview
TABLE shortcut as \"Raccourci\", quicksummary as \"Description\", priority as \"Priorité\"
FROM \"02_Projects/PKM-SYSTEM/Shortcuts\"
WHERE type = \"feature\" AND status = \"dev\"
SORT priority DESC, shortcut ASC
```

### Cassés
```dataview
TABLE shortcut as \"Raccourci\", quicksummary as \"Description\", priority as \"Priorité\"
FROM \"02_Projects/PKM-SYSTEM/Shortcuts\"
WHERE type = \"feature\" AND status = \"broken\"
SORT priority DESC, shortcut ASC
```

### Partiels
```dataview
TABLE shortcut as \"Raccourci\", quicksummary as \"Description\"
FROM \"02_Projects/PKM-SYSTEM/Shortcuts\"
WHERE type = \"feature\" AND status = \"partial\"
SORT shortcut ASC
```

### Prévus
```dataview
TABLE shortcut as \"Raccourci\", quicksummary as \"Description\"
FROM \"02_Projects/PKM-SYSTEM/Shortcuts\"
WHERE type = \"feature\" AND status = \"planned\"
SORT shortcut ASC
```

### Dépréciés
```dataview
TABLE shortcut as \"Raccourci\", quicksummary as \"Description\"
FROM \"02_Projects/PKM-SYSTEM/Shortcuts\"
WHERE type = \"feature\" AND status = \"deprecated\"
SORT shortcut ASC
```

---

## 🌍 Layer 1 - Global OS Shortcuts

> Raccourcis qui fonctionnent même quand l'app est cachée ou minimisée

### Window Toggle
```dataview
TABLE shortcut as \"Raccourci\", quicksummary as \"Description\", status as \"Status\", priority as \"Priorité\"
FROM \"02_Projects/PKM-SYSTEM/Shortcuts\"
WHERE contains(tags, \"layer-1\") AND contains(tags, \"toggle-window\")
SORT priority DESC, shortcut ASC
```

### Window Management
```dataview
TABLE shortcut as \"Raccourci\", quicksummary as \"Description\", status as \"Status\", priority as \"Priorité\"
FROM \"02_Projects/PKM-SYSTEM/Shortcuts\"
WHERE contains(tags, \"layer-1\") AND contains(tags, \"window-management\")
SORT priority DESC, shortcut ASC
```

**Voir aussi:** [[Global Shortcuts System]] pour la vue complète Layer 1

---

## 🎨 Layer 2 - Internal App Shortcuts

> Raccourcis internes à l'application

### Navigation
```dataview
TABLE shortcut as \"Raccourci\", quicksummary as \"Description\", status as \"Status\"
FROM \"02_Projects/PKM-SYSTEM/Shortcuts\"
WHERE contains(tags, \"layer-2\") AND contains(tags, \"navigation\")
SORT shortcut ASC
```

### Help & UI
```dataview
TABLE shortcut as \"Raccourci\", quicksummary as \"Description\", status as \"Status\"
FROM \"02_Projects/PKM-SYSTEM/Shortcuts\"
WHERE contains(tags, \"layer-2\") AND (contains(tags, \"help\") OR contains(tags, \"ui\"))
SORT shortcut ASC
```

---

## 📄 Layer 3 - Page-Specific Shortcuts

> Raccourcis spécifiques à chaque page

### Capture Page
```dataview
TABLE shortcut as \"Raccourci\", quicksummary as \"Description\", status as \"Status\"
FROM \"02_Projects/PKM-SYSTEM/Shortcuts\"
WHERE contains(tags, \"layer-3\") AND contains(tags, \"capture-page\")
SORT shortcut ASC
```

### Hub Page
```dataview
TABLE shortcut as \"Raccourci\", quicksummary as \"Description\", status as \"Status\"
FROM \"02_Projects/PKM-SYSTEM/Shortcuts\"
WHERE contains(tags, \"layer-3\") AND contains(tags, \"hub-page\")
SORT shortcut ASC
```

### Reference Page
```dataview
TABLE shortcut as \"Raccourci\", quicksummary as \"Description\", status as \"Status\"
FROM \"02_Projects/PKM-SYSTEM/Shortcuts\"
WHERE contains(tags, \"layer-3\") AND contains(tags, \"reference-page\")
SORT shortcut ASC
```

---

## 🧪 Test Shortcuts (À Supprimer)
```dataview
TABLE shortcut as \"Raccourci\", quicksummary as \"Description\"
FROM \"02_Projects/PKM-SYSTEM/Shortcuts\"
WHERE status = \"deprecated\"
SORT shortcut ASC
```

---

## 📋 Actions Prioritaires

### Broken Features par Priorité
```dataview
TASK
FROM \"02_Projects/PKM-SYSTEM/Shortcuts\"
WHERE status = \"broken\"
SORT priority DESC
```

**Tâches manuelles:**
- [ ] Débugger IPC pour global shortcuts
- [ ] Implémenter smartToggle()
- [ ] Tester chaque raccourci global
- [ ] Finaliser navigation Ctrl+1/2/3
- [ ] Fix shortcuts help
- [ ] Supprimer test shortcuts
- [ ] Documenter architecture finale

---

## 🔗 Liens Projet

- [[Architecture PKM System]] - Vue d'ensemble
- [[Global Shortcuts System]] - Détails Layer 1
- [[Backlog]] - Tâches en attente
- [[Phase 1.5 - Refactor]] - Contexte actuel

---

## 📊 Statistiques

### Répartition par Status
```dataview
TABLE length(rows) as \"Nombre\"
FROM \"02_Projects/PKM-SYSTEM/Shortcuts\"
WHERE type = \"feature\"
GROUP BY status
SORT length(rows) DESC
```

### Répartition par Layer
```dataview
TABLE length(rows) as \"Nombre\"
FROM \"02_Projects/PKM-SYSTEM/Shortcuts\"
WHERE type = \"feature\"
FLATTEN file.tags as layer
WHERE contains(layer, \"layer-\")
GROUP BY layer
SORT layer ASC
```

### Dernières Modifications
```dataview
TABLE shortcut as \"Raccourci\", status as \"Status\", updated as \"Modifié\"
FROM \"02_Projects/PKM-SYSTEM/Shortcuts\"
WHERE type = \"feature\"
SORT updated DESC
LIMIT 10
```

---

**Légende Status:**
- ✅ ACTIVE - Fonctionne parfaitement
- 🟡 PARTIAL - Fonctionne partiellement
- ❌ BROKEN - Ne fonctionne pas
- 🔵 PLANNED - Prévu mais pas implémenté
- 🔧 DEV - En développement
- 🗑️ DEPRECATED - À supprimer

---

**Dernière mise à jour:** 2025-11-01T18:45:00
**Maintenance:** Auto-update via Dataview

🏷️ TAGS REQUIS POUR LES CARTES
Pour que les queries Dataview fonctionnent, chaque carte de raccourci doit avoir :
Tags obligatoires:
yamltags: [feature, shortcut, pkm-system, layer-X, ...]
Tags par Layer:
Layer 1:
yamltags: [..., layer-1, toggle-window] # ou window-management
Layer 2:
yamltags: [..., layer-2, navigation] # ou help, ou ui
Layer 3:
yamltags: [..., layer-3, capture-page] # ou hub-page, ou reference-page

📝 MISE À JOUR DES 3 CARTES EXISTANTES
Ctrl+Shift+Space (OK, déjà bon)
yamltags: [feature, shortcut, pkm-system, global, layer-1, toggle-window]
Ctrl+Shift+F (OK, déjà bon)
yamltags: [feature, shortcut, pkm-system, global, layer-1, toggle-window]
Ctrl+Shift+H (OK, déjà bon)
yamltags: [feature, shortcut, pkm-system, global, layer-1, toggle-window]

✅ AVANTAGES DE CETTE VERSION
Automatique:

✅ Plus besoin de mettre à jour manuellement les listes
✅ Ajoute une nouvelle carte → apparaît automatiquement
✅ Change un status → se met à jour tout seul

Vue d'ensemble:

✅ Stats en temps réel
✅ Tri par priorité, status, date
✅ Filtres par layer, catégorie, status

Maintenable:

✅ Une seule source de vérité (les cartes individuelles)
✅ Pas de duplication
✅ Consistance garantie


Remplace ton MOC actuel par celui-ci et toutes les listes seront dynamiques ! 🚀

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-534-R534-Architected-dynamic-Dataview-queries-rem]]
- ⬇️ Next: [[Card-536-R536-Architected-dynamic-Dataview-queries-rem]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #python
- #obsidian
- #receipts
- #code
- #automation
