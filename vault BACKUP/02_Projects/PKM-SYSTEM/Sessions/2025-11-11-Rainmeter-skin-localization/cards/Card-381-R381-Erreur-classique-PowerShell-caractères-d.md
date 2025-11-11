---
type: chat-card
parent_export: '[[Export]]'
order: 381
role: assistant
created: '2025-11-11T00:21:47.326747Z'
tags:
- chat-card
- python
- automation
attachments_count: 0
---

# 🤖 Message 381 - Assistant

**ID:** msg-381

## 💬 Content


**ID:** msg-381

Ah ! Erreur classique de PowerShell ! Les caractères & dans les URLs doivent être échappés. Je corrige le script :Script PowerShell - API SynologyCode ∙ Version 2 # Script PowerShell pour récupérer les données du NAS Synology
# Usage: .\\SynoAPI.ps1 <IP> <PORT> <USER> <PASSWORD>

param(
 [string]$NAS_IP = \"192.168.1.141\",
 [string]$NAS_PORT = \"5000\",
 [string]$NAS_USER = \"rainmeter_api\",
 [string]$NParfait ! J'ai corrigé le script PowerShell. Le problème : tous les & dans les URLs doivent être échappés avec `& (backtick + &) en PowerShell.
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
Dites-moi ce qui s'affiche quand vous lancez le script maintenant ! 😊Réessayer

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-380-S380--ysURL-baseURLentrycgi]]
- ⬇️ Next: [[Card-382-R382-Erreur-classique-PowerShell-caractères-d]]
- 📊 MOC: [[_MOC_Rainmeter skin localization]]

## 🏷️ Topics

- #python
- #automation
