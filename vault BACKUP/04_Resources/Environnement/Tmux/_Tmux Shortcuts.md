---
created: 2025-11-01 20:15:00
updated: '2025-11-02T04:34:51'
type: moc
tags:
- cheatsheet
- moc
- reference
- shortcut
- terminal
- tmux
related:
- '[[MOC - Nvim Commands]]'
- '[[PKM System Workflow]]'
- '[[Ubuntu Setup]]'
---

# 🖥️ MOC - Tmux Shortcuts

> **Map of Content** - Index des raccourcis Tmux

---

## 📊 Vue d'Ensemble

### Sessions
```dataview
TABLE shortcut as "Commande", quicksummary as "Action"
FROM "04_Resources/Environnement/Tmux"
WHERE contains(tags, "tmux-session") AND type = "shortcut"
SORT shortcut ASC
```

### Windows
```dataview
TABLE shortcut as "Raccourci", quicksummary as "Action"
FROM "04_Resources/Environnement/Tmux"
WHERE contains(tags, "tmux-window") AND type = "shortcut"
SORT shortcut ASC
```

### Panes
```dataview
TABLE shortcut as "Raccourci", quicksummary as "Action"
FROM "04_Resources/Environnement/Tmux"
WHERE contains(tags, "tmux-pane") AND type = "shortcut"
SORT shortcut ASC
```

### Copy Mode
```dataview
TABLE shortcut as "Raccourci", quicksummary as "Action"
FROM "04_Resources/Environnement/Tmux"
WHERE contains(tags, "tmux-copy") AND type = "shortcut"
SORT shortcut ASC
```

### Autres
```dataview
TABLE shortcut as "Raccourci", quicksummary as "Action"
FROM "04_Resources/Environnement/Tmux"
WHERE contains(tags, "tmux") AND type = "shortcut" AND !contains(tags, "tmux-session") AND !contains(tags, "tmux-window") AND !contains(tags, "tmux-pane") AND !contains(tags, "tmux-copy")
SORT shortcut ASC
```

---

## 🎯 Workflow PKM Recommandé

**Session dédiée:**
```bash
tmux new -s pkm
```

**Layout 3 panes:**
```
┌─────────────────┬──────────┐
│   Nvim Editor   │   Git    │
│   (notes)       │  Status  │
├─────────────────┴──────────┤
│     Terminal (scripts)     │
└────────────────────────────┘
```

**Commandes:**
1. [[tmux new -s - New Session]] - Créer session "pkm"
2. [[Ctrl Space % - Split Vertical]] - Split éditeur/git
3. [[Ctrl Space - Split Horizontal]] - Split pour terminal
4. [[Ctrl d - Detach Session]] - Détacher et continuer plus tard
5. [[tmux attach -t - Attach Session]] - Réattacher session

---

## 📚 Ressources

- [Tmux Manual](https://man.openbsd.org/tmux.1)
- [Tmux Cheat Sheet](https://tmuxcheatsheet.com/)
- [Tmux Plugins](https://github.com/tmux-plugins)

---

## 🔗 Liens

- [[MOC - Nvim Commands]] - Commandes Neovim
- [[PKM System Workflow]] - Workflow complet
- [[Ubuntu Setup]] - Configuration système

---

**Dernière mise à jour:** 2025-11-01T20:15:00  
**Maintenance:** Ajouter raccourcis au fur et à mesure