---
type: chat-card
parent_export: '[[Export]]'
order: 158
role: assistant
created: '2025-11-11T00:47:14.236961Z'
tags:
- chat-card
- python
- git
- automation
attachments_count: 0
---

# 🤖 Message 158 - Assistant

**ID:** msg-158

## 💬 Content


**ID:** msg-158

Ah, tu as un clavier Mac/Logitech avec une touche Cmd/Alt ! Sur ces claviers, cette touche peut être mappée différemment. Testons d'abord quelle est vraiment cette touche :
1️⃣ Script de détection de touche
Copie ce code pour identifier ta touche :
ahk#Requires AutoHotkey v2.0

; Affiche quelle touche tu appuies
~*SC056::ToolTip(\"SC056 - ISO <> key\")
~*LWin::ToolTip(\"LWin - Windows gauche\")
~*RWin::ToolTip(\"RWin - Windows droite\")
~*LAlt::ToolTip(\"LAlt - Alt gauche\")
~*RAlt::ToolTip(\"RAlt - Alt droite\")
~*LControl::ToolTip(\"LControl - Ctrl gauche\")
~*RControl::ToolTip(\"RControl - Ctrl droite\")
~*AppsKey::ToolTip(\"AppsKey - Menu contextuel\")

; Efface le tooltip après 2 secondes
F12::ToolTip()
Instructions :

Lance ce script
Appuie sur ta touche Cmd/Alt
Note ce qui s'affiche dans le tooltip
Appuie sur F12 pour effacer

2️⃣ Solutions possibles selon ta touche
Si c'est LWin (touche Windows gauche) :
ahkglobal LastLWinPress := 0

LWin:: {
 global LastLWinPress
 currentTime := A_TickCount

 if (currentTime - LastLWinPress < 400) {
 ; Menu contextuel étendu
 Send(\"+{AppsKey}\")
 LastLWinPress := 0
 } else {
 ; Menu contextuel normal
 Send(\"{AppsKey}\")
 LastLWinPress := currentTime
 }
}
Si c'est RWin (touche Windows droite) :
ahkglobal LastRWinPress := 0

RWin:: {
 global LastRWinPress
 currentTime := A_TickCount

 if (currentTime - LastRWinPress < 400) {
 Send(\"+{AppsKey}\")
 LastRWinPress := 0
 } else {
 Send(\"{AppsKey}\")
 LastRWinPress := currentTime
 }
}
Si c'est LAlt (Alt gauche) :
ahkglobal LastLAltPress := 0

LAlt:: {
 global LastLAltPress
 currentTime := A_TickCount

 if (currentTime - LastLAltPress < 400) {
 Send(\"+{AppsKey}\")
 LastLAltPress := 0
 } else {
 Send(\"{AppsKey}\")
 LastLAltPress := currentTime
 }
}
3️⃣ Alternative : Utiliser le logiciel Logitech Options+
Le Logitech Craft peut être configuré avec Logitech Options+. Tu peux :

Vérifier comment la touche Cmd/Alt est mappée
La remapper si nécessaire

4️⃣ Solution universelle (détecte automatiquement)
Si tu veux tester sans savoir exactement quelle touche c'est :
ahk#Requires AutoHotkey v2.0

; Test avec toutes les touches Alt/Win possibles
~LWin::CheckDoublePress(\"LWin\")
~RWin::CheckDoublePress(\"RWin\")
~LAlt::CheckDoublePress(\"LAlt\")
~RAlt::CheckDoublePress(\"RAlt\")

global LastPress := Map()

CheckDoublePress(keyName) {
 global LastPress
 currentTime := A_TickCount

 if (!LastPress.Has(keyName)) {
 LastPress[keyName] := 0
 }

 if (currentTime - LastPress[keyName] < 400) {
 ; Double appui détecté
 Send(\"+{AppsKey}\")
 ToolTip(\"Menu étendu avec \" keyName)
 SetTimer(() => ToolTip(), -2000)
 LastPress[keyName] := 0
 } else {
 ; Simple appui
 Send(\"{AppsKey}\")
 ToolTip(\"Menu normal avec \" keyName)
 SetTimer(() => ToolTip(), -2000)
 LastPress[keyName] := currentTime
 }
}
Lance d'abord le script de détection (étape 1) et dis-moi ce qui s'affiche quand tu appuies sur ta touche Cmd/Alt ! 🔍

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-157-R157-Clavier-Logitech-avec-touche-claviers]]
- ⬇️ Next: [[Card-159-R159-Requires-AutoHotkey-Affiche-quelle-touch]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]

## 🏷️ Topics

- #python
- #git
- #automation
