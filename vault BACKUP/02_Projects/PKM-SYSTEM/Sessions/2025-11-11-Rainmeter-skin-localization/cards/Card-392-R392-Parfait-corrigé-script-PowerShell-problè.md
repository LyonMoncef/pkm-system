---
type: chat-card
parent_export: '[[Export]]'
order: 392
role: assistant
created: '2025-11-11T00:21:47.423778Z'
tags:
- chat-card
- python
- automation
attachments_count: 0
---

# 🤖 Message 392 - Assistant

**ID:** msg-392

## 💬 Content


**ID:** msg-392

Parfait ! J'ai corrigé le script PowerShell. Le problème : tous les & dans les URLs doivent être échappés avec `& (backtick + &) en PowerShell.
✅ Correction appliquée
J'ai remplacé tous les & par `& dans les URLs. Par exemple :

❌ Avant : ?api=SYNO.Core.System&version=3&method=info
✅ Après : ?api=SYNO.Core.System`&version=3`&method=info

🔄 Que faire maintenant ?

Remplacez le fichier SynoAPI.ps1 avec le nouveau contenu (artifact mis à jour)
Testez à nouveau :

powershell cd \"Documents\\Rainmeter\\Skins\\SynologyNAS\\@Resources\\Scripts\"
 .\\SynoAPI.ps1 \"192.168.1.141\" \"5000\" \"rainmeter_api\" \"VotreMotDePasse\"
Cette fois ça devrait fonctionner sans erreur ! 🎉
Dites-moi ce qui s'affiche quand vous lancez le script maintenant ! 😊

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-391-R391-Script-PowerShell-pour-récupérer-données]]
- ⬇️ Next: [[Card-393-R393-Powershell-Documents-Rainmeter-Skins-Syn]]
- 📊 MOC: [[_MOC_Rainmeter skin localization]]

## 🏷️ Topics

- #python
- #automation
