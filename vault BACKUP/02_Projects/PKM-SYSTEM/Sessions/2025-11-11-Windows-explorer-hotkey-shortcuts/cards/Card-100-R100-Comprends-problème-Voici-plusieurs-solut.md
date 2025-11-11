---
type: chat-card
parent_export: '[[Export]]'
order: 100
role: assistant
created: '2025-11-11T00:47:13.583231Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 100 - Assistant

**ID:** msg-100

## 💬 Content


**ID:** msg-100

Je comprends ton problème ! Voici plusieurs solutions pour gérer ces séquences proprement en AutoHotkey :
Solution 1 : Intercepter Win+E et attendre la lettre
ahk; Variable globale pour le chemin NAS
NAS_PATH := \"\\\\MonNAS\\Partage\"

; Intercepter Win+E pour éviter l'ouverture automatique
#e::
{
 ; Attendre une touche pendant 1 seconde
 Input, UserInput, L1 T1, {Esc}

 if (ErrorLevel = \"Timeout\" || ErrorLevel = \"NewInput\") {
 ; Si timeout ou autre touche, ouvrir l'Explorateur normalement
 Run, explorer.exe
 return
 }

 ; Sinon, ouvrir le dossier correspondant
 switch UserInput {
 case \"b\": OpenFolder(A_Desktop)
 case \"t\": OpenFolder(A_Desktop . \"\\..\\Downloads\")
 case \"d\": OpenFolder(A_MyDocuments)
 case \"i\": OpenFolder(A_Desktop . \"\\..\\Pictures\")
 case \"v\": OpenFolder(A_Desktop . \"\\..\\Videos\")
 case \"n\": OpenFolder(NAS_PATH)
 case \"a\": OpenFolder(A_AppData)
 case \"s\": OpenFolder(A_Startup)
 case \"p\": OpenFolder(A_StartMenu)
 default: Run, explorer.exe
 }
}

OpenFolder(path) {
 ; Vérifier si une fenêtre Explorateur existe déjà
 if WinExist(\"ahk_class CabinetWClass\") {
 WinActivate
 ; Naviguer vers le nouveau dossier
 Send, !d ; Focus sur la barre d'adresse
 Sleep, 50
 SendInput, %path%{Enter}
 } else {
 ; Sinon ouvrir une nouvelle fenêtre
 Run, explorer.exe \"%path%\"
 }
}
Solution 2 : Utiliser un modificateur différent (plus simple)
ahk; Ctrl+Win+Lettre au lieu de Win+E+Lettre
^#b:: OpenFolder(A_Desktop)
^#t:: OpenFolder(A_Desktop . \"\\..\\Downloads\")
^#d:: OpenFolder(A_MyDocuments)
^#i:: OpenFolder(A_Desktop . \"\\..\\Pictures\")
^#v:: OpenFolder(A_Desktop . \"\\..\\Videos\")
^#n:: OpenFolder(NAS_PATH)
^#a:: OpenFolder(A_AppData)
^#s:: OpenFolder(A_Startup)
^#p:: OpenFolder(A_StartMenu)

OpenFolder(path) {
 if WinExist(\"ahk_class CabinetWClass\")
 WinActivate
 Run, explorer.exe \"%path%\"
}
Solution 3 : Mode séquence avec variable d'état
ahkglobal WinEMode := false

#e::
{
 global WinEMode
 WinEMode := true
 ; Indicateur visuel optionnel
 ToolTip, Mode navigation activé (Win+E)
 ; Timeout de 2 secondes
 SetTimer, ResetWinEMode, -2000
 return
}

ResetWinEMode:
 global WinEMode
 WinEMode := false
 ToolTip
 return

; Les raccourcis suivants
b::HandleShortcut(A_Desktop)
t::HandleShortcut(A_Desktop . \"\\..\\Downloads\")
d::HandleShortcut(A_MyDocuments)
i::HandleShortcut(A_Desktop . \"\\..\\Pictures\")
v::HandleShortcut(A_Desktop . \"\\..\\Videos\")
n::HandleShortcut(NAS_PATH)
a::HandleShortcut(A_AppData)
s::HandleShortcut(A_Startup)
p::HandleShortcut(A_StartMenu)

HandleShortcut(path) {
 global WinEMode
 if (WinEMode) {
 WinEMode := false
 ToolTip
 Run, explorer.exe \"%path%\"
 } else {
 Send, {%A_ThisHotkey%} ; Envoyer la touche normalement
 }
}
Ma recommandation
Je te conseille la Solution 2 (Ctrl+Win+Lettre) car :

✅ Pas de conflit avec les raccourcis Windows natifs
✅ Pas de double fenêtre
✅ Simple et fiable
✅ Une seule combinaison de touches (pas de séquence)

Si tu veux vraiment la séquence Win+E, utilise la Solution 1 qui intercepte Win+E proprement.
Quelle approche préfères-tu ?

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-099-R099-Utilisateur-problème-avec-raccourcis-Aut]]
- ⬇️ Next: [[Card-101-R101-Variable-globale-pour-chemin-MonNAS]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]
