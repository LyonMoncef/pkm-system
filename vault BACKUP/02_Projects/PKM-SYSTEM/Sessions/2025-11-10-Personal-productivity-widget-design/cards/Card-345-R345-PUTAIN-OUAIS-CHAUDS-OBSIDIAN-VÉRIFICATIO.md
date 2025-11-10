---
type: chat-card
parent_export: '[[Export]]'
order: 345
role: assistant
created: '2025-11-10T22:55:59.266838Z'
tags:
- chat-card
- obsidian
attachments_count: 0
---

# 🤖 Message 345 - Assistant

**ID:** msg-345

## 💬 Content


**ID:** msg-345

PUTAIN OUAIS ! 🔥🔥🔥
ON EST CHAUDS ! LET'S GO !

🧠 OBSIDIAN - VÉRIFICATION & SETUP
Étape 1 : Vérif installation (2 min)
Dans ton terminal :
bash# Va dans ton dossier pkm-system
cd ~/Projects/pkm-system

# Vérifie la structure vault
ls -la vault/

# Tu devrais voir les dossiers :
# 00_Inbox, 01_Journal, 02_Projects, etc.
Obsidian est installé ? (tu as dit oui hier)

Étape 2 : Pointer Obsidian vers ton vault
Option A : Vault local (pour tester rapidement)

Ouvre Obsidian
\"Open folder as vault\"
Sélectionne ~/Projects/pkm-system/vault/
Boom, vault ouvert !

Option B : Vault sur NAS (ton setup final)
Tu as dit que tu as créé l'arbo sur ton NAS.
C'est où exactement ?

/mnt/nas/PKM_Vault/ ?
Autre chemin ?

Pour le lier :
bash# Crée un lien symbolique du NAS vers ton projet local
ln -s /chemin/vers/ton/NAS/PKM_Vault ~/Projects/pkm-system/vault

# OU si tu veux garder les deux séparés
# Point juste Obsidian directement vers le NAS

Étape 3 : Installer les plugins essentiels
Dans Obsidian :

Settings (⚙️ en bas à gauche)
Community plugins → \"Turn on community plugins\"
Browse → Cherche et installe :

PLUGINS ESSENTIELS (Phase 1) :
✅ Dataview

Pour queries dynamiques
\"Install\" → \"Enable\"

✅ Templater

Pour templates intelligents
\"Install\" → \"Enable\"
Settings → Template folder : ../obsidian/templates

✅ Calendar

Vue calendrier pour daily notes
\"Install\" → \"Enable\"

✅ QuickAdd (Optionnel pour MVP)

Capture rapide depuis Obsidian
\"Install\" → \"Enable\"


Étape 4 : Config de base
Settings → Files & Links :

Default location for new notes : 00_Inbox
New link format : Relative path to file
Use [[Wikilinks]] : ✅ ON

Settings → Daily notes :

Date format : YYYY-MM-DD
New file location : 01_Journal
Template file location : ../obsidian/templates/daily-note.md


📝 CRÉER TES PREMIÈRES NOTES
Note 1 : Le Pari (celle que je t'ai donnée)
bash# Dans ton vault
cd ~/Projects/pkm-system/vault/02_Projects

# Crée le fichier
nano \"20251018-Le-Pari-PKM-System.md\"

# OU utilise Obsidian directement
Contenu : Utilise l'artifact \"20241016 - Le Pari PKM System\" que je t'ai donné avant !

Note 2 : Ta première cheatsheet
Dans Obsidian :

Nouveau fichier dans 04_Resources/
Nom : Tmux-Nvim-Cheatsheet.md
Contenu :

markdown---
tags: #cheatsheet #tmux #nvim #terminal
created: 2025-10-18
pinned: true
---

# Tmux & Nvim Cheatsheet

## 🖥️ Tmux

### Sessions
- `tmux new -s nom` - Nouvelle session
- `tmux attach -t nom` - Attacher session
- `Ctrl+B d` - Détacher session
- `tmux ls` - Lister sessions

### Windows
- `Ctrl+B c` - Nouvelle fenêtre
- `Ctrl+B n` - Fenêtre suivante
- `Ctrl+B p` - Fenêtre précédente
- `Ctrl+B ,` - Renommer fenêtre

### Panes
- `Ctrl+B %` - Split vertical
- `Ctrl+B \"` - Split horizontal
- `Ctrl+B ←→↑↓` - Naviguer entre panes
- `Ctrl+B z` - Toggle fullscreen pane

## ⚡ Nvim

### Navigation
- `h j k l` - Gauche, Bas, Haut, Droite
- `w` - Mot suivant
- `b` - Mot précédent
- `gg` - Début fichier
- `G` - Fin fichier

### Édition
- `i` - Insert mode
- `ESC` - Normal mode
- `dd` - Supprimer ligne
- `yy` - Copier ligne
- `p` - Coller

### Commandes
- `:w` - Sauvegarder
- `:q` - Quitter
- `:wq` - Sauvegarder et quitter
- `:q!` - Quitter sans sauvegarder

## 🔗 Liens utiles
- [Tmux Cheat Sheet](https://tmuxcheatsheet.com/)
- [Nvim Documentation](https://neovim.io/doc/)

---

**Note :** Complète au fur et à mesure que tu te rappelles des commandes !

✅ CHECKLIST - OÙ TU EN ES ?
Dis-moi :

 Obsidian ouvert sur le vault ?
 Plugins installés (Dataview, Templater, Calendar) ?
 Settings de base configurés ?
 Note \"Le Pari\" créée ?
 Cheatsheet tmux/nvim créée ?

Quelle étape tu fais en ce moment ?
OU tu as un blocage quelque part ? 🤔
GO GO GO ! 💪🔥Réessayer

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-344-S344-ID-msg-344]]
- ⬇️ Next: [[Card-346-R346-PUTAIN-OUAIS-CHAUDS-OBSIDIAN-VÉRIFICATIO]]
- 📊 MOC: [[_MOC_Personal productivity widget design]]

## 🏷️ Topics

- #obsidian
