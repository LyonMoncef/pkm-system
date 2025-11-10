---
type: chat-card
parent_export: '[[Export]]'
order: 93
role: user
created: '2025-11-10T21:08:50.355036Z'
tags:
- chat-card
- code
attachments_count: 0
---

# 👤 Message 93 - User

**ID:** msg-93

## 💬 Content


**ID:** msg-93

on va décomposer ensemble un fichier quarto.lua qui gère un plugin permettant de simuler un jupyter notebook dans un environnement neovim { -- requires plugins in lua/plugins/treesitter.lua and lua/plugins/lsp.lua
 -- for complete functionality (language features)
 'quarto-dev/quarto-nvim',
 ft = { 'quarto' },
 dev = false,
 opts = {},
 dependencies = {
 -- for language features in code cells
 -- configured in lua/plugins/lsp.lua and
 -- added as a nvim-cmp source in lua/plugins/completion.lua
 'jmbuhr/otter.nvim',
 },
 },

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-092-R092-Décomposer-ensemble-fichier-quarto-gère]]
- ⬇️ Next: [[Card-094-R094-Bonjour-vais-vous-aider-décomposer]]
- 📊 MOC: [[_MOC_Configuring Quarto.lua Plugin for Neovim Jupyter Notebook Simulation]]

## 🏷️ Topics

- #code
