---
type: chat-card
parent_export: '[[Export]]'
order: 207
role: user
created: '2025-11-11T00:47:14.788756Z'
tags:
- chat-card
attachments_count: 0
---

# 👤 Message 207 - User

**ID:** msg-207

## 💬 Content


**ID:** msg-207

RCtrl:: {
 ih := InputHook(\"L1 T0.4\")
 ih.Start()
 ih.Wait() if (ih.EndReason = \"Timeout\") {
 Send(\"+{F10}\")
 return
 } switch ih.Input {
 case \"RAlt\": Send \"r2\" ; au lieu de flèche bas, tape \"r2\"
 default: Send \"+{F10}\" ; par défaut menu étendu
 }
}Je veux simuler la séquence R2 dans le menu contextuel suite à l'appui de la touche ctrl avec la touche 0

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-206-R206-RCtrl-InputHook-Start-Wait-EndReason]]
- ⬇️ Next: [[Card-208-R208-Voici-code-corrigé-pour-simuler]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]
