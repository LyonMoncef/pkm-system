---
type: chat-card
parent_export: '[[Export]]'
order: 598
role: assistant
created: '2025-11-10T21:46:14.073686Z'
tags:
- chat-card
- python
- obsidian
- receipts
- code
- automation
attachments_count: 0
---

# 🤖 Message 598 - Assistant

**ID:** msg-598

## 💬 Content


**ID:** msg-598

markdown---
created: 2025-10-24T15:45:00
updated: 2025-11-01T19:15:00
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
FROM \"02_Projects/PKM-SYSTEM\"
WHERE contains(file.folder, \"Shortcuts\") AND type = \"feature\" AND status = \"active\"
SORT shortcut ASC
```

### En Développement
```dataview
TABLE shortcut as \"Raccourci\", quicksummary as \"Description\", priority as \"Priorité\"
FROM \"02_Projects/PKM-SYSTEM\"
WHERE contains(file.folder, \"Shortcuts\") AND type = \"feature\" AND status = \"dev\"
SORT priority DESC, shortcut ASC
```

### Cassés
```dataview
TABLE shortcut as \"Raccourci\", quicksummary as \"Description\", priority as \"Priorité\"
FROM \"02_Projects/PKM-SYSTEM\"
WHERE contains(file.folder, \"Shortcuts\") AND type = \"feature\" AND status = \"broken\"
SORT priority DESC, shortcut ASC
```

### Partiels
```dataview
TABLE shortcut as \"Raccourci\", quicksummary as \"Description\"
FROM \"02_Projects/PKM-SYSTEM\"
WHERE contains(file.folder, \"Shortcuts\") AND type = \"feature\" AND status = \"partial\"
SORT shortcut ASC
```

### Prévus
```dataview
TABLE shortcut as \"Raccourci\", quicksummary as \"Description\"
FROM \"02_Projects/PKM-SYSTEM\"
WHERE contains(file.folder, \"Shortcuts\") AND type = \"feature\" AND status = \"planned\"
SORT shortcut ASC
```

### Dépréciés
```dataview
TABLE shortcut as \"Raccourci\", quicksummary as \"Description\"
FROM \"02_Projects/PKM-SYSTEM\"
WHERE contains(file.folder, \"Shortcuts\") AND type = \"feature\" AND status = \"deprecated\"
SORT shortcut ASC
```

---

## 🌍 Layer 1 - Global OS Shortcuts

> Raccourcis qui fonctionnent même quand l'app est cachée ou minimisée

### Window Toggle
```dataview
TABLE shortcut as \"Raccourci\", quicksummary as \"Description\", status as \"Status\", priority as \"Priorité\"
FROM \"02_Projects/PKM-SYSTEM\"
WHERE contains(file.folder, \"Shortcuts\") AND contains(tags, \"layer-1\") AND contains(tags, \"toggle-window\")
SORT priority DESC, shortcut ASC
```

### Window Management
```dataview
TABLE shortcut as \"Raccourci\", quicksummary as \"Description\", status as \"Status\", priority as \"Priorité\"
FROM \"02_Projects/PKM-SYSTEM\"
WHERE contains(file.folder, \"Shortcuts\") AND contains(tags, \"layer-1\") AND contains(tags, \"window-management\")
SORT priority DESC, shortcut ASC
```

**Voir aussi:** [[Global Shortcuts System]] pour la vue complète Layer 1

---

## 🎨 Layer 2 - Internal App Shortcuts

> Raccourcis internes à l'application

### Navigation
```dataview
TABLE shortcut as \"Raccourci\", quicksummary as \"Description\", status as \"Status\"
FROM \"02_Projects/PKM-SYSTEM\"
WHERE contains(file.folder, \"Shortcuts\") AND contains(tags, \"layer-2\") AND contains(tags, \"navigation\")
SORT shortcut ASC
```

### Help & UI
```dataview
TABLE shortcut as \"Raccourci\", quicksummary as \"Description\", status as \"Status\"
FROM \"02_Projects/PKM-SYSTEM\"
WHERE contains(file.folder, \"Shortcuts\") AND contains(tags, \"layer-2\") AND (contains(tags, \"help\") OR contains(tags, \"ui\"))
SORT shortcut ASC
```

---

## 📄 Layer 3 - Page-Specific Shortcuts

> Raccourcis spécifiques à chaque page

### Capture Page
```dataview
TABLE shortcut as \"Raccourci\", quicksummary as \"Description\", status as \"Status\"
FROM \"02_Projects/PKM-SYSTEM\"
WHERE contains(file.folder, \"Shortcuts\") AND contains(tags, \"layer-3\") AND contains(tags, \"capture-page\")
SORT shortcut ASC
```

### Hub Page
```dataview
TABLE shortcut as \"Raccourci\", quicksummary as \"Description\", status as \"Status\"
FROM \"02_Projects/PKM-SYSTEM\"
WHERE contains(file.folder, \"Shortcuts\") AND contains(tags, \"layer-3\") AND contains(tags, \"hub-page\")
SORT shortcut ASC
```

### Reference Page
```dataview
TABLE shortcut as \"Raccourci\", quicksummary as \"Description\", status as \"Status\"
FROM \"02_Projects/PKM-SYSTEM\"
WHERE contains(file.folder, \"Shortcuts\") AND contains(tags, \"layer-3\") AND contains(tags, \"reference-page\")
SORT shortcut ASC
```

---

## 🧪 Test Shortcuts (À Supprimer)
```dataview
TABLE shortcut as \"Raccourci\", quicksummary as \"Description\"
FROM \"02_Projects/PKM-SYSTEM\"
WHERE contains(file.folder, \"Shortcuts\") AND status = \"deprecated\"
SORT shortcut ASC
```

---

## 📋 Actions Prioritaires

### Features Cassées par Priorité
```dataview
TABLE shortcut as \"Raccourci\", quicksummary as \"Description\", priority as \"Priorité\", updated as \"MAJ\"
FROM \"02_Projects/PKM-SYSTEM\"
WHERE contains(file.folder, \"Shortcuts\") AND status = \"broken\"
SORT priority DESC, updated DESC
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
TABLE rows.file.link as \"Raccourcis\", length(rows) as \"Nombre\"
FROM \"02_Projects/PKM-SYSTEM\"
WHERE contains(file.folder, \"Shortcuts\") AND type = \"feature\"
GROUP BY status
SORT length(rows) DESC
```

### Répartition par Layer
```dataview
TABLE length(rows) as \"Nombre\"
FROM \"02_Projects/PKM-SYSTEM\"
WHERE contains(file.folder, \"Shortcuts\") AND type = \"feature\"
FLATTEN file.tags as layer
WHERE startswith(layer, \"layer-\")
GROUP BY layer
SORT layer ASC
```

### Dernières Modifications
```dataview
TABLE shortcut as \"Raccourci\", status as \"Status\", updated as \"Modifié\"
FROM \"02_Projects/PKM-SYSTEM\"
WHERE contains(file.folder, \"Shortcuts\") AND type = \"feature\"
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

**Dernière mise à jour:** 2025-11-01T19:15:00
**Maintenance:** Auto-update via Dataview (dossier + tags)

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-597-R597-DataviewTABLE-shortcut-Raccourci-quicksu]]
- ⬇️ Next: [[Card-599-R599-DataviewFROM-SYSTEM-Shortcuts-Exact-frag]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #python
- #obsidian
- #receipts
- #code
- #automation
