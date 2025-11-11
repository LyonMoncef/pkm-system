---
type: chat-card
parent_export: '[[Export]]'
order: 115
role: user
created: '2025-11-11T00:20:36.440114Z'
tags:
- chat-card
- code
attachments_count: 0
---

# 👤 Message 115 - User

**ID:** msg-115

## 💬 Content


**ID:** msg-115

j'ai ça dans mon fichier lsp.lua -- Ensure the servers and tools above are installed
 require('mason').setup()
 -- You can add other tools here that you want Mason to install
 -- for you, so that they are available from within Neovim.
 local ensure_installed = vim.tbl_keys(servers or {})
 vim.list_extend(ensure_installed, {
 'stylua', -- Used to format lua code
 })
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

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-114-R114-Dans-fichier-Ensure-servers-tools]]
- ⬇️ Next: [[Card-116-R116-Merci-pour-partage-votre-configuration]]
- 📊 MOC: [[_MOC_Quarto setup issues in Neovim on Ubuntu]]

## 🏷️ Topics

- #code
