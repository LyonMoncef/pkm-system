---
type: chat-card
parent_export: '[[Export]]'
order: 251
role: assistant
created: '2025-11-10T03:56:32.168695Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 251 - Assistant

**ID:** msg-251

## 💬 Content


**ID:** msg-251

powershell# Supprime le cache utilisateur Electron
Remove-Item -Recurse -Force \"$env:APPDATA\\Electron\"
Remove-Item -Recurse -Force \"$env:APPDATA\\pkm-system\"

# Supprime node_modules cache
cd C:\\Users\\idsmf\\Projects\\pkm-system\\electron
Remove-Item -Recurse -Force \"node_modules\\.cache\"

---


## 🔗 Navigation

- ⬆️ Previous: [[250_assistant_msg-250]]
- ⬇️ Next: [[252_assistant_msg-252]]
- 📊 MOC: [[_MOC_French chat message instructions]]
