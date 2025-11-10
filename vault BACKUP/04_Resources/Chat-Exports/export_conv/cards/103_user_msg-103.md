---
type: chat-card
parent_export: '[[🚀 POWER BI / EXCEL POWER PIVOT - Architecture de rêve pour tes tickets
  de caisse !]]'
order: 103
role: user
created: '2025-11-09T20:20:58.938627Z'
tags:
- chat-card
- power-bi
- code
attachments_count: 0
---

# 👤 Message 103 - User

**ID:** msg-103

## 💬 Content

\n\n**ID:** msg-103\n\ndax// Index de Saisonnalité\nIndice_Saisonnier = \nVAR CAMoisActuel = [CA Total]\nVAR CAMoyenAnnuel = \n    CALCULATE(\n        [CA Total],\n        ALL(dim_Temps[Mois])\n    ) / 12\nRETURN\n    DIVIDE(CAMoisActuel, CAMoyenAnnuel, 0) * 100\n\nMois_le_Plus_Fort = \n    CALCULATE(\n        FIRSTNONBLANK(dim_Temps[MoisNom], 1),\n        TOPN(1, ALL(dim_Temps[MoisNom]), [CA Total], DESC)\n    )\n\nMois_le_Plus_Faible = \n    CALCULATE(\n        FIRSTNONBLANK(dim_Temps[MoisNom], 1),\n        TOPN(1, ALL(dim_Temps[MoisNom]), [CA Total], ASC)\n    )\n\n// Comparaison Week-end vs Semaine\nPerformance_Weekend = \nVAR CAWeekend = CALCULATE([CA Total], dim_Temps[EstWeekend] = 1)\nVAR CAMoyenJour = DIVIDE([CA Total], DISTINCTCOUNT(dim_Temps[Date]), 0)\nRETURN\n    DIVIDE(CAWeekend, CAMoyenJour, 0)\n\n---\n\n

## 🔗 Navigation

- ⬆️ Previous: [[102_user_msg-102]]
- ⬇️ Next: [[104_user_msg-104]]
- 📊 MOC: [[_MOC_export_conv]]

## 🏷️ Topics

- #power-bi
- #code
