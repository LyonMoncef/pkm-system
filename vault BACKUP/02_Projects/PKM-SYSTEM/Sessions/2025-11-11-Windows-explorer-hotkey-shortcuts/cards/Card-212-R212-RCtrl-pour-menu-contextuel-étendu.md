---
type: chat-card
parent_export: '[[Export]]'
order: 212
role: assistant
created: '2025-11-11T00:47:14.838581Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 212 - Assistant

**ID:** msg-212

## 💬 Content


**ID:** msg-212

ahk; RCtrl pour menu contextuel étendu
RCtrl:: {
 ih := InputHook(\"L1 T0.4\")
 ih.Start()
 ih.Wait()

 if (ih.EndReason = \"Timeout\") {
 Send(\"+{F10}\")
 return
 }

 switch ih.Input {
 case \"0\": {
 Send(\"+{F10}\")
 Sleep(100)
 Send(\"r2\")
 }
 default: Send(\"+{F10}\")
 }
}

; RAlt pour menu contextuel normal
RAlt::Send(\"{AppsKey}\")

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-211-R211-AhkRCtrl-InputHook-Start-Wait-EndReason]]
- ⬇️ Next: [[Card-213-R213-MFError-contain-recognize-action-Specifi]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]
