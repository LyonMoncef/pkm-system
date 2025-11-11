---
type: chat-card
parent_export: '[[Export]]'
order: 210
role: assistant
created: '2025-11-11T00:47:14.814264Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 210 - Assistant

**ID:** msg-210

## 💬 Content


**ID:** msg-210

Voici le code corrigé pour simuler \"R2\" dans le menu contextuel :
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
Explication :
✅ RCtrl seul → Menu contextuel étendu (Shift+F10)
✅ RCtrl + 0 → Menu étendu, puis simule la frappe \"r2\" pour sélectionner l'option
Le Sleep(100) laisse le temps au menu de s'ouvrir avant de taper \"r2\".
Si tu veux que RAlt fonctionne aussi :
ahk; RCtrl pour menu contextuel étendu
RCtrl:: {
 ih := InputHook(\"L1 T0.4\")
 ih.Start()
 ih.Wait()

 if (ih.EndReason = \"Timeout\") {
 Send(\"+{F10}\")
 return
 }

 switch ih.Input {
 case \"0\": {
 Send(\"+{F10}\")
 Sleep(100)
 Send(\"r2\")
 }
 default: Send(\"+{F10}\")
 }
}

; RAlt pour menu contextuel normal
RAlt::Send(\"{AppsKey}\")
Teste et dis-moi si le \"r2\" se tape bien dans le menu ! Si le timing est trop court, on peut augmenter le Sleep(100) à 150 ou 200. 🎯

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-209-R209-Voici-code-corrigé-pour-simuler]]
- ⬇️ Next: [[Card-211-R211-AhkRCtrl-InputHook-Start-Wait-EndReason]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]
