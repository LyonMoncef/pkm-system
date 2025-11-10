---
type: chat-card
parent_export: '[[🚀 POWER BI / EXCEL POWER PIVOT - Architecture de rêve pour tes tickets
  de caisse !]]'
order: 101
role: user
created: '2025-11-09T20:20:58.913226Z'
tags:
- chat-card
- power-bi
- finance
- code
attachments_count: 0
---

# 👤 Message 101 - User

**ID:** msg-101

## 💬 Content

\n\n**ID:** msg-101\n\ndax        JoursDepuisDerniereVisite <= 90, 3,\n        JoursDepuisDerniereVisite <= 180, 2,\n        1\n    )\n\nScore_Frequency = \nVAR NbVisites = [Frequence Achat]\nRETURN\n    SWITCH(\n        TRUE(),\n        NbVisites >= 10, 5,\n        NbVisites >= 7, 4,\n        NbVisites >= 5, 3,\n        NbVisites >= 3, 2,\n        1\n    )\n\nScore_Monetary = \nVAR CAClient = [CA Total]\nVAR CAMoyen = CALCULATE([CA Total], ALL(fact_Achats)) / DISTINCTCOUNT(fact_Achats[TicketID])\nRETURN\n    SWITCH(\n        TRUE(),\n        CAClient >= CAMoyen * 2, 5,\n        CAClient >= CAMoyen * 1.5, 4,\n        CAClient >= CAMoyen, 3,\n        CAClient >= CAMoyen * 0.5, 2,\n        1\n    )\n\nScore_RFM_Total = \n    [Score_Recency] * 100 + [Score_Frequency] * 10 + [Score_Monetary]\n\nSegment_Client_RFM = \nVAR ScoreTotal = [Score_RFM_Total]\nRETURN\n    SWITCH(\n        TRUE(),\n        ScoreTotal >= 544, \"🌟 Champions\",\n        ScoreTotal >= 434, \"💎 Fidèles\",\n        ScoreTotal >= 334, \"⭐ Potentiel\",\n        ScoreTotal >= 244, \"⚠️ À Risque\",\n        ScoreTotal >= 144, \"😴 Hibernants\",\n        \"❌ Perdus\"\n    )\n\n---\n\n

## 🔗 Navigation

- ⬆️ Previous: [[100_assistant_msg-100]]
- ⬇️ Next: [[102_user_msg-102]]
- 📊 MOC: [[_MOC_export_conv]]

## 🏷️ Topics

- #power-bi
- #finance
- #code
