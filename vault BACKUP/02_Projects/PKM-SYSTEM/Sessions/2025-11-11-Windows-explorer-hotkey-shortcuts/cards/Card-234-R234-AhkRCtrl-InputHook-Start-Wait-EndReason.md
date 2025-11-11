---
type: chat-card
parent_export: '[[Export]]'
order: 234
role: assistant
created: '2025-11-11T00:47:15.059173Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 234 - Assistant

**ID:** msg-234

## 💬 Content


**ID:** msg-234

ahkRCtrl:: {
 ih := InputHook(\"L1 T0.4\")
 ih.Start()
 ih.Wait()

 if (ih.EndReason = \"Timeout\") {
 Send(\"{AppsKey}\")
 return
 }

 if (ih.Input = \"0\") {
 Send(\"{AppsKey}\")
 Sleep(150)
 Send(\"a\") ; \"Afficher plus d'options\" en français
 } else {
 Send(\"{AppsKey}\")
 }
}

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-233-R233-AhkRCtrl-InputHook-Start-Wait-EndReason]]
- ⬇️ Next: [[Card-235-R235-MFok-découpper-RCtrl-Clic-Gauche]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]
