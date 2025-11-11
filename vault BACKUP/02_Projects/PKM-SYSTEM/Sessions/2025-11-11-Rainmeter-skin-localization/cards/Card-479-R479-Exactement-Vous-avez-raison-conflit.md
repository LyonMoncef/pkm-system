---
type: chat-card
parent_export: '[[Export]]'
order: 479
role: assistant
created: '2025-11-11T00:21:48.151726Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 479 - Assistant

**ID:** msg-479

## 💬 Content


**ID:** msg-479

Exactement ! Vous avez raison. Il y a un conflit entre :

Variables globales : pour la cohérence visuelle
Couleur dynamique du Clock : qui change selon le jour

Voici les solutions possibles :
💡 Solution 1 : Variables de couleur séparées (RECOMMANDÉ)Variables Globales - GlobalVariables.incCode ∙ Version 2 ; ----------------------------------
; COULEURS PRINCIPALES
; ----------------------------------
; Format: Rouge,Vert,Bleu,Alpha (0-255)
colorBar=235,170,0,255
colorText=255,255,255,205
colorTextDynamic=255,255,255,205
colorBackground=0,0,0,100

; CoParfait ! Voici la solution propre :
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
Testez maintenant ! Tous vos skins devraient avoir la même couleur, sauf Clock qui change chaque jour ! 🎉Réessayer

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-478-S478-ID-msg-478]]
- ⬇️ Next: [[Card-480-R480-Exactement-Vous-avez-raison-conflit]]
- 📊 MOC: [[_MOC_Rainmeter skin localization]]
