---
type: chat-card
parent_export: '[[Export]]'
order: 180
role: assistant
created: '2025-11-11T01:06:55.797382Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 180 - Assistant

**ID:** msg-180

## 💬 Content


**ID:** msg-180

lua-- Au lieu de if vim.fn.has('wsl') == 1 then
-- Utilise :
if vim.fn.executable('win32yank.exe') == 1 then
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

- ⬆️ Previous: [[Card-179-R179-Bash-Copie-quelque-chose-dans]]
- ⬇️ Next: [[Card-181-R181-Test-echo]]
- 📊 MOC: [[_MOC_Slow copy-paste in terminal]]
