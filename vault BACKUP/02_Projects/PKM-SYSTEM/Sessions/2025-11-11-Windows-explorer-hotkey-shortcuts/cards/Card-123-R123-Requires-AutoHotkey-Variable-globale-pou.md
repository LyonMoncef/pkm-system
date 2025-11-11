---
type: chat-card
parent_export: '[[Export]]'
order: 123
role: assistant
created: '2025-11-11T00:47:13.842509Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 123 - Assistant

**ID:** msg-123

## 💬 Content


**ID:** msg-123

MF#Requires AutoHotkey v2.0
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
}Ce code produit ce que je voulais, mais garde le curseur sur la barre dadresse
Je voudrais le focus sur les dossiers actifs pour naviguer par lettre entre les dossiers au clavierAfficher plus

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-122-R122-Requires-AutoHotkey-MonNAS-Partage-WinEM]]
- ⬇️ Next: [[Card-124-R124-Requires-AutoHotkey-Variable-globale-pou]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]
