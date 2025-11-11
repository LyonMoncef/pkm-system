---
type: chat-card
parent_export: '[[Export]]'
order: 160
role: assistant
created: '2025-11-11T00:47:14.258367Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 160 - Assistant

**ID:** msg-160

## 💬 Content


**ID:** msg-160

ahkglobal LastLWinPress := 0

LWin:: {
 global LastLWinPress
 currentTime := A_TickCount

 if (currentTime - LastLWinPress < 400) {
 ; Menu contextuel étendu
 Send(\"+{AppsKey}\")
 LastLWinPress := 0
 } else {
 ; Menu contextuel normal
 Send(\"{AppsKey}\")
 LastLWinPress := currentTime
 }
}

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-159-R159-Requires-AutoHotkey-Affiche-quelle-touch]]
- ⬇️ Next: [[Card-161-R161-Ahkglobal-LastRWinPress-RWin-global-Last]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]
