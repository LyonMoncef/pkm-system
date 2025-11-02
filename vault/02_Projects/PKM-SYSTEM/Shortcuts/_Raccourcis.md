---
created: 2025-10-24 15:45:00
updated: 2025-11-02T04:34:51
type: moc
tags:
  - index
  - moc
  - pkm-system
  - shortcut
related:
  - "[[Architecture PKM System]]"
  - "[[02_Projects/PKM-SYSTEM/BackLog/Backlog]]"
  - "[[1-Global Shortcuts System]]"
source: développement pkm-system phase 1.5
---

# 🎹 MOC - Raccourcis PKM System

> **Map of Content** - Index des raccourcis clavier du système
---
## 📊 Vue d'Ensemble

### **Raccourcis actifs:** 
```dataview
LIST 
FROM "02_Projects/Shortcuts"
WHERE contains(tags,"shortcut") and type="feature"
```
### **En développement:** 
```dataview
TABLE shortcut, quicksummary 
FROM "02_Projects/Shortcuts"
WHERE type = "feature" AND status = "dev" 
SORT priority DESC, shortcut ASC
```
### **Cassés:** 
```dataview
TABLE shortcut as "Raccourci", quicksummary as "Description", priority as "Priorité"
FROM "02_Projects/Shortcuts"
WHERE type = "feature" AND status = "broken" 
SORT priority DESC, shortcut ASC

```
### **Dépréciés:** 
```dataview
TABLE shortcut as "Raccourci", quicksummary as "Description" 
FROM "02_Projects/Shortcuts"
WHERE type = "feature" AND status = "deprecated" SORT shortcut ASC
```

---

## 🌍 Layer 1 - Global OS Shortcuts

> Raccourcis qui fonctionnent même quand l'app est cachée ou minimisée

### Window Toggle
```dataview
TABLE shortcut as "Raccourci", quicksummary as "Description", status as "Status", priority as "Priorité"
FROM #shortcut AND #layer-1 AND #toggle-window
SORT priority DESC, shortcut ASC
```

### Window Management
```dataview
TABLE shortcut as "Raccourci", quicksummary as "Description", status as "Status", priority as "Priorité"
FROM #shortcut AND #layer-1 AND #window-management
SORT priority DESC, shortcut ASC
```

**Voir aussi:** [[1-Global Shortcuts System]] pour la vue complète Layer 1

---

## 🎨 Layer 2 - Internal App Shortcuts

> Raccourcis internes à l'application

### Navigation
```dataview
TABLE shortcut as "Raccourci", quicksummary as "Description", status as "Status"
FROM #shortcut AND #layer-2 AND #navigation
SORT shortcut ASC
```

### Help & UI
```dataview
TABLE shortcut as "Raccourci", quicksummary as "Description", status as "Status"
FROM #shortcut AND #layer-2
WHERE contains(tags, "help") OR contains(tags, "ui")
SORT shortcut ASC
```

---

## 📄 Layer 3 - Page-Specific Shortcuts

> Raccourcis spécifiques à chaque page

### Capture Page
```dataview
TABLE shortcut as "Raccourci", quicksummary as "Description", status as "Status"
FROM #shortcut AND #layer-3 AND #capture-page
SORT shortcut ASC
```

### Hub Page
```dataview
TABLE shortcut as "Raccourci", quicksummary as "Description", status as "Status"
FROM #shortcut AND #layer-3 AND #hub-page
SORT shortcut ASC
```

### Reference Page
```dataview
TABLE shortcut as "Raccourci", quicksummary as "Description", status as "Status"
FROM #shortcut AND #layer-3 AND #reference-page
SORT shortcut ASC
```

---

## 🧪 Test Shortcuts (À Supprimer)
```dataview
TABLE shortcut as "Raccourci", quicksummary as "Description"
FROM #shortcut
WHERE status = "deprecated"
SORT shortcut ASC
```

---

## 📋 Actions Prioritaires

### Features Cassées par Priorité
```dataview
TABLE shortcut as "Raccourci", quicksummary as "Description", priority as "Priorité", updated as "MAJ"
FROM #shortcut
WHERE status = "broken"
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
- [[1-Global Shortcuts System]] - Détails Layer 1
- [[02_Projects/PKM-SYSTEM/BackLog/Backlog]] - Tâches en attente
- [[Phase 1.5 - Refactor]] - Contexte actuel

---

## 📊 Statistiques

### Répartition par Status
```dataview
TABLE rows.file.link as "Raccourcis", length(rows) as "Nombre"
FROM #shortcut
WHERE type = "feature"
GROUP BY status
SORT length(rows) DESC
```

### Répartition par Layer
```dataview
TABLE length(rows) as "Nombre"
FROM #shortcut
WHERE type = "feature" AND (contains(tags, "layer-1") OR contains(tags, "layer-2") OR contains(tags, "layer-3"))
FLATTEN file.tags as layer
WHERE startswith(layer, "layer-")
GROUP BY layer
SORT layer ASC
```

### Dernières Modifications
```dataview
TABLE shortcut as "Raccourci", status as "Status", updated as "Modifié"
FROM #shortcut
WHERE type = "feature"
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

**Dernière mise à jour:** 2025-11-01T19:00:00  
**Maintenance:** Auto-update via Dataview (basé sur tags)