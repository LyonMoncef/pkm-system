---
type: chat-card
parent_export: '[[Export]]'
order: 711
role: assistant
created: '2025-11-10T21:46:15.653814Z'
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

# 🤖 Message 711 - Assistant

**ID:** msg-711

## 💬 Content


**ID:** msg-711

Architected Tmux guide with five essential shortcuts.L'utilisateur veut l'option A: Créer le MOC Tmux + 5 raccourcis les plus utilisés.
Je vais créer:

Le MOC - Tmux Shortcuts.md
5 notes de raccourcis les plus utilisés (je vais choisir les plus courants)

Les 5 plus utilisés pour un workflow PKM seraient probablement:

tmux new -s - New Session (créer session)
tmux attach -t - Attach Session (réattacher)
Ctrl+B d - Detach Session (détacher)
Ctrl+B % - Split Vertical (split vertical)
Ctrl+B \" - Split Horizontal (split horizontal)

Je vais faire des notes ultra concises comme demandé.🚀 CRÉATION MOC TMUX + 5 RACCOURCIS
📝 FICHIER 1: MOC - Tmux Shortcuts
Fichier: 04_Resources/Environnement/Tmux/MOC - Tmux Shortcuts.md
markdown---
created: 2025-11-01T20:15:00
updated: 2025-11-01T20:15:00
type: moc
tags: [moc, tmux, shortcuts, reference, cheatsheet, terminal]
related:
 - \"[[MOC - Nvim Commands]]\"
 - \"[[PKM System Workflow]]\"
 - \"[[Ubuntu Setup]]\"
---

# 🖥️ MOC - Tmux Shortcuts

> **Map of Content** - Index des raccourcis Tmux

---

## 📊 Vue d'Ensemble

### Sessions
```dataview
TABLE shortcut as \"Commande\", quicksummary as \"Action\"
FROM \"04_Resources/Environnement/Tmux\"
WHERE contains(tags, \"tmux-session\") AND type = \"shortcut\"
SORT shortcut ASC
```

### Windows
```dataview
TABLE shortcut as \"Raccourci\", quicksummary as \"Action\"
FROM \"04_Resources/Environnement/Tmux\"
WHERE contains(tags, \"tmux-window\") AND type = \"shortcut\"
SORT shortcut ASC
```

### Panes
```dataview
TABLE shortcut as \"Raccourci\", quicksummary as \"Action\"
FROM \"04_Resources/Environnement/Tmux\"
WHERE contains(tags, \"tmux-pane\") AND type = \"shortcut\"
SORT shortcut ASC
```

### Copy Mode
```dataview
TABLE shortcut as \"Raccourci\", quicksummary as \"Action\"
FROM \"04_Resources/Environnement/Tmux\"
WHERE contains(tags, \"tmux-copy\") AND type = \"shortcut\"
SORT shortcut ASC
```

### Autres
```dataview
TABLE shortcut as \"Raccourci\", quicksummary as \"Action\"
FROM \"04_Resources/Environnement/Tmux\"
WHERE contains(tags, \"tmux\") AND type = \"shortcut\" AND !contains(tags, \"tmux-session\") AND !contains(tags, \"tmux-window\") AND !contains(tags, \"tmux-pane\") AND !contains(tags, \"tmux-copy\")
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
1. [[tmux new -s - New Session]] - Créer session \"pkm\"
2. [[Ctrl+B % - Split Vertical]] - Split éditeur/git
3. [[Ctrl+B \" - Split Horizontal]] - Split pour terminal
4. [[Ctrl+B d - Detach Session]] - Détacher et continuer plus tard
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

📝 FICHIER 2: tmux new -s
Fichier: 04_Resources/Environnement/Tmux/tmux new -s - New Session.md
markdown---
created: 2025-11-01T20:15:00
updated: 2025-11-01T20:15:00
type: shortcut
tags: [shortcut, tmux, tmux-session, session-management]
shortcut: \"tmux new -s nom\"
quicksummary: \"Créer une nouvelle session nommée\"
category: sessions
---

# tmux new -s - New Session

## Action

Crée une nouvelle session tmux avec un nom spécifique.

## Syntaxe
```bash
tmux new -s nom_session
```

## Exemples
```bash
tmux new -s pkm        # Session pour notes PKM
tmux new -s dev        # Session développement
tmux new -s server     # Session monitoring serveur
```

## Use Case PKM
```bash
tmux new -s pkm
cd ~/vault
nvim .
```

---

**Liens:** [[MOC - Tmux Shortcuts]] | [[tmux attach -t - Attach Session]]

📝 FICHIER 3: tmux attach -t
Fichier: 04_Resources/Environnement/Tmux/tmux attach -t - Attach Session.md
markdown---
created: 2025-11-01T20:15:00
updated: 2025-11-01T20:15:00
type: shortcut
tags: [shortcut, tmux, tmux-session, session-management]
shortcut: \"tmux attach -t nom\"
quicksummary: \"Réattacher une session existante\"
category: sessions
---

# tmux attach -t - Attach Session

## Action

Réattache (reconnecte) à une session tmux existante.

## Syntaxe
```bash
tmux attach -t nom_session
# ou raccourci:
tmux a -t nom_session
```

## Exemples
```bash
tmux attach -t pkm     # Réattacher session pkm
tmux a -t dev          # Raccourci pour attach
tmux a                 # Attache dernière session
```

## Use Case PKM
```bash
# Morning workflow
tmux attach -t pkm     # Reprendre où tu en étais hier
```

---

**Liens:** [[MOC - Tmux Shortcuts]] | [[tmux new -s - New Session]] | [[Ctrl+B d - Detach Session]]

📝 FICHIER 4: Ctrl+B d
Fichier: 04_Resources/Environnement/Tmux/Ctrl+B d - Detach Session.md
markdown---
created: 2025-11-01T20:15:00
updated: 2025-11-01T20:15:00
type: shortcut
tags: [shortcut, tmux, tmux-session, session-management]
shortcut: \"Ctrl+B d\"
quicksummary: \"Détacher de la session (continue en background)\"
category: sessions
---

# Ctrl+B d - Detach Session

## Action

Détache de la session actuelle. La session continue de tourner en background.

## Séquence
```
1. Ctrl+B    (prefix)
2. d         (detach)
```

## Résultat
```
[detached (from session pkm)]
```

La session reste active et peut être réattachée plus tard avec [[tmux attach -t - Attach Session]].

## Use Case PKM
```bash
# En train d'éditer des notes
Ctrl+B d                # Détacher session
# Faire autre chose...
tmux attach -t pkm      # Reprendre plus tard
```

---

**Liens:** [[MOC - Tmux Shortcuts]] | [[tmux attach -t - Attach Session]]

📝 FICHIER 5: Ctrl+B %
Fichier: 04_Resources/Environnement/Tmux/Ctrl+B % - Split Vertical.md
markdown---
created: 2025-11-01T20:15:00
updated: 2025-11-01T20:15:00
type: shortcut
tags: [shortcut, tmux, tmux-pane, split, layout]
shortcut: \"Ctrl+B %\"
quicksummary: \"Split vertical du pane actif\"
category: panes
---

# Ctrl+B % - Split Vertical

## Action

Divise le pane actuel verticalement (│).

## Séquence
```
1. Ctrl+B    (prefix)
2. %         (split vertical)
```

## Résultat
```
Avant:                  Après:
┌──────────────┐       ┌───────┬──────┐
│              │       │       │      │
│    Pane      │  →    │ Pane 1│Pane 2│
│              │       │       │      │
└──────────────┘       └───────┴──────┘
```

## Navigation

Utiliser [[Ctrl+B arrow - Navigate Panes]] pour se déplacer entre les panes.

## Use Case PKM
```
┌─────────────┬────────┐
│   Nvim      │  Git   │
│   Notes     │ Status │
└─────────────┴────────┘
```

---

**Liens:** [[MOC - Tmux Shortcuts]] | [[Ctrl+B \" - Split Horizontal]] | [[Ctrl+B z - Toggle Fullscreen]]

📝 FICHIER 6: Ctrl+B \"
Fichier: 04_Resources/Environnement/Tmux/Ctrl+B \" - Split Horizontal.md
markdown---
created: 2025-11-01T20:15:00
updated: 2025-11-01T20:15:00
type: shortcut
tags: [shortcut, tmux, tmux-pane, split, layout]
shortcut: 'Ctrl+B \"'
quicksummary: \"Split horizontal du pane actif\"
category: panes
---

# Ctrl+B \" - Split Horizontal

## Action

Divise le pane actuel horizontalement (─).

## Séquence
```
1. Ctrl+B    (prefix)
2. \"         (split horizontal)
```

## Résultat
```
Avant:                  Après:
┌──────────────┐       ┌──────────────┐
│              │       │   Pane 1     │
│    Pane      │  →    ├──────────────┤
│              │       │   Pane 2     │
└──────────────┘       └──────────────┘
```

## Navigation

Utiliser [[Ctrl+B arrow - Navigate Panes]] pour se déplacer entre les panes.

## Use Case PKM
```
┌──────────────┐
│   Nvim       │
│   Notes      │
├──────────────┤
│   Terminal   │
│   (git/scripts)
└──────────────┘
```

---

**Liens:** [[MOC - Tmux Shortcuts]] | [[Ctrl+B % - Split Vertical]] | [[Ctrl+B z - Toggle Fullscreen]]
```

---

## ✅ RÉSUMÉ DES 6 FICHIERS CRÉÉS

### MOC (1)
- ✅ MOC - Tmux Shortcuts.md

### Raccourcis Sessions (3)
- ✅ tmux new -s - New Session.md
- ✅ tmux attach -t - Attach Session.md
- ✅ Ctrl+B d - Detach Session.md

### Raccourcis Panes (2)
- ✅ Ctrl+B % - Split Vertical.md
- ✅ Ctrl+B \" - Split Horizontal.md

---

## 📁 STRUCTURE FINALE
```
04_Resources/Environnement/Tmux/
├── MOC - Tmux Shortcuts.md
├── tmux new -s - New Session.md
├── tmux attach -t - Attach Session.md
├── Ctrl+B d - Detach Session.md
├── Ctrl+B % - Split Vertical.md
└── Ctrl+B \" - Split Horizontal.md

🎯 PROCHAINES ÉTAPES
Option A: Continuer avec 5 raccourcis Tmux supplémentaires (Windows, Navigation)
Option B: Passer à Nvim - Créer MOC + 5 commandes les plus utilisées
Option C: Créer TOUS les raccourcis Tmux d'un coup (liste complète ~20)
Option D: Autre chose
Ton choix ? 🚀Réessayer

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-710-R710-Yaml-created-YYYY-DDTHH-updated]]
- ⬇️ Next: [[Card-712-R712-Architected-Tmux-guide-with-five]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #python
- #obsidian
- #receipts
- #code
- #git
- #automation
