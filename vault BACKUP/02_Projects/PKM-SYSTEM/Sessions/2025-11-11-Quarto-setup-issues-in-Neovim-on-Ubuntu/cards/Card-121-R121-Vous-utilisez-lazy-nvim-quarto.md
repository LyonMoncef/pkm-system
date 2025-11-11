---
type: chat-card
parent_export: '[[Export]]'
order: 121
role: assistant
created: '2025-11-11T00:20:36.485897Z'
tags:
- chat-card
- python
- code
attachments_count: 0
---

# 🤖 Message 121 - Assistant

**ID:** msg-121

## 💬 Content


**ID:** msg-121

lua-- Si vous utilisez lazy.nvim
{
 'quarto-dev/quarto-nvim',
 dependencies = {
 'jmbuhr/otter.nvim',
 'neovim/nvim-lspconfig',
 },
 config = function()
 require('quarto').setup({
 lspFeatures = {
 enabled = true,
 languages = { 'r', 'python', 'julia' },
 diagnostics = {
 enabled = true,
 },
 completion = {
 enabled = true,
 },
 },
 })
 end,
}

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-120-R120-Luavim-stylua-quarto-Ajoutez-ceci]]
- ⬇️ Next: [[Card-122-R122-MFError-executing-schedule-callback-shar]]
- 📊 MOC: [[_MOC_Quarto setup issues in Neovim on Ubuntu]]

## 🏷️ Topics

- #python
- #code
