---
type: chat-card
parent_export: '[[Export]]'
order: 107
role: assistant
created: '2025-11-11T00:20:36.376390Z'
tags:
- chat-card
- obsidian
attachments_count: 0
---

# 🤖 Message 107 - Assistant

**ID:** msg-107

## 💬 Content


**ID:** msg-107

Merci pour ces informations complémentaires. Je vois maintenant le problème plus clairement.
L'erreur indique que le parser pour \"quarto\" n'est pas disponible dans nvim-treesitter. C'est pourquoi vous obtenez l'erreur \"Parser not available for language 'quarto'\" lors du chargement du plugin nvim-ts-autotag.
Voici comment résoudre ce problème :

En fait, Quarto utilise le parser markdown avec des extensions spécifiques. Il n'existe pas de parser Treesitter nommé \"quarto\" directement. Modifiez votre configuration treesitter.lua pour enlever 'quarto' et assurez-vous d'avoir 'markdown' à la place :

lua-- Dans votre fichier de configuration treesitter
ensure_installed = {
 \"lua\",
 \"vim\",
 \"markdown\", -- Utilisez markdown au lieu de quarto
 -- autres parsers...
}

Pour le support Quarto dans Neovim, vous devriez utiliser le serveur de langage Quarto via LSP. Assurez-vous d'avoir configuré correctement le LSP pour Quarto avec quelque chose comme :

lua-- Dans votre configuration LSP
require('lspconfig').quarto.setup{}

Si vous n'avez pas encore le plugin quarto-nvim, vous pourriez l'ajouter à votre configuration :

luause {
 'quarto-dev/quarto-nvim',
 requires = {
 'jmbuhr/otter.nvim',
 'neovim/nvim-lspconfig'
 }
}

Une fois ces modifications effectuées, redémarrez Neovim et essayez d'ouvrir à nouveau votre fichier .qmd.

Est-ce que vous utilisez déjà quarto-nvim ou un autre plugin spécifique à Quarto ? En sachant cela, je pourrais vous donner des conseils plus précis pour résoudre votre problème.

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-106-R106-Merci-pour-informations-complémentaires-]]
- ⬇️ Next: [[Card-108-R108-Dans-votre-fichier-configuration-treesit]]
- 📊 MOC: [[_MOC_Quarto setup issues in Neovim on Ubuntu]]

## 🏷️ Topics

- #obsidian
