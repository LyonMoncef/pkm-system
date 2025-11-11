---
type: chat-card
parent_export: '[[Export]]'
order: 220
role: assistant
created: '2025-11-11T00:47:14.924577Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 220 - Assistant

**ID:** msg-220

## 💬 Content


**ID:** msg-220

Ah, erreur de syntaxe ! En AutoHotkey v2, quand tu as plusieurs lignes dans un case, il faut utiliser des accolades { } correctement. Voici la correction :
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
Ou version plus compacte (sans accolades pour une seule ligne) :
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
La deuxième version avec if/else est plus claire pour ce cas simple ! 🎯
Teste ça et dis-moi si l'erreur disparaît !

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-219-R219-Erreur-syntaxe-AutoHotkey-quand-plusieur]]
- ⬇️ Next: [[Card-221-R221-AhkRCtrl-InputHook-Start-Wait-EndReason]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]
