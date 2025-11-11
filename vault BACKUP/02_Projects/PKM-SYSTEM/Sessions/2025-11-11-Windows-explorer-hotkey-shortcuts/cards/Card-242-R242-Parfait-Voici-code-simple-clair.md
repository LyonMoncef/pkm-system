---
type: chat-card
parent_export: '[[Export]]'
order: 242
role: assistant
created: '2025-11-11T00:47:15.139881Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 242 - Assistant

**ID:** msg-242

## 💬 Content


**ID:** msg-242

Parfait ! Voici le code simple et clair :
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

; ===== Menu contextuel =====
; RCtrl seul = Shift+F10 (menu étendu)
RCtrl::Send(\"+{F10}\")

; Shift+RCtrl = Shift+Clic gauche (sélection étendue)
+RCtrl::Send(\"+{Click}\")
Explication :
✅ RCtrl → Shift+F10 (menu contextuel étendu)
✅ Shift+RCtrl → Shift+Clic gauche (sélection multiple/étendue)
Simple, efficace et sans séquence ! 🎯

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-241-R241-Parfait-Voici-code-simple-clair]]
- ⬇️ Next: [[Card-243-R243-Requires-AutoHotkey-Variable-globale-pou]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]
