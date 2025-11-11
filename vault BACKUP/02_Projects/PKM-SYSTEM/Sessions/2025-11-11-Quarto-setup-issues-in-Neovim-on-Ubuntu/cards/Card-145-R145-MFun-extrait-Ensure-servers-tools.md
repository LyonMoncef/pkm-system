---
type: chat-card
parent_export: '[[Export]]'
order: 145
role: assistant
created: '2025-11-11T00:20:36.697029Z'
tags:
- chat-card
- obsidian
- code
- git
attachments_count: 0
---

# 🤖 Message 145 - Assistant

**ID:** msg-145

## 💬 Content


**ID:** msg-145

MFun extrait de mon lsp.lua -- Ensure the servers and tools above are installed
 require('mason').setup()
 -- You can add other tools here that you want Mason to install
 -- for you, so that they are available from within Neovim.
 local ensure_installed = vim.tbl_keys(servers or {})
 vim.list_extend(ensure_installed, {
 'stylua', -- Used to format lua code
 })
 vim.filetype.add({
 extension = {
 qmd = \"markdown\",
 },
 })
 require('lspconfig').quarto.setup{
 cmd = { \"quarto\", \"check\" }
 }
 require('mason-tool-installer').setup { ensure_installed = ensure_installed }
 require('mason-lspconfig').setup {
 handlers = {
 function(server_name)
 local server = servers[server_name] or {}
 -- This handles overriding only values explicitly passed
 -- by the server configuration above. Useful when disabling
 -- certain features of an LSP (for example, turning off formatting for tsserver)
 server.capabilities = vim.tbl_deep_extend('force', {}, capabilities, server.capabilities or {})
 require('lspconfig')[server_name].setup(server)
 end,
 },
 }
 end,un extrait de mon init.lua-- Setup plugins
require('lazy').setup({
 require 'plugins.aerial',
 require 'plugins.alpha',
 require 'plugins.completion',
 require 'plugins.avante',
 require 'plugins.bufferline',
 require 'plugins.colortheme',
 require 'plugins.comment',
 -- require 'plugins.database',
 -- require 'plugins.debug',
 require 'plugins.gitsigns',
 require 'plugins.harpoon',
 require 'plugins.indent-blankline',
 require 'plugins.lazygit',
 require 'plugins.lsp',
 require 'plugins.lualine',
 require 'plugins.misc',
 require 'plugins.neo-tree',
 require 'plugins.quarto',
 require 'plugins.slime',
 require 'plugins.telescope',
 require 'plugins.treesitter',
 require 'plugins.vim-tmux-navigator',
 require 'plugins.themes.onedark',
 require 'plugins.themes.nord',
 --require 'plugins.none-ls',
 -- require 'plugins.chatgpt',
}, {
 ui = {
 -- If you have a Nerd Font, set icons to an empty table which will use the
 -- default lazy.nvim defined Nerd Font icons otherwise define a unicode icons table
 icons = vim.g.have_nerd_font and {} or {
 cmd = '⌘',
 config = '🛠',
 event = '📅',
 ft = '📂',
 init = '⚙',
 keys = '🗝',
 plugin = '🔌',
 runtime = '💻',
 require = '🌙',
 source = '📄',
 start = '🚀',
 task = '📌',
 lazy = '💤 ',
 },
 },
})l'erreur à l'ouverture de nvim :
Error executing vim.schedule lua callback: ...l/share/nvim/lazy/mason.nvim/lua/mason-registry/init.lua:80: Cannot find package \"quarto\".
stack traceback:
 [C]: in function 'error'
 ...l/share/nvim/lazy/mason.nvim/lua/mason-registry/init.lua:80: in function 'get_package'
 ...on-tool-installer.nvim/lua/mason-tool-installer/init.lua:169: in function 'callback'
 ...share/nvim/lazy/mason.nvim/lua/mason-core/async/init.lua:87: in function 'step'
 ...share/nvim/lazy/mason.nvim/lua/mason-core/async/init.lua:96: in function 'run'
 ...l/share/nvim/lazy/mason.nvim/lua/mason-registry/init.lua:202: in function 'refresh'
 ...on-tool-installer.nvim/lua/mason-tool-installer/init.lua:251: in function ''
 vim/_editor.lua: in function ''
 vim/_editor.lua: in function <vim/_editor.lua:0>Afficher plus

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-144-R144-MFun-extrait-Ensure-servers-tools]]
- ⬇️ Next: [[Card-146-R146-Extrait-Ensure-servers-tools-above]]
- 📊 MOC: [[_MOC_Quarto setup issues in Neovim on Ubuntu]]

## 🏷️ Topics

- #obsidian
- #code
- #git
