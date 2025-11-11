---
type: chat-card
parent_export: '[[Export]]'
order: 221
role: assistant
created: '2025-11-11T00:47:14.932330Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 221 - Assistant

**ID:** msg-221

## 💬 Content


**ID:** msg-221

ahkRCtrl:: {
 ih := InputHook(\"L1 T0.4\")
 ih.Start()
 ih.Wait()

 if (ih.EndReason = \"Timeout\") {
 Send(\"+{F10}\")
 return
 }

 switch ih.Input {
 case \"0\":
 {
 ; Ctrl + 0 = Menu étendu puis tape \"r2\"
 Send(\"+{F10}\")
 Sleep(100)
 Send(\"r2\")
 }
 default:
 {
 Send(\"+{F10}\")
 }
 }
}

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-220-R220-Erreur-syntaxe-AutoHotkey-quand-plusieur]]
- ⬇️ Next: [[Card-222-R222-AhkRCtrl-InputHook-Start-Wait-EndReason]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]
