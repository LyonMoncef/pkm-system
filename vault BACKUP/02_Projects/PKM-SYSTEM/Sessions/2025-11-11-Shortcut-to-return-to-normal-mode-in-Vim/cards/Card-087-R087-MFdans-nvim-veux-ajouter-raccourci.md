---
type: chat-card
parent_export: '[[Export]]'
order: 87
role: assistant
created: '2025-11-11T00:41:26.875087Z'
tags:
- chat-card
- python
- automation
attachments_count: 0
---

# 🤖 Message 87 - Assistant

**ID:** msg-87

## 💬 Content


**ID:** msg-87

MFdans nvim je veux ajouter un raccourci \"q\" en mode visuel qui permet de revenir en mode normalPour ajouter un raccourci \"q\" en mode visuel dans nvim qui permet de revenir en mode normal, vous pouvez modifier votre fichier de configuration nvim.
Voici comment procéder :

Ouvrez votre fichier de configuration nvim (généralement ~/.config/nvim/init.vim ou ~/.config/nvim/init.lua)
Ajoutez la ligne suivante si vous utilisez Vimscript (init.vim) :

vimvnoremap q <Esc>

Ou si vous utilisez Lua (init.lua) :

luavim.api.nvim_set_keymap('v', 'q', '<Esc>', { noremap = true, silent = true })
Cette commande associe la touche \"q\" en mode visuel à la fonction d'échappement (Escape), qui vous ramènera au mode normal.
Après avoir ajouté cette ligne, sauvegardez le fichier et redémarrez nvim (ou rechargez la configuration avec :source % si vous êtes en train d'éditer votre fichier de configuration).RéessayerClaude peut faire des erreurs. Assurez-vous de vérifier ses réponses. Sonnet 4.5

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-086-R086-MFdans-nvim-veux-ajouter-raccourci]]
- ⬇️ Next: [[Card-088-R088-MFdans-nvim-veux-ajouter-raccourci]]
- 📊 MOC: [[_MOC_Shortcut to return to normal mode in Vim]]

## 🏷️ Topics

- #python
- #automation
