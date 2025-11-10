---
type: chat-card
parent_export: '[[Export]]'
order: 180
role: assistant
created: '2025-11-11T00:41:53.115442Z'
tags:
- chat-card
- power-bi
- finance
- code
attachments_count: 0
---

# 🤖 Message 180 - Assistant

**ID:** msg-180

## 💬 Content


**ID:** msg-180

dax JoursDepuisDerniereVisite <= 90, 3,
 JoursDepuisDerniereVisite <= 180, 2,
 1
 )

Score_Frequency =
VAR NbVisites = [Frequence Achat]
RETURN
 SWITCH(
 TRUE(),
 NbVisites >= 10, 5,
 NbVisites >= 7, 4,
 NbVisites >= 5, 3,
 NbVisites >= 3, 2,
 1
 )

Score_Monetary =
VAR CAClient = [CA Total]
VAR CAMoyen = CALCULATE([CA Total], ALL(fact_Achats)) / DISTINCTCOUNT(fact_Achats[TicketID])
RETURN
 SWITCH(
 TRUE(),
 CAClient >= CAMoyen * 2, 5,
 CAClient >= CAMoyen * 1.5, 4,
 CAClient >= CAMoyen, 3,
 CAClient >= CAMoyen * 0.5, 2,
 1
 )

Score_RFM_Total =
 [Score_Recency] * 100 + [Score_Frequency] * 10 + [Score_Monetary]

Segment_Client_RFM =
VAR ScoreTotal = [Score_RFM_Total]
RETURN
 SWITCH(
 TRUE(),
 ScoreTotal >= 544, \"🌟 Champions\",
 ScoreTotal >= 434, \"💎 Fidèles\",
 ScoreTotal >= 334, \"⭐ Potentiel\",
 ScoreTotal >= 244, \"⚠️ À Risque\",
 ScoreTotal >= 144, \"😴 Hibernants\",
 \"❌ Perdus\"
 )

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-179-R179-JoursDepuisDerniereVisite-JoursDepuisDer]]
- ⬇️ Next: [[Card-181-R181-Tendance-Linéaire-simple-MinDate-Date]]
- 📊 MOC: [[_MOC_Ticket receipt data extraction]]

## 🏷️ Topics

- #power-bi
- #finance
- #code
