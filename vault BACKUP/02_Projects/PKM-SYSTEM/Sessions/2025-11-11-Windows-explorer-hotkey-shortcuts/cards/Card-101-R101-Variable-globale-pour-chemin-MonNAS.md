---
type: chat-card
parent_export: '[[Export]]'
order: 101
role: assistant
created: '2025-11-11T00:47:13.591464Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 101 - Assistant

**ID:** msg-101

## 💬 Content


**ID:** msg-101

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

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-100-R100-Comprends-problème-Voici-plusieurs-solut]]
- ⬇️ Next: [[Card-102-R102-Ctrl-Lettre-lieu-Lettre-OpenFolder]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]
