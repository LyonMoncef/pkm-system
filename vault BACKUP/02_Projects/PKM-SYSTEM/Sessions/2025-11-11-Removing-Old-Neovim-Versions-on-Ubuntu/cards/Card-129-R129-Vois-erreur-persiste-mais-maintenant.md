---
type: chat-card
parent_export: '[[Export]]'
order: 129
role: assistant
created: '2025-11-11T00:40:04.908425Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 129 - Assistant

**ID:** msg-129

## 💬 Content


**ID:** msg-129

Je vois que l'erreur persiste, mais maintenant à la ligne 120 de votre fichier lsp.lua, toujours liée au module manquant 'misc.style'.
Voici une solution plus complète pour résoudre ce problème :

Créez le module manquant avec tous les chemins nécessaires :

bash mkdir -p ~/.config/nvim/lua/misc

Créez le fichier style.lua dans ce répertoire :

bash nvim ~/.config/nvim/lua/misc/style.lua

Ajoutez ce contenu au fichier :

lua local M = {}

 -- Style de bordure par défaut pour les popups LSP
 M.border = \"rounded\"

 -- Vous pouvez ajouter d'autres styles ici si nécessaire

 return M

Sauvegardez le fichier et redémarrez Neovim.

Si cela ne résout pas le problème, vous pourriez avoir plusieurs utilisations de ce module manquant. Une solution alternative serait de modifier votre fichier lsp.lua pour remplacer toutes les références à 'misc.style' :

Ouvrez votre fichier lsp.lua :

bash nvim ~/.config/nvim/lua/plugins/lsp.lua

Cherchez toutes les occurrences de require('misc.style') et remplacez-les par des valeurs directes. Par exemple, pour la ligne 120 et la ligne 118 précédente :

lua -- Avant :
 vim.lsp.handlers['textDocument/hover'] = vim.lsp.with(vim.lsp.handlers.hover, { border = require('misc.style').border })

 -- Après :
 vim.lsp.handlers['textDocument/hover'] = vim.lsp.with(vim.lsp.handlers.hover, { border = \"rounded\" })
Faites de même pour toutes les autres références à ce module dans votre configuration.

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-128-R128-Vois-erreur-persiste-mais-maintenant]]
- ⬇️ Next: [[Card-130-R130-Bash-mkdir-config-nvim-misc]]
- 📊 MOC: [[_MOC_Removing Old Neovim Versions on Ubuntu]]
