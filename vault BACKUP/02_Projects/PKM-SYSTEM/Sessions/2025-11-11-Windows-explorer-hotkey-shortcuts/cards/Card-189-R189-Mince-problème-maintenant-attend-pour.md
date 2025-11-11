---
type: chat-card
parent_export: '[[Export]]'
order: 189
role: assistant
created: '2025-11-11T00:47:14.608025Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 189 - Assistant

**ID:** msg-189

## 💬 Content


**ID:** msg-189

Ah mince ! Le problème c'est que maintenant il attend pour détecter le double appui. Essayons avec un timer pour que le simple appui fonctionne immédiatement si pas de deuxième appui :
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
Comment ça fonctionne maintenant :
✅ Un appui → Attend 250ms, puis ouvre le menu normal
✅ Double appui rapide → Annule l'attente et ouvre directement le menu étendu
Si tu trouves que 250ms d'attente c'est trop long, on peut réduire à 150ms ou 200ms.
Teste ça et dis-moi si ça marche mieux ! 🎯Réessayer

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-188-S188-ID-msg-188]]
- ⬇️ Next: [[Card-190-R190-Mince-problème-maintenant-attend-pour]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]
