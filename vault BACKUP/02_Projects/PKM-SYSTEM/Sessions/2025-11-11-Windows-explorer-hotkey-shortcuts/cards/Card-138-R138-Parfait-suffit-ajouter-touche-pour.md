---
type: chat-card
parent_export: '[[Export]]'
order: 138
role: assistant
created: '2025-11-11T00:47:14.026618Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 138 - Assistant

**ID:** msg-138

## 💬 Content


**ID:** msg-138

Parfait ! Il suffit d'ajouter une touche pour ramener le focus sur la liste des fichiers après la navigation. Voici le code corrigé :
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
Modifications apportées :

Ajout de Sleep(100) après l'Enter pour laisser le temps à l'Explorateur de naviguer
Ajout de Send(\"{Escape}\") pour quitter la barre d'adresse et mettre le focus sur la liste des fichiers

Alternatives si Escape ne marche pas bien :
ahk; Option 1 : Utiliser Tab pour naviguer vers la liste
Send(\"{Tab}\")

; Option 2 : Utiliser F6 pour changer de panneau
Send(\"{F6}\")

; Option 3 : Simuler un clic sur la liste (plus robuste)
Sleep(100)
ControlFocus(\"DirectUIHWND3\", \"ahk_class CabinetWClass\")
Maintenant tu peux naviguer directement au clavier en tapant les premières lettres des dossiers ! 🎯
Si {Escape} ne fonctionne pas parfaitement, essaie de remplacer cette ligne par Send(\"{Tab}\") ou une des autres alternatives.

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-137-R137-Utilisateur-veut-focus-soit-liste]]
- ⬇️ Next: [[Card-139-R139-Requires-AutoHotkey-Variable-globale-pou]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]
