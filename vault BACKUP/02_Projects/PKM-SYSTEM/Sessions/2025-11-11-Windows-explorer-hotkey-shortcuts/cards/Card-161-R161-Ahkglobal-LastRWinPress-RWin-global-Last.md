---
type: chat-card
parent_export: '[[Export]]'
order: 161
role: assistant
created: '2025-11-11T00:47:14.270326Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 161 - Assistant

**ID:** msg-161

## 💬 Content


**ID:** msg-161

ahkglobal LastRWinPress := 0

RWin:: {
 global LastRWinPress
 currentTime := A_TickCount

 if (currentTime - LastRWinPress < 400) {
 Send(\"+{AppsKey}\")
 LastRWinPress := 0
 } else {
 Send(\"{AppsKey}\")
 LastRWinPress := currentTime
 }
}

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-160-R160-Ahkglobal-LastLWinPress-LWin-global-Last]]
- ⬇️ Next: [[Card-162-R162-Ahkglobal-LastLAltPress-LAlt-global-Last]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]
