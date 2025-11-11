---
type: chat-card
parent_export: '[[Export]]'
order: 509
role: assistant
created: '2025-11-11T00:21:48.389023Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 509 - Assistant

**ID:** msg-509

## 💬 Content


**ID:** msg-509

Parfait ! Voici comment ça fonctionne maintenant :
🎨 Système de couleur globale par jour
📋 Dans GlobalVariables.inc :

Mesures globales ajoutées :

measureGlobalDayNumber : Détecte le jour de la semaine
measureGlobalDayColor : Change automatiquement colorDynamic


Variable colorDynamic :

Change automatiquement chaque jour
Utilisée par TOUS les skins


📝 Dans Clock.ini :

Simplifié : Plus besoin de measureDayNumber et measureDayColor locaux
Utilise directement #colorDynamic# des variables globales
DynamicVariables=1 sur tous les styles pour voir les changements


🌈 Résultat :
TOUS vos skins (Clock, System, Disk, Network, NAS) auront maintenant la même couleur qui change selon le jour :

🔴 Dimanche : Rouge
🟢 Lundi : Vert
🟠 Mardi : Orange
🟡 Mercredi : Jaune
🟣 Jeudi : Violet
🔵 Vendredi : Bleu
🟠 Samedi : Orange


✅ Pour appliquer à vos autres skins :
Dans System.ini, Disk.ini, Network.ini :
Remplacez FontColor=#colorText# par FontColor=#colorDynamic# dans tous les styles, et ajoutez DynamicVariables=1.
Exemple :
ini[styleLeftText]
FontColor=#colorDynamic# ← Au lieu de #colorText#
DynamicVariables=1 ← Ajouter cette ligne
Testez Clock.ini maintenant, la couleur devrait changer selon le jour ! 🎉

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-508-R508-FICHIER-VARIABLES-GLOBALES-placer-dans]]
- ⬇️ Next: [[Card-510-R510-StyleLeftText-FontColor-colorDynamic-lie]]
- 📊 MOC: [[_MOC_Rainmeter skin localization]]
