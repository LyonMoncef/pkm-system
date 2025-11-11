---
type: chat-card
parent_export: '[[Export]]'
order: 232
role: assistant
created: '2025-11-11T00:47:15.035567Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 232 - Assistant

**ID:** msg-232

## 💬 Content


**ID:** msg-232

ahkRCtrl:: {
 ih := InputHook(\"L1 T0.4\")
 ih.Start()
 ih.Wait()

 if (ih.EndReason = \"Timeout\") {
 ; Shift + Clic droit = menu classique complet
 Click(\"Right\", , , , , \"Down Shift\")
 Sleep(50)
 Click(\"Right\", , , , , \"Up\")
 return
 }

 if (ih.Input = \"0\") {
 ; Menu normal puis cherche \"Afficher plus d'options\"
 Send(\"{AppsKey}\")
 Sleep(100)
 Send(\"s\") ; Raccourci clavier pour \"Show more options\" (langue système)
 } else {
 Send(\"+{F10}\")
 }
}

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-231-R231-AhkRCtrl-InputHook-Start-Wait-EndReason]]
- ⬇️ Next: [[Card-233-R233-AhkRCtrl-InputHook-Start-Wait-EndReason]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]
