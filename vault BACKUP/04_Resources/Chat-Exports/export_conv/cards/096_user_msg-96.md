---
type: chat-card
parent_export: '[[🚀 POWER BI / EXCEL POWER PIVOT - Architecture de rêve pour tes tickets
  de caisse !]]'
order: 96
role: user
created: '2025-11-09T20:20:58.861585Z'
tags:
- chat-card
- power-bi
- code
attachments_count: 0
---

# 👤 Message 96 - User

**ID:** msg-96

## 💬 Content

\n\n**ID:** msg-96\n\ndax// === COMPARAISONS TEMPORELLES ===\nCA Mois Précédent = \nCALCULATE(\n    [CA Total],\n    DATEADD(dim_Temps[Date], -1, MONTH)\n)\n\nCA Année Précédente = \nCALCULATE(\n    [CA Total],\n    SAMEPERIODLASTYEAR(dim_Temps[Date])\n)\n\nEvolution vs Mois-1 = \nVAR CAActuel = [CA Total]\nVAR CAMoisPrec = [CA Mois Précédent]\nRETURN\n    DIVIDE(CAActuel - CAMoisPrec, CAMoisPrec, 0) * 100\n\nEvolution vs N-1 = \nVAR CAActuel = [CA Total]\nVAR CAAnPrec = [CA Année Précédente]\nRETURN\n    DIVIDE(CAActuel - CAAnPrec, CAAnPrec, 0) * 100\n\n// === CUMULS ===\nCA YTD = \nTOTALYTD([CA Total], dim_Temps[Date])\n\nCA MTD = \nTOTALMTD([CA Total], dim_Temps[Date])\n\nCA Cumul Mobile 30j = \nCALCULATE(\n    [CA Total],\n    DATESINPERIOD(dim_Temps[Date], LASTDATE(dim_Temps[Date]), -30, DAY)\n)\n\n---\n\n

## 🔗 Navigation

- ⬆️ Previous: [[095_user_msg-95]]
- ⬇️ Next: [[097_user_msg-97]]
- 📊 MOC: [[_MOC_export_conv]]

## 🏷️ Topics

- #power-bi
- #code
