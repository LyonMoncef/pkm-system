---
type: chat-card
parent_export: '[[Export]]'
order: 183
role: assistant
created: '2025-11-11T00:47:14.524453Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 183 - Assistant

**ID:** msg-183

## 💬 Content


**ID:** msg-183

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
global LastRAltTime := 0

RAlt:: {
 global LastRAltTime
 currentTime := A_TickCount
 timeSinceLastPress := currentTime - LastRAltTime

 ; Si double appui en moins de 300ms
 if (timeSinceLastPress > 0 && timeSinceLastPress < 300) {
 ; Menu contextuel étendu (avec Shift)
 Send(\"+{AppsKey}\")
 LastRAltTime := 0 ; Reset pour éviter un triple appui
 } else {
 ; Simple appui = menu contextuel normal
 Send(\"{AppsKey}\")
 LastRAltTime := currentTime
 }
}

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-182-R182-Parfait-Voici-version-avec-double]]
- ⬇️ Next: [[Card-184-R184-MFlà-fonctionne-plus]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]
