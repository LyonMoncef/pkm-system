---
type: chat-card
parent_export: '[[Export]]'
order: 233
role: assistant
created: '2025-11-11T00:47:15.052060Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 233 - Assistant

**ID:** msg-233

## 💬 Content


**ID:** msg-233

ahkRCtrl:: {
 ih := InputHook(\"L1 T0.4\")
 ih.Start()
 ih.Wait()

 if (ih.EndReason = \"Timeout\") {
 ; Menu contextuel normal
 Send(\"{AppsKey}\")
 return
 }

 if (ih.Input = \"0\") {
 ; RCtrl+0 = Menu étendu avec Shift
 Send(\"{Shift down}\")
 Send(\"{AppsKey}\")
 Send(\"{Shift up}\")
 } else {
 Send(\"{AppsKey}\")
 }
}

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-232-R232-AhkRCtrl-InputHook-Start-Wait-EndReason]]
- ⬇️ Next: [[Card-234-R234-AhkRCtrl-InputHook-Start-Wait-EndReason]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]
