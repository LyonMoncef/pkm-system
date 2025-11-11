---
type: chat-card
parent_export: '[[Export]]'
order: 154
role: assistant
created: '2025-11-11T00:20:36.775505Z'
tags:
- chat-card
- code
attachments_count: 0
---

# 🤖 Message 154 - Assistant

**ID:** msg-154

## 💬 Content


**ID:** msg-154

return {

 { -- requires plugins in lua/plugins/treesitter.lua and lua/plugins/lsp.lua
 -- for complete functionality (language features)
 'quarto-dev/quarto-nvim',
 ft = { 'quarto' },
 dev = false,
 opts = {},
 dependencies = {
 -- for language features in code cells
 -pasted local capabilities = vim.lsp.protocol.make_client_capabilities()
 capabilities = vim.tbl_deep_extend('force', capabilities, require('cmp_nvim_lsp').default_capabilities())
 capabilities.workspace.didChangeWatchedFiles.dynamicRegistration = false


 -- Enable the following language servepasted

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-153-R153-Return-requires-plugins-plugins-treesitt]]
- ⬇️ Next: [[Card-155-R155-Return-requires-plugins-plugins-treesitt]]
- 📊 MOC: [[_MOC_Quarto setup issues in Neovim on Ubuntu]]

## 🏷️ Topics

- #code
