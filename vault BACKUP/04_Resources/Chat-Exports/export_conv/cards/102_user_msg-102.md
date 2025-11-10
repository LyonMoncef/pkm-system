---
type: chat-card
parent_export: '[[🚀 POWER BI / EXCEL POWER PIVOT - Architecture de rêve pour tes tickets
  de caisse !]]'
order: 102
role: user
created: '2025-11-09T20:20:58.925581Z'
tags:
- chat-card
- power-bi
- code
attachments_count: 0
---

# 👤 Message 102 - User

**ID:** msg-102

## 💬 Content

\n\n**ID:** msg-102\n\ndax// Tendance Linéaire (simple)\nCA_Tendance = \nVAR MinDate = MIN(dim_Temps[Date])\nVAR MaxDate = MAX(dim_Temps[Date])\nVAR NbJours = DATEDIFF(MinDate, MaxDate, DAY)\nVAR SommeX = SUMX(ALL(dim_Temps[Date]), DATEDIFF(MinDate, dim_Temps[Date], DAY))\nVAR SommeY = CALCULATE([CA Total], ALL(dim_Temps[Date]))\nVAR SommeXY = SUMX(ALL(dim_Temps[Date]), DATEDIFF(MinDate, dim_Temps[Date], DAY) * [CA Total])\nVAR SommeX2 = SUMX(ALL(dim_Temps[Date]), POWER(DATEDIFF(MinDate, dim_Temps[Date], DAY), 2))\nVAR N = COUNTROWS(ALL(dim_Temps[Date]))\nVAR Slope = DIVIDE((N * SommeXY) - (SommeX * SommeY), (N * SommeX2) - POWER(SommeX, 2))\nVAR Intercept = DIVIDE(SommeY - (Slope * SommeX), N)\nVAR XActuel = DATEDIFF(MinDate, MAX(dim_Temps[Date]), DAY)\nRETURN\n    Intercept + (Slope * XActuel)\n\nVariance_vs_Tendance = \n    [CA Total] - [CA_Tendance]\n\n// Prévision Moyenne Mobile\nCA_Moyenne_Mobile_7j = \n    AVERAGEX(\n        DATESINPERIOD(dim_Temps[Date], LASTDATE(dim_Temps[Date]), -7, DAY),\n        [CA Total]\n    )\n\nCA_Prevision_Demain = \n    [CA_Moyenne_Mobile_7j]\n\n---\n\n

## 🔗 Navigation

- ⬆️ Previous: [[101_user_msg-101]]
- ⬇️ Next: [[103_user_msg-103]]
- 📊 MOC: [[_MOC_export_conv]]

## 🏷️ Topics

- #power-bi
- #code
