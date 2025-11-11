---
type: chat-card
parent_export: '[[Export]]'
order: 145
role: user
created: '2025-11-11T00:47:14.091337Z'
tags:
- chat-card
attachments_count: 0
---

# 👤 Message 145 - User

**ID:** msg-145

## 💬 Content


**ID:** msg-145

#Requires AutoHotkey v2.0
; Variable globale pour le chemin NAS
NAS_PATH := \"Z:\\MES DOCUMENTS\"
; Intercepter Win+E
#e:: {
 ; Attendre une touche pendant 1 seconde
 ih := InputHook(\"L1 T1\")
 ih.Start()
 ih.Wait() if (ih.EndReason = \"Timeout\") {
 ; Si timeout, ouvrir l'Explorateur normalement
 Run(\"explorer.exe\")
 return
 } ; Sinon, ouvrir le dossier correspondant
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
}Ce code est ok,Maintenant je veux que l'appui de la touche alt droite, simule un clic gauche menu contextuel
On peut dans l'explorateur développer plus d'options supplémentaires par exemple
ça doit pouvoir se faire en faisant une double touche successive alt droite

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-144-R144-Requires-AutoHotkey-Variable-globale-pou]]
- ⬇️ Next: [[Card-146-R146-Voici-code-avec-ajout-fonctionnalité]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]
