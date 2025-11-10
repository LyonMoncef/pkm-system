---
type: chat-card
parent_export: '[[Export]]'
order: 114
role: assistant
created: '2025-11-10T21:08:50.587562Z'
tags:
- chat-card
- code
attachments_count: 0
---

# 🤖 Message 114 - Assistant

**ID:** msg-114

## 💬 Content


**ID:** msg-114

MFreturn {
 'stevearc/aerial.nvim',
 lazy_load = true,
 opts = {},
 -- Optional dependencies
 dependencies = {
 'nvim-treesitter/nvim-treesitter',
 'nvim-tree/nvim-web-devicons',
 },
 config = function()
 require('aerial').setup {
 -- optionally use on_attach to set keymaps when aerial has attached to a buffer
 on_attach = function(bufnr)
 -- Jump forwards/backwards with '{' and '}'
 vim.keymap.set('n', '{', '<cmd>AerialPrev<CR>', { buffer = bufnr })
 vim.keymap.set('n', '}', '<cmd>AerialNext<CR>', { buffer = bufnr })
 end,
 layout = {
 min_width = 30,
 },
 }
 -- You probably also want to set a keymap to toggle aerial
 vim.keymap.set('n', '<leader>o', '<cmd>AerialToggle!<CR>')
 vim.keymap.set('n', '<leader>on', '<cmd>AerialNavToggle<CR>')
 end,
}Quand est ce que les raccourcis sont actifsAfficher plus

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-113-R113-MFreturn-stevearc-aerial-nvim-true]]
- ⬇️ Next: [[Card-115-R115-MFreturn-stevearc-aerial-nvim-true]]
- 📊 MOC: [[_MOC_Configuring Quarto.lua Plugin for Neovim Jupyter Notebook Simulation]]

## 🏷️ Topics

- #code
