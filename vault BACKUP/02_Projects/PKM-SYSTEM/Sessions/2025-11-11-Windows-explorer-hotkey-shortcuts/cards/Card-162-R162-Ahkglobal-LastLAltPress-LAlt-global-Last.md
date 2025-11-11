---
type: chat-card
parent_export: '[[Export]]'
order: 162
role: assistant
created: '2025-11-11T00:47:14.283630Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 162 - Assistant

**ID:** msg-162

## 💬 Content


**ID:** msg-162

ahkglobal LastLAltPress := 0

LAlt:: {
 global LastLAltPress
 currentTime := A_TickCount

 if (currentTime - LastLAltPress < 400) {
 Send(\"+{AppsKey}\")
 LastLAltPress := 0
 } else {
 Send(\"{AppsKey}\")
 LastLAltPress := currentTime
 }
}

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-161-R161-Ahkglobal-LastRWinPress-RWin-global-Last]]
- ⬇️ Next: [[Card-163-R163-Requires-AutoHotkey-Test-avec-toutes]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]
