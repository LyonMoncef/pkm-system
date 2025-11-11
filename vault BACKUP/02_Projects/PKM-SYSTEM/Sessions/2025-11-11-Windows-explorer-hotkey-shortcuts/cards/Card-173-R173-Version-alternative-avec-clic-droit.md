---
type: chat-card
parent_export: '[[Export]]'
order: 173
role: assistant
created: '2025-11-11T00:47:14.412410Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 173 - Assistant

**ID:** msg-173

## 💬 Content


**ID:** msg-173

ahk; Version alternative avec clic droit direct
~RAlt:: {
 global LastRAltPress
 currentTime := A_TickCount

 if (currentTime - LastRAltPress < 400) {
 ; Double appui = Menu étendu avec Shift+Clic droit
 Send(\"+{F10}\") ; Shift+F10 = menu contextuel étendu
 LastRAltPress := 0
 } else {
 ; Simple appui = Menu contextuel normal
 Send(\"{F10}\") ; F10 seul ne marche pas, utilisons AppsKey
 Send(\"{AppsKey}\")
 LastRAltPress := currentTime
 }
}

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-172-R172-Requires-AutoHotkey-Variable-globale-pou]]
- ⬇️ Next: [[Card-174-R174-Test-basique-RAlt-menu-contextuel]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]
