---
type: chat-card
parent_export: '[[Export]]'
order: 103
role: assistant
created: '2025-11-11T00:47:13.614747Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 103 - Assistant

**ID:** msg-103

## 💬 Content


**ID:** msg-103

ahkglobal WinEMode := false

#e::
{
 global WinEMode
 WinEMode := true
 ; Indicateur visuel optionnel
 ToolTip, Mode navigation activé (Win+E)
 ; Timeout de 2 secondes
 SetTimer, ResetWinEMode, -2000
 return
}

ResetWinEMode:
 global WinEMode
 WinEMode := false
 ToolTip
 return

; Les raccourcis suivants
b::HandleShortcut(A_Desktop)
t::HandleShortcut(A_Desktop . \"\\..\\Downloads\")
d::HandleShortcut(A_MyDocuments)
i::HandleShortcut(A_Desktop . \"\\..\\Pictures\")
v::HandleShortcut(A_Desktop . \"\\..\\Videos\")
n::HandleShortcut(NAS_PATH)
a::HandleShortcut(A_AppData)
s::HandleShortcut(A_Startup)
p::HandleShortcut(A_StartMenu)

HandleShortcut(path) {
 global WinEMode
 if (WinEMode) {
 WinEMode := false
 ToolTip
 Run, explorer.exe \"%path%\"
 } else {
 Send, {%A_ThisHotkey%} ; Envoyer la touche normalement
 }
}

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-102-R102-Ctrl-Lettre-lieu-Lettre-OpenFolder]]
- ⬇️ Next: [[Card-104-R104-MFIt-looks-like-script-trying]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]
