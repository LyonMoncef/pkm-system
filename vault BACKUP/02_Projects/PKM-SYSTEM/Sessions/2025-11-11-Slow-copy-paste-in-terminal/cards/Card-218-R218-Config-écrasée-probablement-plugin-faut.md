---
type: chat-card
parent_export: '[[Export]]'
order: 218
role: assistant
created: '2025-11-11T01:06:56.234803Z'
tags:
- chat-card
- code
attachments_count: 0
---

# 🤖 Message 218 - Assistant

**ID:** msg-218

## 💬 Content


**ID:** msg-218

Ah ! Ta config est écrasée par OSC52 (probablement un plugin). Il faut forcer après le chargement.
Solution : Force la config APRÈS les plugins
Dans ton ~/.config/nvim/init.lua, à la toute fin du fichier (après tous les plugins) :
lua-- Force win32yank APRÈS tout le reste
vim.schedule(function()
 vim.g.clipboard = {
 name = 'WslClipboard',
 copy = {
 ['+'] = 'win32yank.exe -i --crlf',
 ['*'] = 'win32yank.exe -i --crlf',
 },
 paste = {
 ['+'] = 'win32yank.exe -o --lf',
 ['*'] = 'win32yank.exe -o --lf',
 },
 cache_enabled = 0,
 }
end)
Ou utilise un autocmd :
luavim.api.nvim_create_autocmd(\"VimEnter\", {
 callback = function()
 vim.g.clipboard = {
 name = 'WslClipboard',
 copy = {
 ['+'] = 'win32yank.exe -i --crlf',
 ['*'] = 'win32yank.exe -i --crlf',
 },
 paste = {
 ['+'] = 'win32yank.exe -o --lf',
 ['*'] = 'win32yank.exe -o --lf',
 },
 cache_enabled = 0,
 }
 end
})
Redémarre Neovim et refais :
vim:lua print(vim.inspect(vim.g.clipboard))
Ça devrait maintenant afficher \"WslClipboard\" au lieu de \"osc52\" ! 🎯

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-217-R217-Problème-clair-config-appliquée-utilise]]
- ⬇️ Next: [[Card-219-R219-Force-APRÈS-tout-reste-schedule]]
- 📊 MOC: [[_MOC_Slow copy-paste in terminal]]

## 🏷️ Topics

- #code
