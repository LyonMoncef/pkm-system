---
type: chat-card
parent_export: '[[Export]]'
order: 202
role: assistant
created: '2025-11-11T00:47:14.738466Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 202 - Assistant

**ID:** msg-202

## 💬 Content


**ID:** msg-202

ahkRAlt:: {
 ih := InputHook(\"L1 T0.4\")
 ih.Start()
 ih.Wait()

 if (ih.EndReason = \"Timeout\") {
 ; RAlt seul = Menu normal
 Send(\"{AppsKey}\")
 return
 }

 switch ih.Input {
 case \"Down\": {
 ; RAlt + Bas = Menu étendu + développer
 Send(\"+{F10}\")
 Sleep(50)
 Send(\"{Down}\")
 }
 default: Send(\"{AppsKey}\")
 }
}

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-201-R201-Requires-AutoHotkey-Variable-globale-pou]]
- ⬇️ Next: [[Card-203-R203-MFRCtrl-InputHook-Start-Wait-EndReason]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]
