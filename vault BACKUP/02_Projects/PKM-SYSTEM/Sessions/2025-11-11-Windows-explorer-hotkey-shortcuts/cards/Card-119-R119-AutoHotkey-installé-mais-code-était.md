---
type: chat-card
parent_export: '[[Export]]'
order: 119
role: assistant
created: '2025-11-11T00:47:13.793837Z'
tags:
- chat-card
- code
attachments_count: 0
---

# 🤖 Message 119 - Assistant

**ID:** msg-119

## 💬 Content


**ID:** msg-119

Tu as AutoHotkey v2 installé, mais mon code était en syntaxe v1 ! Voici les versions corrigées pour AutoHotkey v2 :
Solution 1 : Win+E puis lettre (AutoHotkey v2)
ahk#Requires AutoHotkey v2.0

; Variable globale pour le chemin NAS
NAS_PATH := \"\\\\MonNAS\\Partage\"

; Intercepter Win+E
#e:: {
 ; Attendre une touche pendant 1 seconde
 ih := InputHook(\"L1 T1\")
 ih.Start()
 ih.Wait()

 if (ih.EndReason = \"Timeout\") {
 ; Si timeout, ouvrir l'Explorateur normalement
 Run(\"explorer.exe\")
 return
 }

 ; Sinon, ouvrir le dossier correspondant
 switch ih.Input {
 case \"b\": OpenFolder(A_Desktop)
 case \"t\": OpenFolder(A_Desktop \"\\..\\Downloads\")
 case \"d\": OpenFolder(A_MyDocuments)
 case \"i\": OpenFolder(A_Desktop \"\\..\\Pictures\")
 case \"v\": OpenFolder(A_Desktop \"\\..\\Videos\")
 case \"n\": OpenFolder(NAS_PATH)
 case \"a\": OpenFolder(A_AppData)
 case \"s\": OpenFolder(A_Startup)
 case \"p\": OpenFolder(A_StartMenu)
 default: Run(\"explorer.exe\")
 }
}

OpenFolder(path) {
 ; Vérifier si une fenêtre Explorateur existe déjà
 if WinExist(\"ahk_class CabinetWClass\") {
 WinActivate
 ; Naviguer vers le nouveau dossier
 Send(\"!d\") ; Focus sur la barre d'adresse
 Sleep(50)
 SendInput(path \"{Enter}\")
 } else {
 ; Sinon ouvrir une nouvelle fenêtre
 Run('explorer.exe \"' path '\"')
 }
}
Solution 2 : Ctrl+Win+Lettre (RECOMMANDÉ - plus simple)
ahk#Requires AutoHotkey v2.0

; Variable globale
NAS_PATH := \"\\\\MonNAS\\Partage\"

; Raccourcis Ctrl+Win+Lettre
^#b:: OpenFolder(A_Desktop)
^#t:: OpenFolder(A_Desktop \"\\..\\Downloads\")
^#d:: OpenFolder(A_MyDocuments)
^#i:: OpenFolder(A_Desktop \"\\..\\Pictures\")
^#v:: OpenFolder(A_Desktop \"\\..\\Videos\")
^#n:: OpenFolder(NAS_PATH)
^#a:: OpenFolder(A_AppData)
^#s:: OpenFolder(A_Startup)
^#p:: OpenFolder(A_StartMenu)

OpenFolder(path) {
 Run('explorer.exe \"' path '\"')
}
Solution 3 : Mode séquence avec variable d'état
ahk#Requires AutoHotkey v2.0

NAS_PATH := \"\\\\MonNAS\\Partage\"
WinEMode := false

#e:: {
 global WinEMode
 WinEMode := true
 ToolTip(\"Mode navigation activé (Win+E)\")
 SetTimer(() => ResetMode(), -2000)
}

ResetMode() {
 global WinEMode
 WinEMode := false
 ToolTip()
}

; Raccourcis contextuels
b:: HandleShortcut(A_Desktop)
t:: HandleShortcut(A_Desktop \"\\..\\Downloads\")
d:: HandleShortcut(A_MyDocuments)
i:: HandleShortcut(A_Desktop \"\\..\\Pictures\")
v:: HandleShortcut(A_Desktop \"\\..\\Videos\")
n:: HandleShortcut(NAS_PATH)
a:: HandleShortcut(A_AppData)
s:: HandleShortcut(A_Startup)
p:: HandleShortcut(A_StartMenu)

HandleShortcut(path) {
 global WinEMode
 if (WinEMode) {
 WinEMode := false
 ToolTip()
 Run('explorer.exe \"' path '\"')
 } else {
 Send(\"{\" A_ThisHotkey \"}\")
 }
}
Principales différences v1 → v2 :

#Requires AutoHotkey v2.0 au début
Les accolades {} sont obligatoires pour les fonctions
Run(), Send(), WinExist() avec parenthèses
Concaténation avec espace au lieu de . : \"texte \" variable
InputHook() au lieu de Input
SetTimer(() => Function(), -2000) avec fonction lambda

Je recommande la Solution 2 pour commencer - c'est la plus simple et fiable !
Tu peux copier le code directement, ça devrait marcher maintenant 👍

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-118-R118-Utilisateur-erreur-AutoHotkey-message-in]]
- ⬇️ Next: [[Card-120-R120-Requires-AutoHotkey-Variable-globale-pou]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]

## 🏷️ Topics

- #code
