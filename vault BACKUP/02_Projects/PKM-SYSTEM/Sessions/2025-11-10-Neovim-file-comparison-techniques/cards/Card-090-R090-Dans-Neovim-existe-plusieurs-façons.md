---
type: chat-card
parent_export: '[[Export]]'
order: 90
role: assistant
created: '2025-11-10T21:42:42.671363Z'
tags:
- chat-card
- excel
- git
attachments_count: 0
---

# 🤖 Message 90 - Assistant

**ID:** msg-90

## 💬 Content


**ID:** msg-90

Dans Neovim, il existe plusieurs façons de comparer/review deux fichiers :
1. Mode diff (vimdiff)
Depuis Neovim :
bash:vs fichier2.txt # Ouvre le 2ème fichier en split vertical
:windo diffthis # Active le mode diff sur les deux fenêtres
Ou directement depuis le terminal :
bashnvim -d fichier1.txt fichier2.txt
# ou
vimdiff fichier1.txt fichier2.txt
2. Commandes utiles en mode diff

]c - Aller à la prochaine différence
[c - Aller à la différence précédente
:diffget - Récupérer les changements de l'autre fichier
:diffput - Envoyer les changements vers l'autre fichier
:diffupdate - Rafraîchir la comparaison
:windo diffoff - Désactiver le mode diff

3. Splits manuels (sans diff)
bash:split fichier2.txt # Split horizontal
:vsplit fichier2.txt # Split vertical
Navigation entre les splits :

Ctrl+w h/j/k/l - Se déplacer entre les fenêtres
Ctrl+w w - Basculer entre les fenêtres

4. Avec un plugin (recommandé)
diffview.nvim est excellent pour Git :
bash:DiffviewOpen
:DiffviewFileHistory
Le mode diff natif est généralement le plus efficace pour comparer deux fichiers côte à côte !Réessayer

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-089-Q089-Je-review-2-fichiers]]
- ⬇️ Next: [[Card-091-R091-Dans-Neovim-existe-plusieurs-façons]]
- 📊 MOC: [[_MOC_Neovim file comparison techniques]]

## 🏷️ Topics

- #excel
- #git
