---
type: chat-card
parent_export: '[[Export]]'
order: 211
role: assistant
created: '2025-11-11T00:47:14.826836Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 211 - Assistant

**ID:** msg-211

## 💬 Content


**ID:** msg-211

ahkRCtrl:: {
 ih := InputHook(\"L1 T0.4\")
 ih.Start()
 ih.Wait()

 if (ih.EndReason = \"Timeout\") {
 Send(\"+{F10}\")
 return
 }

 switch ih.Input {
 case \"0\": {
 ; Ctrl + 0 = Menu étendu puis tape \"r2\"
 Send(\"+{F10}\")
 Sleep(100) ; Attendre que le menu s'ouvre
 Send(\"r2\")
 }
 default: Send(\"+{F10}\")
 }
}

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-210-R210-Voici-code-corrigé-pour-simuler]]
- ⬇️ Next: [[Card-212-R212-RCtrl-pour-menu-contextuel-étendu]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]
