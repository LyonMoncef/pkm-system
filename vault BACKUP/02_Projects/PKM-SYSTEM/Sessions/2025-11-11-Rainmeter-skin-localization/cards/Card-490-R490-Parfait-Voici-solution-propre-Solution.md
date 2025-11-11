---
type: chat-card
parent_export: '[[Export]]'
order: 490
role: assistant
created: '2025-11-11T00:21:48.239353Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 490 - Assistant

**ID:** msg-490

## 💬 Content


**ID:** msg-490

Parfait ! Voici la solution propre :
✅ Solution mise en place
📝 Principe :

colorText : Couleur globale pour tous les skins normaux
colorTextDynamic : Couleur spéciale pour Clock qui change selon le jour
colorSunday, colorMonday, etc. : Couleurs définies globalement mais utilisées uniquement par Clock

🎨 Résultat :

Tous les autres skins (System, Disk, Network, NAS) utilisent #colorText# (blanc)
Clock uniquement utilise #colorTextDynamic# qui change chaque jour
Les couleurs des jours sont dans GlobalVariables.inc, donc modifiables centralement

🔄 Pour changer les couleurs des jours :
Éditez GlobalVariables.inc :
ini; Changez toutes les couleurs des jours en une fois !
colorSunday=255,50,50,205 ; Rouge (dimanche)
colorMonday=50,200,50,205 ; Vert (lundi)
colorTuesday=255,165,0,205 ; Orange (mardi)
; etc.
🌈 Pour changer la couleur de tous les autres skins :
inicolorText=100,200,255,205 ; Bleu clair pour System, Disk, Network, NAS

📊 Récapitulatif :
SkinVariable utiliséeComportementClock#colorTextDynamic#Change selon le jourSystem#colorText#Blanc fixeDisk#colorText#Blanc fixeNetwork#colorText#Blanc fixeNAS#colorText#Blanc fixe
Testez maintenant ! Tous vos skins devraient avoir la même couleur, sauf Clock qui change chaque jour ! 🎉

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-489-R489-COULEURS-PRINCIPALES-Format-Rouge-Vert]]
- ⬇️ Next: [[Card-491-R491-Changez-toutes-couleurs-jours-fois]]
- 📊 MOC: [[_MOC_Rainmeter skin localization]]
