---
type: chat-card
parent_export: '[[Export]]'
order: 203
role: assistant
created: '2025-11-11T00:47:14.749117Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 203 - Assistant

**ID:** msg-203

## 💬 Content


**ID:** msg-203

MFRCtrl:: {
 ih := InputHook(\"L1 T0.4\")
 ih.Start()
 ih.Wait() if (ih.EndReason = \"Timeout\") {
 Send(\"+{F10}\")
 return
 } switch ih.Input {
 case \"RAlt\": Send \"r2\" ; au lieu de flèche bas, tape \"r2\"
 default: Send \"+{F10}\" ; par défaut menu étendu
 }
}Je veux simuler la séquence R2 dans le menu contextuel suite à l'appui de la touche ctrl avec la touche 0Afficher plus

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-202-R202-AhkRAlt-InputHook-Start-Wait-EndReason]]
- ⬇️ Next: [[Card-204-R204-MFRCtrl-InputHook-Start-Wait-EndReason]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]
