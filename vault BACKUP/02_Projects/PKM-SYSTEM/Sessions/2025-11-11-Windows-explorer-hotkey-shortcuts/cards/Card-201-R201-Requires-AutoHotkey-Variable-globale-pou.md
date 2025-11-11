---
type: chat-card
parent_export: '[[Export]]'
order: 201
role: assistant
created: '2025-11-11T00:47:14.729021Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 201 - Assistant

**ID:** msg-201

## 💬 Content


**ID:** msg-201

ahk#Requires AutoHotkey v2.0

; Variable globale pour le chemin NAS
NAS_PATH := \"Z:\\MES DOCUMENTS\"

; ===== Navigation Explorateur avec Win+E =====
#e:: {
 ih := InputHook(\"L1 T1\")
 ih.Start()
 ih.Wait()

 if (ih.EndReason = \"Timeout\") {
 Run(\"explorer.exe\")
 return
 }

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
 if WinExist(\"ahk_class CabinetWClass\") {
 WinActivate
 Send(\"!d\")
 Sleep(50)
 SendInput(path \"{Enter}\")
 Sleep(100)
 Send(\"{Escape}\")
 } else {
 Run('explorer.exe \"' path '\"')
 }
}

; ===== Menu contextuel avec RAlt =====
RAlt:: {
 ih := InputHook(\"L1 T0.4\") ; Attendre 1 touche pendant max 0.4 seconde
 ih.Start()
 ih.Wait()

 if (ih.EndReason = \"Timeout\") {
 ; Aucune touche après RAlt = Menu contextuel étendu
 Send(\"+{F10}\")
 return
 }

 ; Touche appuyée après RAlt
 switch ih.Input {
 case \"Down\": Send(\"+{F10}{Down}\") ; Menu étendu + flèche bas
 default: Send(\"+{F10}\") ; Par défaut menu étendu
 }
}

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-200-R200-Voici-version-simple-claire-Requires]]
- ⬇️ Next: [[Card-202-R202-AhkRAlt-InputHook-Start-Wait-EndReason]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]
