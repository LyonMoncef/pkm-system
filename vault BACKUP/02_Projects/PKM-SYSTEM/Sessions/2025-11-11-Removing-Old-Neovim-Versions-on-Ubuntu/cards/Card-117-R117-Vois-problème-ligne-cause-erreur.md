---
type: chat-card
parent_export: '[[Export]]'
order: 117
role: assistant
created: '2025-11-11T00:40:04.768993Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 117 - Assistant

**ID:** msg-117

## 💬 Content


**ID:** msg-117

Je vois le problème. La ligne qui cause l'erreur est celle qui essaie d'appliquer un style de bordure personnalisé aux popups LSP en utilisant un module misc.style qui n'existe pas dans votre configuration.
Voici comment vous pouvez résoudre ce problème :

Créez le module manquant :

bash mkdir -p ~/.config/nvim/lua/misc
 touch ~/.config/nvim/lua/misc/style.lua

Ajoutez le contenu suivant dans le fichier style.lua :

lua local M = {}

 -- Style de bordure par défaut
 M.border = \"rounded\" -- Vous pouvez choisir: 'none', 'single', 'double', 'rounded', 'solid', 'shadow'

 return M

Alternativement, si vous préférez ne pas créer ce module, vous pouvez modifier directement votre fichier lsp.lua pour qu'il n'utilise pas ce module manquant :

lua vim.lsp.handlers['textDocument/hover'] = vim.lsp.with(vim.lsp.handlers.hover, { border = \"rounded\" })
Le problème vient du fait que votre configuration essaie d'utiliser un module personnalisé pour les styles qui n'existe pas dans votre installation. Cette erreur n'est pas directement liée aux multiples versions de Neovim, mais plutôt à la configuration de votre instance actuelle.
Préférez-vous créer le module manquant ou simplement modifier la ligne problématique pour utiliser un style de bordure directement?

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-116-R116-Vois-problème-ligne-cause-erreur]]
- ⬇️ Next: [[Card-118-R118-Vois-problème-ligne-cause-erreur]]
- 📊 MOC: [[_MOC_Removing Old Neovim Versions on Ubuntu]]
