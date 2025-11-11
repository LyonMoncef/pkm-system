---
type: chat-card
parent_export: '[[Export]]'
order: 142
role: assistant
created: '2025-11-11T01:06:55.468223Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 142 - Assistant

**ID:** msg-142

## 💬 Content


**ID:** msg-142

lua-- Configuration clipboard pour WSL
if vim.fn.has('wsl') == 1 then
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

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-141-R141-Bash-Télécharge-curl-https-github]]
- ⬇️ Next: [[Card-143-R143-Bash-mode-insertion-dans-Neovim]]
- 📊 MOC: [[_MOC_Slow copy-paste in terminal]]
