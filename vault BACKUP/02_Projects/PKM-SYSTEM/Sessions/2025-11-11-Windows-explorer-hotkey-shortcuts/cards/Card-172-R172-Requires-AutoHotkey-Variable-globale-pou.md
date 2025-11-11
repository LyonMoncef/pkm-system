---
type: chat-card
parent_export: '[[Export]]'
order: 172
role: assistant
created: '2025-11-11T00:47:14.399068Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 172 - Assistant

**ID:** msg-172

## 💬 Content


**ID:** msg-172

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
global RAltPressed := false

; Détecte l'appui sur RAlt
~RAlt:: {
 global LastRAltPress, RAltPressed
 currentTime := A_TickCount

 ; Si double appui en moins de 400ms
 if (currentTime - LastRAltPress < 400 && RAltPressed) {
 ; Menu contextuel étendu (Shift + AppsKey)
 Send(\"+{AppsKey}\")
 LastRAltPress := 0
 RAltPressed := false
 } else {
 ; Premier appui détecté
 RAltPressed := true
 LastRAltPress := currentTime
 ; Timer pour reset si pas de deuxième appui
 SetTimer(() => ResetRAlt(), -450)
 }
}

ResetRAlt() {
 global RAltPressed, LastRAltPress
 ; Si un seul appui, ouvrir menu contextuel normal
 if (RAltPressed) {
 Send(\"{AppsKey}\")
 RAltPressed := false
 LastRAltPress := 0
 }
}

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-171-R171-Parfait-bien-RAlt-droite-problème]]
- ⬇️ Next: [[Card-173-R173-Version-alternative-avec-clic-droit]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]
