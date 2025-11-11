---
type: chat-card
parent_export: '[[Export]]'
order: 149
role: assistant
created: '2025-11-11T00:47:14.130202Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 149 - Assistant

**ID:** msg-149

## 💬 Content


**ID:** msg-149

ahk#Requires AutoHotkey v2.0

; Variable globale pour le chemin NAS
NAS_PATH := \"Z:\\MES DOCUMENTS\"

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
 case \"&\": OpenFolder(\"C:\\Program Files\")
 case \"é\": OpenFolder(\"C:\\Program Files (x86)\")
 case \"c\": OpenFolder(\"C:\\\")
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
 Sleep(100) ; Attendre que la navigation se fasse
 Send(\"{Escape}\") ; Sortir de la barre d'adresse et revenir à la liste
 } else {
 ; Sinon ouvrir une nouvelle fenêtre
 Run('explorer.exe \"' path '\"')
 }
}

; ===== Menu contextuel avec Alt Droite =====
global LastRAltPress := 0

RAlt:: {
 global LastRAltPress
 currentTime := A_TickCount

 ; Si double appui en moins de 400ms
 if (currentTime - LastRAltPress < 400) {
 ; Menu contextuel étendu (Shift + Clic droit)
 Send(\"+{AppsKey}\") ; Shift + Menu contextuel
 LastRAltPress := 0 ; Reset pour éviter triple appui
 } else {
 ; Simple appui = menu contextuel normal
 Send(\"{AppsKey}\") ; Touche Menu (équivalent clic droit)
 LastRAltPress := currentTime
 }
}

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-148-R148-Voici-code-avec-ajout-fonctionnalité]]
- ⬇️ Next: [[Card-150-R150-Alternative-Clic-droit-position-curseur]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]
