---
type: chat-card
parent_export: '[[Export]]'
order: 95
role: assistant
created: '2025-11-11T00:20:36.276685Z'
tags:
- chat-card
- obsidian
- code
attachments_count: 0
---

# 🤖 Message 95 - Assistant

**ID:** msg-95

## 💬 Content


**ID:** msg-95

Bonjour ! Je comprends que vous rencontrez un problème avec Quarto dans Neovim sur Ubuntu, spécifiquement une erreur \"Error requesting document symbols\" lors de l'ouverture de fichiers .qmd.
Ce problème est probablement lié à la configuration de Language Server Protocol (LSP) pour les fichiers Quarto dans Neovim. Voici quelques pistes pour résoudre ce problème :

Assurez-vous d'avoir le serveur de langage Quarto installé :

bashnpm install -g @quarto/quarto-lsp

Vérifiez que votre configuration Neovim inclut un support LSP pour Quarto. Vous pouvez utiliser nvim-lspconfig avec une configuration comme celle-ci :

luarequire('lspconfig').quarto.setup{}

Si vous utilisez nvim-treesitter, vérifiez que vous avez les parsers nécessaires :

lua:TSInstall quarto markdown
```

4. Vérifiez les journaux LSP pour des informations plus détaillées sur l'erreur :
```
:LspLog

Si vous utilisez null-ls ou conform.nvim, assurez-vous qu'ils n'entrent pas en conflit avec le serveur LSP de Quarto.

Avez-vous récemment mis à jour Neovim, Quarto ou l'un de vos plugins ? Pourriez-vous partager votre configuration actuelle pour les fichiers Quarto dans Neovim ?

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-094-R094-Bonjour-comprends-vous-rencontrez-problè]]
- ⬇️ Next: [[Card-096-R096-Bonjour-comprends-vous-rencontrez-problè]]
- 📊 MOC: [[_MOC_Quarto setup issues in Neovim on Ubuntu]]

## 🏷️ Topics

- #obsidian
- #code
