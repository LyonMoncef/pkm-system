---
type: chat-card
parent_export: '[[🚀 POWER BI / EXCEL POWER PIVOT - Architecture de rêve pour tes tickets
  de caisse !]]'
order: 107
role: user
created: '2025-11-09T20:20:58.976382Z'
tags:
- chat-card
- power-bi
- finance
- code
attachments_count: 0
---

# 👤 Message 107 - User

**ID:** msg-107

## 💬 Content

\n\n**ID:** msg-107\n\ndax// Utiliser des variables pour éviter les recalculs\nMesure_Optimisee = \nVAR _CA = [CA Total]\nVAR _Tickets = [Nombre Tickets]\nVAR _Panier = DIVIDE(_CA, _Tickets, 0)\nRETURN\n    IF(_Panier > 100, \"Premium\", \"Standard\")\n\n// Plutôt que de recalculer [CA Total] et [Nombre Tickets] plusieurs fois\n```\n\n### **Formatage conditionnel avancé :**\n```\n// Dans Power BI, créer une mesure pour le format\nCouleur_Performance = \nVAR Perf = [Evolution vs N-1]\nRETURN\n    SWITCH(\n        TRUE(),\n        Perf > 10, \"#00FF00\",  // Vert\n        Perf > 0, \"#90EE90\",   // Vert clair\n        Perf > -5, \"#FFD700\",  // Jaune\n        Perf > -10, \"#FFA500\", // Orange\n        \"#FF0000\"               // Rouge\n    )\n\n---\n\n

## 🔗 Navigation

- ⬆️ Previous: [[106_user_msg-106]]
- ⬇️ Next: [[108_user_msg-108]]
- 📊 MOC: [[_MOC_export_conv]]

## 🏷️ Topics

- #power-bi
- #finance
- #code
