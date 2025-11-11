---
type: chat-card
parent_export: '[[Export]]'
order: 146
role: assistant
created: '2025-11-11T00:47:14.100655Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 146 - Assistant

**ID:** msg-146

## 💬 Content


**ID:** msg-146

Voici le code avec l'ajout de la fonctionnalité Alt droite pour le menu contextuel :
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
Explication des modifications :
Option choisie : {AppsKey} (Touche Menu contextuel)

Simple appui Alt droite → Menu contextuel normal
Double appui rapide (< 400ms) → Menu contextuel étendu (avec Shift)

Alternatives si tu préfères un vrai clic de souris :
ahk; Alternative 1 : Clic droit à la position du curseur
RAlt:: {
 global LastRAltPress
 currentTime := A_TickCount

 if (currentTime - LastRAltPress < 400) {
 ; Menu contextuel étendu (Shift + Clic droit)
 Click(\"Right\", , , , , \"Down Shift\")
 Click(\"Right\", , , , , \"Up\")
 } else {
 ; Menu contextuel normal
 Click(\"Right\")
 LastRAltPress := currentTime
 }
}

; Alternative 2 : Shift + F10 (raccourci Windows standard)
RAlt:: {
 global LastRAltPress
 currentTime := A_TickCount

 if (currentTime - LastRAltPress < 400) {
 Send(\"+{F10}\") ; Menu étendu
 LastRAltPress := 0
 } else {
 Send(\"+{F10}\") ; Menu normal
 LastRAltPress := currentTime
 }
}
Points importants :
✅ {AppsKey} = Touche Menu (entre Alt droite et Ctrl droite sur certains claviers)
✅ Double appui détecté en moins de 400ms
✅ Shift + Menu = Options avancées dans l'Explorateur Windows
Le menu étendu avec Shift affiche par exemple :

\"Copier comme chemin d'accès\"
\"Ouvrir dans le Terminal\"
Plus d'options de partage, etc.

Teste et dis-moi si ça fonctionne comme tu veux ! 🎯Réessayer

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-145-S145-ID-msg-145]]
- ⬇️ Next: [[Card-147-R147-Voici-code-avec-ajout-fonctionnalité]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]
