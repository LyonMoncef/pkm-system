---
type: chat-card
parent_export: '[[Export]]'
order: 222
role: assistant
created: '2025-11-11T00:47:14.942161Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 222 - Assistant

**ID:** msg-222

## 💬 Content


**ID:** msg-222

ahkRCtrl:: {
 ih := InputHook(\"L1 T0.4\")
 ih.Start()
 ih.Wait()

 if (ih.EndReason = \"Timeout\") {
 Send(\"+{F10}\")
 return
 }

 if (ih.Input = \"0\") {
 Send(\"+{F10}\")
 Sleep(100)
 Send(\"r2\")
 } else {
 Send(\"+{F10}\")
 }
}

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-221-R221-AhkRCtrl-InputHook-Start-Wait-EndReason]]
- ⬇️ Next: [[Card-223-R223-Erreur-disparait-mais-dans-tous]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]
