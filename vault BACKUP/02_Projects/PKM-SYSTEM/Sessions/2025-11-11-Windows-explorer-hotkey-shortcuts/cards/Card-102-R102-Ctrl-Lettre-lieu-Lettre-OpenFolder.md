---
type: chat-card
parent_export: '[[Export]]'
order: 102
role: assistant
created: '2025-11-11T00:47:13.605788Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 102 - Assistant

**ID:** msg-102

## 💬 Content


**ID:** msg-102

ahk; Ctrl+Win+Lettre au lieu de Win+E+Lettre
^#b:: OpenFolder(A_Desktop)
^#t:: OpenFolder(A_Desktop . \"\\..\\Downloads\")
^#d:: OpenFolder(A_MyDocuments)
^#i:: OpenFolder(A_Desktop . \"\\..\\Pictures\")
^#v:: OpenFolder(A_Desktop . \"\\..\\Videos\")
^#n:: OpenFolder(NAS_PATH)
^#a:: OpenFolder(A_AppData)
^#s:: OpenFolder(A_Startup)
^#p:: OpenFolder(A_StartMenu)

OpenFolder(path) {
 if WinExist(\"ahk_class CabinetWClass\")
 WinActivate
 Run, explorer.exe \"%path%\"
}

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-101-R101-Variable-globale-pour-chemin-MonNAS]]
- ⬇️ Next: [[Card-103-R103-Ahkglobal-WinEMode-false-global-WinEMode]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]
