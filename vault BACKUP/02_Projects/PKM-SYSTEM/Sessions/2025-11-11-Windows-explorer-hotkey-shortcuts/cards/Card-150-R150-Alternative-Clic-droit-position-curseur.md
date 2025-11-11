---
type: chat-card
parent_export: '[[Export]]'
order: 150
role: assistant
created: '2025-11-11T00:47:14.141022Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 150 - Assistant

**ID:** msg-150

## 💬 Content


**ID:** msg-150

ahk; Alternative 1 : Clic droit à la position du curseur
RAlt:: {
 global LastRAltPress
 currentTime := A_TickCount

 if (currentTime - LastRAltPress < 400) {
 ; Menu contextuel étendu (Shift + Clic droit)
 Click(\"Right\", , , , , \"Down Shift\")
 Click(\"Right\", , , , , \"Up\")
 } else {
 ; Menu contextuel normal
 Click(\"Right\")
 LastRAltPress := currentTime
 }
}

; Alternative 2 : Shift + F10 (raccourci Windows standard)
RAlt:: {
 global LastRAltPress
 currentTime := A_TickCount

 if (currentTime - LastRAltPress < 400) {
 Send(\"+{F10}\") ; Menu étendu
 LastRAltPress := 0
 } else {
 Send(\"+{F10}\") ; Menu normal
 LastRAltPress := currentTime
 }
}

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-149-R149-Requires-AutoHotkey-Variable-globale-pou]]
- ⬇️ Next: [[Card-151-R151-MFça-marche-mais-touche-correspond]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]
