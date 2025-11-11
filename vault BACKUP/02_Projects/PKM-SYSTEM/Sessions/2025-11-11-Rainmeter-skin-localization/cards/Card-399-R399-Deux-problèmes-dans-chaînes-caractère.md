---
type: chat-card
parent_export: '[[Export]]'
order: 399
role: assistant
created: '2025-11-11T00:21:47.481528Z'
tags:
- chat-card
- python
- automation
attachments_count: 0
---

# 🤖 Message 399 - Assistant

**ID:** msg-399

## 💬 Content


**ID:** msg-399

Ah, deux problèmes : le % dans les chaînes et le caractère ✓ qui ne passe pas bien. Je corrige :Script PowerShell - API SynologyCode ∙ Version 3  $data.volume_used = \"$usedGB GB\"
 $data.volume_total = \"$totalGB GB\"
 $data.volume_percent = \"$percent\"
 Write-Host \" Volume 1: $usedGB GB / $totalGB GB ($percent%)\" -NoNewline
 Write-Host \"\"Parfait ! J'ai corrigé les deux problèmes :

Le symbole % dans Write-Host : J'ai ajouté -NoNewline pour éviter le conflit
Le caractère ✓ : Remplacé par [char]0x2713 qui est le code Unicode pour le checkmark

Le script devrait maintenant fonctionner parfaitement ! Testez à nouveau :
powershell.\\SynoAPI.ps1 \"192.168.1.141\" \"5000\" \"rainmeter_api\" \"VotreMotDePasse\"
Qu'est-ce que ça donne ? 🤞Réessayer

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-398-S398-ID-msg-398]]
- ⬇️ Next: [[Card-400-R400-Deux-problèmes-dans-chaînes-caractère]]
- 📊 MOC: [[_MOC_Rainmeter skin localization]]

## 🏷️ Topics

- #python
- #automation
