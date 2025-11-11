---
type: chat-card
parent_export: '[[Export]]'
order: 121
role: assistant
created: '2025-11-11T00:47:13.813999Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 121 - Assistant

**ID:** msg-121

## 💬 Content


**ID:** msg-121

ahk#Requires AutoHotkey v2.0

; Variable globale
NAS_PATH := \"\\\\MonNAS\\Partage\"

; Raccourcis Ctrl+Win+Lettre
^#b:: OpenFolder(A_Desktop)
^#t:: OpenFolder(A_Desktop \"\\..\\Downloads\")
^#d:: OpenFolder(A_MyDocuments)
^#i:: OpenFolder(A_Desktop \"\\..\\Pictures\")
^#v:: OpenFolder(A_Desktop \"\\..\\Videos\")
^#n:: OpenFolder(NAS_PATH)
^#a:: OpenFolder(A_AppData)
^#s:: OpenFolder(A_Startup)
^#p:: OpenFolder(A_StartMenu)

OpenFolder(path) {
 Run('explorer.exe \"' path '\"')
}

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-120-R120-Requires-AutoHotkey-Variable-globale-pou]]
- ⬇️ Next: [[Card-122-R122-Requires-AutoHotkey-MonNAS-Partage-WinEM]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]
