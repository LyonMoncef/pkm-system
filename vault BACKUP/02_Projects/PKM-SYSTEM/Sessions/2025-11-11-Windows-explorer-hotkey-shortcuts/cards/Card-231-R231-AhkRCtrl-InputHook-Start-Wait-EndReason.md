---
type: chat-card
parent_export: '[[Export]]'
order: 231
role: assistant
created: '2025-11-11T00:47:15.020554Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 231 - Assistant

**ID:** msg-231

## 💬 Content


**ID:** msg-231

ahkRCtrl:: {
 ih := InputHook(\"L1 T0.4\")
 ih.Start()
 ih.Wait()

 if (ih.EndReason = \"Timeout\") {
 ; Menu contextuel étendu (ancien style Windows)
 Send(\"+{F10}\")
 return
 }

 if (ih.Input = \"0\") {
 ; Si Windows 11 avec nouveau menu, il faut cliquer sur \"Afficher plus d'options\"
 Send(\"{AppsKey}\") ; Ouvre le nouveau menu
 Sleep(150)
 Send(\"{Down}{Down}{Down}{Down}{Down}{Enter}\") ; Descend jusqu'à \"Afficher plus\"
 } else {
 Send(\"+{F10}\")
 }
}

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-230-R230-Problème-bonne-méthode-pour-développer]]
- ⬇️ Next: [[Card-232-R232-AhkRCtrl-InputHook-Start-Wait-EndReason]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]
