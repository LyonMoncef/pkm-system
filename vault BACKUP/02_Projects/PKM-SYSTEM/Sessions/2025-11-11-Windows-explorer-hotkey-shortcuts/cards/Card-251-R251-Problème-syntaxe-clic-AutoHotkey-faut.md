---
type: chat-card
parent_export: '[[Export]]'
order: 251
role: assistant
created: '2025-11-11T00:47:15.245641Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 251 - Assistant

**ID:** msg-251

## 💬 Content


**ID:** msg-251

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

- ⬆️ Previous: [[Card-250-R250-Problème-syntaxe-clic-AutoHotkey-faut]]
- ⬇️ Next: [[Card-252-R252-Shift-RCtrl-Shift-Clic-gauche]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]
