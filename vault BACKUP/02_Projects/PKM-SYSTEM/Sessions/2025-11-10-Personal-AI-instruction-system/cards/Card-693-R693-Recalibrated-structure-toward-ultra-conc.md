---
type: chat-card
parent_export: '[[Export]]'
order: 693
role: assistant
created: '2025-11-10T21:46:15.306286Z'
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

# 🤖 Message 693 - Assistant

**ID:** msg-693

## 💬 Content


**ID:** msg-693

Recalibrated structure toward ultra-concise atomic notes with dataview indexing.Ah OK ! Je comprends maintenant. Le but c'est le même principe qu'avec les raccourcis du PKM System :

UN MOC (Map of Content) avec des Dataview queries
UNE NOTE PAR RACCOURCI - atomique, concise, juste l'essentiel

Comme on a fait pour les shortcuts Electron, on va faire pareil pour Tmux et Nvim.
Structure :
04_Resources/Environnement/Tmux/
├── MOC - Tmux & Nvim.md ← Index avec dataview
├── Sessions/
│ ├── tmux new -s.md
│ ├── tmux attach -t.md
│ └── ...
├── Windows/
│ ├── Ctrl+B c - New Window.md
│ └── ...
└── Panes/
 ├── Ctrl+B % - Split Vertical.md
 └── ...

04_Resources/Environnement/Nvim/
├── Navigation/
├── Edition/
└── ...
Ou tout dans le même dossier avec des tags pour filtrer.
Chaque note de raccourci :

Métadonnées (créé, type, tags, shortcut, quicksummary)
Le raccourci
Description ultra courte
Exemple si pertinent
C'est tout !

Le MOC utilise Dataview pour lister tous les raccourcis par catégorie.🎯 AH OK ! MOC + NOTES ATOMIQUES
Exactement comme pour les shortcuts PKM System !

📁 STRUCTURE PROPOSÉE
04_Resources/Environnement/
├── Tmux/
│ ├── MOC - Tmux Shortcuts.md ← Index Dataview
│ ├── tmux new -s - New Session.md
│ ├── tmux attach -t - Attach Session.md
│ ├── tmux ls - List Sessions.md
│ ├── Ctrl+B d - Detach Session.md
│ ├── Ctrl+B c - New Window.md
│ ├── Ctrl+B % - Split Vertical.md
│ └── ...
└── Nvim/
 ├── MOC - Nvim Commands.md ← Index Dataview
 ├── i - Insert Mode.md
 ├── ESC - Normal Mode.md
 ├── dd - Delete Line.md
 ├── yy - Copy Line.md
 └── ...

📝 EXEMPLE: MOC - Tmux Shortcuts
Fichier: 04_Resources/Environnement/Tmux/MOC - Tmux Shortcuts.md
markdown---
created: 2025-11-01T20:10:00
updated: 2025-11-01T20:10:00
type: moc
tags: [moc, tmux, shortcuts, reference, cheatsheet]
related:
 - \"[[MOC - Nvim Commands]]\"
 - \"[[PKM System Workflow]]\"
---

# 🖥️ MOC - Tmux Shortcuts

> **Map of Content** - Index des raccourcis Tmux

---

## 📊 Vue d'Ensemble

### Sessions
```dataview
TABLE shortcut as \"Commande\", quicksummary as \"Action\"
FROM \"04_Resources/Environnement/Tmux\"
WHERE contains(tags, \"tmux-session\")
SORT shortcut ASC
```

### Windows
```dataview
TABLE shortcut as \"Raccourci\", quicksummary as \"Action\"
FROM \"04_Resources/Environnement/Tmux\"
WHERE contains(tags, \"tmux-window\")
SORT shortcut ASC
```

### Panes
```dataview
TABLE shortcut as \"Raccourci\", quicksummary as \"Action\"
FROM \"04_Resources/Environnement/Tmux\"
WHERE contains(tags, \"tmux-pane\")
SORT shortcut ASC
```

### Copy Mode
```dataview
TABLE shortcut as \"Raccourci\", quicksummary as \"Action\"
FROM \"04_Resources/Environnement/Tmux\"
WHERE contains(tags, \"tmux-copy\")
SORT shortcut ASC
```

---

## 🔗 Liens

- [[MOC - Nvim Commands]] - Commandes Neovim
- [[PKM System Workflow]] - Workflow complet
- [[Ubuntu Setup]] - Configuration

---

**Dernière mise à jour:** 2025-11-01T20:10:00

📝 EXEMPLE: Note de Raccourci Tmux
Fichier: 04_Resources/Environnement/Tmux/Ctrl+B % - Split Vertical.md
markdown---
created: 2025-11-01T20:10:00
updated: 2025-11-01T20:10:00
type: shortcut
tags: [shortcut, tmux, tmux-pane, split]
shortcut: \"Ctrl+B %\"
quicksummary: \"Split vertical du pane actif\"
category: panes
---

# Ctrl+B % - Split Vertical

## Action

Divise le pane actuel verticalement (│).

## Exemple
```
Avant:                  Après Ctrl+B %:
┌──────────────┐       ┌───────┬──────┐
│              │       │       │      │
│    Pane 1    │  →    │ Pane 1│Pane 2│
│              │       │       │      │
└──────────────┘       └───────┴──────┘
```

## Use Case PKM

Éditer note à gauche + git status à droite.

---

**Liens:** [[MOC - Tmux Shortcuts]]

📝 EXEMPLE: Note de Raccourci Nvim
Fichier: 04_Resources/Environnement/Nvim/dd - Delete Line.md
markdown---
created: 2025-11-01T20:10:00
updated: 2025-11-01T20:10:00
type: shortcut
tags: [shortcut, nvim, nvim-edit, delete]
shortcut: \"dd\"
quicksummary: \"Supprimer la ligne courante\"
category: edition
mode: normal
---

# dd - Delete Line

## Action

Supprime la ligne où se trouve le curseur.

## Variantes

- `5dd` - Supprimer 5 lignes
- `dG` - Supprimer jusqu'à la fin du fichier
- `dgg` - Supprimer jusqu'au début du fichier

## Use Case PKM

Nettoyer brouillon de notes rapidement.

---

**Liens:** [[MOC - Nvim Commands]]

🏷️ SYSTÈME DE TAGS
Tmux
yamltags: [shortcut, tmux, tmux-session] # Sessions
tags: [shortcut, tmux, tmux-window] # Windows
tags: [shortcut, tmux, tmux-pane] # Panes
tags: [shortcut, tmux, tmux-copy] # Copy mode
Nvim
yamltags: [shortcut, nvim, nvim-navigation] # Navigation
tags: [shortcut, nvim, nvim-edit] # Édition
tags: [shortcut, nvim, nvim-file] # Fichiers
tags: [shortcut, nvim, nvim-visual] # Visual mode
tags: [shortcut, nvim, nvim-search] # Recherche

🎯 MÉTADONNÉES STANDARD
Pour chaque note de raccourci:
yaml---
created: YYYY-MM-DDTHH:mm:ss
updated: YYYY-MM-DDTHH:mm:ss
type: shortcut
tags: [shortcut, tool, category]
shortcut: \"commande\"
quicksummary: \"Description courte\"
category: nom_categorie
mode: normal|insert|visual|command # (Nvim seulement)
---

✅ ON COMMENCE PAR QUOI ?
Option A: Créer le MOC Tmux + 5 raccourcis les plus utilisés
Option B: Créer le MOC Nvim + 5 commandes les plus utilisées
Option C: Faire les deux MOCs d'abord, notes après
Option D: Je te génère TOUS les raccourcis d'un coup (liste complète)
Quelle option ? Et quels raccourcis en priorité ? 🚀

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-692-R692-Recalibrated-structure-toward-ultra-conc]]
- ⬇️ Next: [[Card-694-R694-Recalibrated-structure-toward-ultra-conc]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #python
- #obsidian
- #receipts
- #code
- #git
- #automation
