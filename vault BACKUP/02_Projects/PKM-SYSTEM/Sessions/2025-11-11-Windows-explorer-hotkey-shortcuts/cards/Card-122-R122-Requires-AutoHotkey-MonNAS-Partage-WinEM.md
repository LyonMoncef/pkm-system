---
type: chat-card
parent_export: '[[Export]]'
order: 122
role: assistant
created: '2025-11-11T00:47:13.830482Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 122 - Assistant

**ID:** msg-122

## 💬 Content


**ID:** msg-122

ahk#Requires AutoHotkey v2.0

NAS_PATH := \"\\\\MonNAS\\Partage\"
WinEMode := false

#e:: {
 global WinEMode
 WinEMode := true
 ToolTip(\"Mode navigation activé (Win+E)\")
 SetTimer(() => ResetMode(), -2000)
}

ResetMode() {
 global WinEMode
 WinEMode := false
 ToolTip()
}

; Raccourcis contextuels
b:: HandleShortcut(A_Desktop)
t:: HandleShortcut(A_Desktop \"\\..\\Downloads\")
d:: HandleShortcut(A_MyDocuments)
i:: HandleShortcut(A_Desktop \"\\..\\Pictures\")
v:: HandleShortcut(A_Desktop \"\\..\\Videos\")
n:: HandleShortcut(NAS_PATH)
a:: HandleShortcut(A_AppData)
s:: HandleShortcut(A_Startup)
p:: HandleShortcut(A_StartMenu)

HandleShortcut(path) {
 global WinEMode
 if (WinEMode) {
 WinEMode := false
 ToolTip()
 Run('explorer.exe \"' path '\"')
 } else {
 Send(\"{\" A_ThisHotkey \"}\")
 }
}

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-121-R121-Requires-AutoHotkey-Variable-globale-Mon]]
- ⬇️ Next: [[Card-123-R123-Requires-AutoHotkey-Variable-globale-pou]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]
