---
type: chat-card
parent_export: '[[Export]]'
order: 163
role: assistant
created: '2025-11-11T00:47:14.291550Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 163 - Assistant

**ID:** msg-163

## 💬 Content


**ID:** msg-163

ahk#Requires AutoHotkey v2.0

; Test avec toutes les touches Alt/Win possibles
~LWin::CheckDoublePress(\"LWin\")
~RWin::CheckDoublePress(\"RWin\")
~LAlt::CheckDoublePress(\"LAlt\")
~RAlt::CheckDoublePress(\"RAlt\")

global LastPress := Map()

CheckDoublePress(keyName) {
 global LastPress
 currentTime := A_TickCount

 if (!LastPress.Has(keyName)) {
 LastPress[keyName] := 0
 }

 if (currentTime - LastPress[keyName] < 400) {
 ; Double appui détecté
 Send(\"+{AppsKey}\")
 ToolTip(\"Menu étendu avec \" keyName)
 SetTimer(() => ToolTip(), -2000)
 LastPress[keyName] := 0
 } else {
 ; Simple appui
 Send(\"{AppsKey}\")
 ToolTip(\"Menu normal avec \" keyName)
 SetTimer(() => ToolTip(), -2000)
 LastPress[keyName] := currentTime
 }
}

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-162-R162-Ahkglobal-LastLAltPress-LAlt-global-Last]]
- ⬇️ Next: [[Card-164-R164-MFça-affiche-RAlt-droite]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]
