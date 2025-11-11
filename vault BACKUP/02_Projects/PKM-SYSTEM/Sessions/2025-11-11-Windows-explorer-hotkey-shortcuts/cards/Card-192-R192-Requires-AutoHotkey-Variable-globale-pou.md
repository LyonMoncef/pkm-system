---
type: chat-card
parent_export: '[[Export]]'
order: 192
role: assistant
created: '2025-11-11T00:47:14.643568Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 192 - Assistant

**ID:** msg-192

## 💬 Content


**ID:** msg-192

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
global RAltClickCount := 0

RAlt:: {
 global RAltClickCount
 RAltClickCount++

 ; Premier appui
 if (RAltClickCount = 1) {
 ; Attendre 250ms pour voir si double appui
 SetTimer(RAltSingleClick, -250)
 }
 ; Deuxième appui
 else if (RAltClickCount = 2) {
 ; Annuler le timer du simple clic
 SetTimer(RAltSingleClick, 0)
 ; Menu étendu immédiatement
 Send(\"+{AppsKey}\")
 RAltClickCount := 0
 }
}

RAltSingleClick() {
 global RAltClickCount
 if (RAltClickCount = 1) {
 ; Simple clic = menu normal
 Send(\"{AppsKey}\")
 }
 RAltClickCount := 0
}

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-191-R191-Mince-problème-maintenant-attend-pour]]
- ⬇️ Next: [[Card-193-R193-RAlt-global-LastRAltPress-currentTime-cu]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]
