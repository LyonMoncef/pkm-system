---
type: chat-card
parent_export: '[[Export]]'
order: 117
role: user
created: '2025-11-10T03:56:18.546465Z'
tags:
- chat-card
- code
attachments_count: 0
---

# 👤 Message 117 - User

**ID:** msg-117

## 💬 Content


**ID:** msg-117

return {
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
}Quand est ce que les raccourcis sont actifs

---


## 🔗 Navigation

- ⬆️ Previous: [[116_assistant_msg-116]]
- ⬇️ Next: [[118_assistant_msg-118]]
- 📊 MOC: [[_MOC_Configuring Quarto.lua Plugin for Neovim Jupyter Notebook Simulation]]

## 🏷️ Topics

- #code
