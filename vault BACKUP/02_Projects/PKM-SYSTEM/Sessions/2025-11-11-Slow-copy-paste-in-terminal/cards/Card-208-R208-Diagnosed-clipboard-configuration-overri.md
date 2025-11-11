---
type: chat-card
parent_export: '[[Export]]'
order: 208
role: assistant
created: '2025-11-11T01:06:56.091945Z'
tags:
- chat-card
- code
attachments_count: 0
---

# 🤖 Message 208 - Assistant

**ID:** msg-208

## 💬 Content


**ID:** msg-208

Diagnosed clipboard configuration override issue in Neovim.Ah ! Le problème est clair : la config win32yank n'est pas appliquée, il utilise toujours osc52. Ça veut dire soit :

La config n'est pas dans le bon ordre dans init.lua
Un plugin surcharge la config après

Il faut soit :

Mettre la config clipboard APRÈS les plugins
Ou utiliser autocmd pour forcer après le chargement
Ou vérifier qu'il n'y a pas un plugin qui gère le clipboard

Le fait que ça affiche \"osc52\" montre que quelque chose surcharge la config.Ah ! Ta config est écrasée par OSC52 (probablement un plugin). Il faut forcer après le chargement.
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
Ça devrait maintenant afficher \"WslClipboard\" au lieu de \"osc52\" ! 🎯Réessayer

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-207-S207-ID-msg-207]]
- ⬇️ Next: [[Card-209-R209-Diagnosed-clipboard-configuration-overri]]
- 📊 MOC: [[_MOC_Slow copy-paste in terminal]]

## 🏷️ Topics

- #code
