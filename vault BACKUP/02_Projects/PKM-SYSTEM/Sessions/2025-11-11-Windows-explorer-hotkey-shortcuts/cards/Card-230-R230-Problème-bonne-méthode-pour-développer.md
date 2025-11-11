---
type: chat-card
parent_export: '[[Export]]'
order: 230
role: assistant
created: '2025-11-11T00:47:15.012397Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 230 - Assistant

**ID:** msg-230

## 💬 Content


**ID:** msg-230

Le problème c'est que \"r2\" n'est pas la bonne méthode pour développer les options dans le menu contextuel Windows 11/10.
Dans les menus contextuels modernes, l'option \"Afficher plus d'options\" se déclenche différemment. Voici les solutions :
Solution 1 : Utiliser Shift+F10 qui ouvre DÉJÀ le menu étendu
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
Solution 2 : Shift+Clic droit (le plus fiable)
Le Shift+F10 ouvre normalement le menu classique directement. Mais sur Windows 11, il faut parfois faire Shift+Clic droit :
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
Solution 3 : La plus simple - RCtrl+0 fait directement Shift+Clic droit
ahkRCtrl:: {
 ih := InputHook(\"L1 T0.4\")
 ih.Start()
 ih.Wait()

 if (ih.EndReason = \"Timeout\") {
 ; Menu contextuel normal
 Send(\"{AppsKey}\")
 return
 }

 if (ih.Input = \"0\") {
 ; RCtrl+0 = Menu étendu avec Shift
 Send(\"{Shift down}\")
 Send(\"{AppsKey}\")
 Send(\"{Shift up}\")
 } else {
 Send(\"{AppsKey}\")
 }
}
Pour Windows 11 spécifiquement
Sur Windows 11, l'option s'appelle \"Afficher plus d'options\" et son raccourci est généralement Shift+F10 OU tu peux taper la lettre \"s\" (pour \"Show\") ou \"a\" (pour \"Afficher\") selon ta langue :
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
Teste la Solution 3 d'abord (la plus simple avec Shift+AppsKey), et dis-moi si ça ouvre bien le menu classique étendu ! 🎯
Si tu es sur Windows 11, essaie aussi de taper \"a\" après l'ouverture du menu.

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-229-R229-Problème-bonne-méthode-pour-développer]]
- ⬇️ Next: [[Card-231-R231-AhkRCtrl-InputHook-Start-Wait-EndReason]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]
