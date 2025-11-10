---
type: chat-card
parent_export: '[[Export]]'
order: 120
role: assistant
created: '2025-11-10T21:08:50.656937Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 120 - Assistant

**ID:** msg-120

## 💬 Content


**ID:** msg-120

Cette configuration du plugin aerial.nvim définit deux types de raccourcis clavier qui sont actifs dans des contextes différents :

Raccourcis définis dans on_attach (touches { et }):

Ces raccourcis sont actifs uniquement dans les buffers où aerial a été attaché
Ils deviennent disponibles quand aerial s'attache à un buffer spécifique (typiquement quand vous ouvrez un fichier de code supporté par aerial)
Ces touches permettent de naviguer entre les éléments du outline (symboles du fichier comme fonctions, classes, etc.)
La définition { buffer = bufnr } signifie que ces mappages sont spécifiques au buffer et ne sont pas globaux


Raccourcis globaux (touches <leader>o et <leader>on):

Ces raccourcis sont actifs globalement dans Neovim
Ils sont disponibles quel que soit le buffer actif
<leader>o bascule l'affichage du panneau aerial (outline)
<leader>on bascule le mode de navigation aerial


La différence principale est que les touches { et } ne fonctionnent que dans les buffers où aerial est actif, tandis que les touches <leader>o et <leader>on fonctionnent partout et servent à activer/désactiver les fonctionnalités d'aerial.
C'est une approche courante dans Neovim : les raccourcis spécifiques à une fonctionnalité ne sont actifs que lorsque cette fonctionnalité est pertinente pour le buffer actuel, ce qui évite de surcharger l'espace des raccourcis clavier global.

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-119-R119-Cette-configuration-plugin-aerial-nvim]]
- ⬇️ Next: [[Card-121-R121-Return-Autocompletion-nvim-dependencies-]]
- 📊 MOC: [[_MOC_Configuring Quarto.lua Plugin for Neovim Jupyter Notebook Simulation]]
