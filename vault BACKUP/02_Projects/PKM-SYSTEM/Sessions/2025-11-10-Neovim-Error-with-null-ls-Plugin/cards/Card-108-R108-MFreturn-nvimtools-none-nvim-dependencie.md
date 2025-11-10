---
type: chat-card
parent_export: '[[Export]]'
order: 108
role: assistant
created: '2025-11-10T21:42:07.845242Z'
tags:
- chat-card
- python
- obsidian
- code
attachments_count: 0
---

# 🤖 Message 108 - Assistant

**ID:** msg-108

## 💬 Content


**ID:** msg-108

MFreturn {
 'nvimtools/none-ls.nvim',
 dependencies = {
 'nvimtools/none-ls-extras.nvim',
 'jayp0521/mason-null-ls.nvim', -- ensure dependencies are installed
 },
 config = function()
 local null_ls = require 'null-ls'
 local formatting = null_ls.builtins.formatting -- to setup formatters
 local diagnostics = null_ls.builtins.diagnostics -- to setup linters
 -- Formatters & linters for mason to install
 require('mason-null-ls').setup {
 ensure_installed = {
 'prettier', -- ts/js formatter
 'stylua', -- lua formatter
 'eslint_d', -- ts/js linter
 'shfmt', -- Shell formatter
 'checkmake', -- linter for Makefiles
 'ruff', -- Python linter and formatter
 },
 automatic_installation = true,
 }
 local sources = {
 diagnostics.checkmake,
 formatting.prettier.with { filetypes = { 'html', 'json', 'yaml', 'markdown' } },
 formatting.stylua,
 formatting.shfmt.with { args = { '-i', '4' } },
 formatting.terraform_fmt,
 require('none-ls.formatting.ruff').with { extra_args = { '--extend-select', 'I' } },
 require 'none-ls.formatting.ruff_format',
 }
 local augroup = vim.api.nvim_create_augroup('LspFormatting', {})
 null_ls.setup {
 -- debug = true, -- Enable debug mode. Inspect logs with :NullLsLog.
 sources = sources,
 -- you can reuse a shared lspconfig on_attach callback here
 on_attach = function(client, bufnr)
 if client.supports_method 'textDocument/formatting' then
 vim.api.nvim_clear_autocmds { group = augroup, buffer = bufnr }
 vim.api.nvim_create_autocmd('BufWritePre', {
 group = augroup,
 buffer = bufnr,
 callback = function()
 vim.lsp.buf.format { async = false }
 end,
 })
 end
 end,
 }
 end,
}Afficher plus

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-107-R107-MFreturn-nvimtools-none-nvim-dependencie]]
- ⬇️ Next: [[Card-109-R109-Return-nvimtools-none-nvim-dependencies]]
- 📊 MOC: [[_MOC_Neovim Error with null-ls Plugin]]

## 🏷️ Topics

- #python
- #obsidian
- #code
