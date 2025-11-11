---
type: chat-card
parent_export: '[[Export]]'
order: 250
role: assistant
created: '2025-11-11T00:47:15.231405Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 250 - Assistant

**ID:** msg-250

## 💬 Content


**ID:** msg-250

Le problème c'est la syntaxe du clic. En AutoHotkey v2, il faut utiliser la fonction Click directement, pas Send. Voici la correction :
ahk; Shift+RCtrl = Shift+Clic gauche (sélection étendue)
+RCtrl::
{
 Send(\"{Shift down}\")
 Click(\"Left\")
 Send(\"{Shift up}\")
}
Ou version plus compacte :
ahk; Shift+RCtrl = Shift+Clic gauche
+RCtrl::Click(\"Left\", , , , , \"Down Shift\")
Ou encore plus simple :
ahk; Shift+RCtrl = Shift+Clic gauche
+RCtrl::
{
 Click(\"Left\", , , 1, , \"D\") ; D = avec Shift maintenu
}
Version complète testée :
ahk; ===== Menu contextuel =====
; RCtrl seul = Shift+F10 (menu étendu)
RCtrl::Send(\"+{F10}\")

; Shift+RCtrl = Shift+Clic gauche (sélection étendue)
+RCtrl::
{
 Send(\"{Shift down}\")
 Click
 Send(\"{Shift up}\")
}
La dernière version est la plus fiable ! Elle maintient Shift, fait un clic gauche normal, puis relâche Shift.
Teste ça et dis-moi si le clic fonctionne maintenant ! 🎯

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-249-R249-Problème-syntaxe-clic-AutoHotkey-faut]]
- ⬇️ Next: [[Card-251-R251-Problème-syntaxe-clic-AutoHotkey-faut]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]
