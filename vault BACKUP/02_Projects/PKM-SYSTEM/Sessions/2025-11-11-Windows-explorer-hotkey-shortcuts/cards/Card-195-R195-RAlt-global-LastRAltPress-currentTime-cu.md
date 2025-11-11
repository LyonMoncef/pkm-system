---
type: chat-card
parent_export: '[[Export]]'
order: 195
role: assistant
created: '2025-11-11T00:47:14.677093Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 195 - Assistant

**ID:** msg-195

## 💬 Content


**ID:** msg-195

MF~RAlt:: {
 global LastRAltPress
 currentTime := A_TickCount if (currentTime - LastRAltPress < 400) {
 ; Double appui = Menu étendu avec Shift+Clic droit
 Send(\"+{F10}\") ; Shift+F10 = menu contextuel étendu
 LastRAltPress := 0
 } else {
 ; Simple appui = Menu contextuel normal
 Send(\"{F10}\") ; F10 seul ne marche pas, utilisons AppsKey
 Send(\"{AppsKey}\")
 LastRAltPress := currentTime
 }
}Inspire toi de ce code mais en version plus simple
Avec RAlt qui envoie shift F10
L'option R2 étant disponible, mappe le sur la flèche du bas pour développer les optionsDonc sur le même esprit que la séquence de touches win e + dossier de destinationAfficher plus

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-194-R194-RAlt-global-LastRAltPress-currentTime-cu]]
- ⬇️ Next: [[Card-196-R196-RAlt-global-LastRAltPress-currentTime-cu]]
- 📊 MOC: [[_MOC_Windows explorer hotkey shortcuts]]
