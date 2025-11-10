---
type: chat-card
parent_export: '[[Export]]'
order: 675
role: assistant
created: '2025-11-10T21:46:15.033720Z'
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

# 🤖 Message 675 - Assistant

**ID:** msg-675

## 💬 Content


**ID:** msg-675

Restructured cheatsheet metadata et classifié comme ressource documentaire.L'utilisateur veut que je traite cette note Tmux & Nvim Cheatsheet. Regardons sa structure actuelle :

C'est une cheatsheet (aide-mémoire)
Tags : #cheatsheet #tmux #nvim #terminal
Date de création : 2025-10-18
Pinned: true
Contenu : Commandes Tmux et Nvim

Ce qu'il faut faire :

Mettre à jour le frontmatter avec le nouveau standard (date+heure, type, etc.)
Ajuster les tags selon notre système
Ajouter les métadonnées appropriées
Peut-être restructurer légèrement si nécessaire
Garder le contenu utile

Type de note : Ce n'est ni une feature, ni un concept, ni un projet... C'est une resource (référence/documentation)
Tags à utiliser :

resource (type)
cheatsheet (catégorie)
tmux, nvim, terminal (sujets)
reference (pour indiquer que c'est une référence)

Structure :

Doit être dans 04_Resources/
C'est une note de référence rapide
Le contenu est bon, juste besoin de standardiser les métadonnées

Liens possibles :

Vers d'autres notes de setup/config si elles existent
Vers la note sur le PKM system workflow
📝 REFACTO: Tmux & Nvim Cheatsheet
📋 ANALYSE
Type: Resource / Cheatsheet
Emplacement actuel: 04_Resources/Tmux-Nvim-Cheatsheet.md
But: Aide-mémoire pour commandes Tmux et Nvim

✅ VERSION REFACTORISÉE
markdown---
created: 2025-10-18T10:00:00
updated: 2025-11-01T20:00:00
type: resource
tags: [resource, cheatsheet, tmux, nvim, terminal, reference, linux, ubuntu]
pinned: true
related:
 - \"[[PKM System Workflow]]\"
 - \"[[Ubuntu Setup]]\"
source: \"configuration personnelle\"
---

# 🖥️ Tmux & Nvim Cheatsheet

> **Aide-mémoire** - Commandes essentielles Tmux et Neovim pour workflow PKM

---

## 🎯 Context d'Utilisation

**Workflow:** Édition notes PKM via Tmux + Nvim sous Ubuntu
**Sync:** Modifications commitées vers NAS, visualisation via Obsidian Windows

---

## 🖥️ Tmux - Terminal Multiplexer

### Sessions (Workspaces)

| Commande | Action |
|----------|--------|
| `tmux new -s pkm` | Nouvelle session \"pkm\" |
| `tmux attach -t pkm` | Attacher session \"pkm\" |
| `tmux ls` | Lister toutes les sessions |
| `Ctrl+B d` | Détacher session (session continue en background) |
| `tmux kill-session -t pkm` | Tuer une session |
| `Ctrl+B s` | Liste interactive des sessions |

**Use case PKM:**
```bash
# Session dédiée PKM
tmux new -s pkm

# Détacher et continuer plus tard
Ctrl+B d

# Réattacher
tmux attach -t pkm
```

---

### Windows (Tabs)

| Commande | Action |
|----------|--------|
| `Ctrl+B c` | Nouvelle fenêtre |
| `Ctrl+B n` | Fenêtre suivante |
| `Ctrl+B p` | Fenêtre précédente |
| `Ctrl+B [0-9]` | Aller à la fenêtre N |
| `Ctrl+B ,` | Renommer fenêtre |
| `Ctrl+B &` | Fermer fenêtre |
| `Ctrl+B w` | Liste interactive des fenêtres |

**Use case PKM:**
```
Window 0: Notes (nvim vault)
Window 1: Git (commits)
Window 2: Scripts (automation)
```

---

### Panes (Splits)

| Commande | Action |
|----------|--------|
| `Ctrl+B %` | Split vertical (│) |
| `Ctrl+B \"` | Split horizontal (─) |
| `Ctrl+B ←→↑↓` | Naviguer entre panes |
| `Ctrl+B z` | Toggle fullscreen pane |
| `Ctrl+B x` | Fermer pane |
| `Ctrl+B {` | Déplacer pane à gauche |
| `Ctrl+B }` | Déplacer pane à droite |
| `Ctrl+B Space` | Changer layout |
| `Ctrl+B Ctrl+←→` | Resize pane |

**Layout PKM recommandé:**
```
┌─────────────────┬──────────┐
│                 │          │
│   Nvim Editor   │   Git    │
│   (main notes)  │  Status  │
│                 │          │
├─────────────────┴──────────┤
│     Terminal (scripts)     │
└────────────────────────────┘

Ctrl+B %  → Split vertical
Ctrl+B \"  → Split horizontal sur droite
```

---

### Copy Mode (Scroll & Copy)

| Commande | Action |
|----------|--------|
| `Ctrl+B [` | Entrer en copy mode |
| `q` | Quitter copy mode |
| `Space` | Commencer sélection |
| `Enter` | Copier sélection |
| `Ctrl+B ]` | Coller |
| `/` | Rechercher en avant |
| `?` | Rechercher en arrière |

**Use case:**
- Scroll dans l'historique terminal
- Copier output de commandes
- Rechercher dans logs

---

## ⚡ Neovim - Text Editor

### Modes

| Mode | Touche | Description |
|------|--------|-------------|
| **Normal** | `ESC` | Navigation et commandes |
| **Insert** | `i` | Édition texte |
| **Visual** | `v` | Sélection |
| **Command** | `:` | Commandes Vim |

---

### Navigation (Normal Mode)

#### Mouvements de Base

| Commande | Action |
|----------|--------|
| `h j k l` | ← ↓ ↑ → |
| `w` | Mot suivant (début) |
| `e` | Mot suivant (fin) |
| `b` | Mot précédent |
| `0` | Début de ligne |
| `$` | Fin de ligne |
| `gg` | Début fichier |
| `G` | Fin fichier |
| `:[num]` | Aller ligne [num] |

#### Navigation Avancée

| Commande | Action |
|----------|--------|
| `{` | Paragraphe précédent |
| `}` | Paragraphe suivant |
| `Ctrl+d` | Descendre ½ page |
| `Ctrl+u` | Monter ½ page |
| `%` | Aller à la parenthèse/bracket correspondante |
| `*` | Rechercher mot sous curseur |

---

### Édition (Normal Mode)

#### Insert Mode

| Commande | Action |
|----------|--------|
| `i` | Insert avant curseur |
| `a` | Insert après curseur |
| `I` | Insert début de ligne |
| `A` | Insert fin de ligne |
| `o` | Nouvelle ligne en dessous |
| `O` | Nouvelle ligne au dessus |

#### Suppression

| Commande | Action |
|----------|--------|
| `x` | Supprimer caractère |
| `dd` | Supprimer ligne |
| `dw` | Supprimer mot |
| `d$` | Supprimer jusqu'à fin de ligne |
| `d0` | Supprimer jusqu'à début de ligne |
| `dG` | Supprimer jusqu'à fin de fichier |

#### Copier/Coller

| Commande | Action |
|----------|--------|
| `yy` | Copier ligne |
| `yw` | Copier mot |
| `y$` | Copier jusqu'à fin de ligne |
| `p` | Coller après curseur |
| `P` | Coller avant curseur |
| `\"*y` | Copier vers clipboard système |
| `\"*p` | Coller depuis clipboard système |

#### Autres

| Commande | Action |
|----------|--------|
| `u` | Undo |
| `Ctrl+r` | Redo |
| `.` | Répéter dernière commande |
| `~` | Toggle majuscule/minuscule |
| `>>` | Indenter ligne |
| `<<` | Désindenter ligne |

---

### Recherche & Remplacement

| Commande | Action |
|----------|--------|
| `/pattern` | Rechercher vers le bas |
| `?pattern` | Rechercher vers le haut |
| `n` | Résultat suivant |
| `N` | Résultat précédent |
| `:%s/old/new/g` | Remplacer dans tout le fichier |
| `:%s/old/new/gc` | Remplacer avec confirmation |

---

### Commandes de Fichier

| Commande | Action |
|----------|--------|
| `:w` | Sauvegarder |
| `:q` | Quitter |
| `:wq` | Sauvegarder et quitter |
| `:q!` | Quitter sans sauvegarder |
| `:e filename` | Ouvrir fichier |
| `:bn` | Buffer suivant |
| `:bp` | Buffer précédent |
| `:bd` | Fermer buffer |
| `:ls` | Lister buffers |

---

### Visual Mode (Sélection)

| Commande | Action |
|----------|--------|
| `v` | Visual mode (caractères) |
| `V` | Visual line mode (lignes) |
| `Ctrl+v` | Visual block mode (colonnes) |
| `d` | Supprimer sélection |
| `y` | Copier sélection |
| `>` | Indenter sélection |
| `<` | Désindenter sélection |

---

## 🔗 Workflow PKM Combiné

### Session Type PKM
```bash
# 1. Lancer session tmux
tmux new -s pkm

# 2. Setup windows
Ctrl+B c  # Window 1: Notes
Ctrl+B c  # Window 2: Git
Ctrl+B c  # Window 3: Scripts

# 3. Window 1: Édition notes
cd ~/vault/02_Projects/PKM-SYSTEM
nvim .

# 4. Window 2: Git
cd ~/vault
watch -n 5 git status

# 5. Window 3: Scripts
cd ~/scripts
```

### Édition Rapide d'une Note
```bash
# Workflow complet
cd ~/vault/00_Inbox
nvim \"$(date +%Y-%m-%d)-nouvelle-idee.md\"

# Dans nvim:
i                           # Insert mode
[écrire contenu]
ESC                         # Normal mode
:wq                         # Save & quit

# Commit
git add .
git commit -m \"feat: nouvelle idée\"
git push
```

---

## 📚 Ressources Externes

### Documentation Officielle
- [Tmux Manual](https://man.openbsd.org/tmux.1)
- [Neovim Documentation](https://neovim.io/doc/)
- [Vim Cheat Sheet](https://vim.rtorr.com/)

### Tutoriels
- [Tmux Cheat Sheet](https://tmuxcheatsheet.com/)
- [Learn Vim Progressively](http://yannesposito.com/Scratch/en/blog/Learn-Vim-Progressively/)

### Configurations
- [Tmux Plugins](https://github.com/tmux-plugins)
- [Neovim Kickstart](https://github.com/nvim-lua/kickstart.nvim)

---

## 🎯 Prochaines Étapes

- [ ] Personnaliser `.tmux.conf`
- [ ] Installer plugins Nvim (LSP, Telescope)
- [ ] Créer snippets pour templates notes
- [ ] Automatiser workflow git avec scripts

---

## 🔗 Liens Projet

- [[PKM System Workflow]] - Workflow général
- [[Ubuntu Setup]] - Configuration système
- [[Git Workflow]] - Gestion versions

---

**Dernière mise à jour:** 2025-11-01T20:00:00
**Status:** 📌 Pinned - Référence active
**Maintenance:** Ajouter commandes au fur et à mesure

---

## 💡 Tips & Astuces

### Tmux
- **Prefix personnalisé:** Change `Ctrl+B` en `Ctrl+A` dans `.tmux.conf` si plus confortable
- **Mouse mode:** `set -g mouse on` pour scroll et resize à la souris
- **Status bar:** Personnalise pour voir session/window/pane actifs

### Nvim
- **Leader key:** Configure une touche leader (ex: Space) pour tes raccourcis perso
- **Relative numbers:** `:set relativenumber` pour navigation rapide (ex: `5j` = 5 lignes bas)
- **Marks:** `ma` pour marquer position, `'a` pour y retourner

✅ CHANGEMENTS APPLIQUÉS
Métadonnées:

✅ Date+heure ajoutées (created, updated)
✅ Type défini (resource)
✅ Tags standardisés et enrichis
✅ Related links ajoutés
✅ Source documentée

Contenu:

✅ Context d'utilisation ajouté
✅ Tables pour meilleure lisibilité
✅ Sections enrichies (copy mode, visual mode, etc.)
✅ Use cases PKM ajoutés
✅ Workflow combiné Tmux+Nvim
✅ Tips & astuces
✅ Liens vers ressources externes
✅ Section prochaines étapes

Structure:

✅ Organisation plus claire
✅ Exemples concrets d'utilisation
✅ Layout recommandé pour PKM
✅ Workflow complet documenté


🎯 EMPLACEMENT
Reste dans: 04_Resources/Tmux-Nvim-Cheatsheet.md
C'est le bon endroit - c'est une resource/référence.

📝 PROCHAINE NOTE ?
Options:
A. VisuMethode.md (dans PKM-SYSTEM)
B. Backlog.md (dans PKM-SYSTEM)
C. Une note LinkedIn (dans PKM-SYSTEM/LinkedIn/)
D. Créer les 2 cartes Layer 1 manquantes (Ctrl+W, Ctrl+Shift+W)
E. Autre chose
Ton choix ? 🚀Réessayer

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-674-S674-ID-msg-674]]
- ⬇️ Next: [[Card-676-R676-Restructured-cheatsheet-metadata-classif]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #python
- #obsidian
- #receipts
- #code
- #git
- #automation
