---
type: chat-card
parent_export: '[[Export]]'
order: 128
role: assistant
created: '2025-11-11T00:47:13.911060Z'
tags:
- chat-card
- code
attachments_count: 0
---

# 🤖 Message 128 - Assistant

**ID:** msg-128

## 💬 Content


**ID:** msg-128

Devised method to shift file explorer focus after navigation.L'utilisateur veut que le focus soit sur la liste des fichiers/dossiers après avoir navigué vers un dossier, pas sur la barre d'adresse. Actuellement, le code envoie !d (Alt+D) pour mettre le focus sur la barre d'adresse, puis envoie le chemin et Enter. Mais après ça, le focus reste dans la barre d'adresse.
Pour mettre le focus sur la liste des fichiers, il faut envoyer une touche supplémentaire après l'Enter. Plusieurs options:

Tab pour passer au volet suivant
F6 pour naviguer entre les panneaux
Escape pour sortir de la barre d'adresse et revenir à la liste
Ou simplement envoyer une touche de direction ou un clic

La solution la plus simple serait probablement d'ajouter un Send(\"{Escape}\") ou Send(\"{Tab}\") après l'Enter, ou mieux encore, envoyer juste un focus sur la liste des fichiers.
Laisse-moi proposer une solution qui fonctionne bien.Parfait ! Il suffit d'ajouter une touche pour ramener le focus sur la liste des fichiers après la navigation. Voici le code corrigé :
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
Si {Escape} ne fonctionne pas parfaitement, essaie de remplacer cette ligne par Send(\"{Tab}\") ou une des autres alternatives.Réessayer

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-127-S127-ID-msg-127]]
- ⬇️ Next: [[Card-129-R129-Devised-method-shift-file-explorer]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]

## 🏷️ Topics

- #code
