---
type: chat-card
parent_export: '[[Export]]'
order: 181
role: assistant
created: '2025-11-11T00:41:53.123428Z'
tags:
- chat-card
- power-bi
- code
attachments_count: 0
---

# 🤖 Message 181 - Assistant

**ID:** msg-181

## 💬 Content


**ID:** msg-181

dax// Tendance Linéaire (simple)
CA_Tendance =
VAR MinDate = MIN(dim_Temps[Date])
VAR MaxDate = MAX(dim_Temps[Date])
VAR NbJours = DATEDIFF(MinDate, MaxDate, DAY)
VAR SommeX = SUMX(ALL(dim_Temps[Date]), DATEDIFF(MinDate, dim_Temps[Date], DAY))
VAR SommeY = CALCULATE([CA Total], ALL(dim_Temps[Date]))
VAR SommeXY = SUMX(ALL(dim_Temps[Date]), DATEDIFF(MinDate, dim_Temps[Date], DAY) * [CA Total])
VAR SommeX2 = SUMX(ALL(dim_Temps[Date]), POWER(DATEDIFF(MinDate, dim_Temps[Date], DAY), 2))
VAR N = COUNTROWS(ALL(dim_Temps[Date]))
VAR Slope = DIVIDE((N * SommeXY) - (SommeX * SommeY), (N * SommeX2) - POWER(SommeX, 2))
VAR Intercept = DIVIDE(SommeY - (Slope * SommeX), N)
VAR XActuel = DATEDIFF(MinDate, MAX(dim_Temps[Date]), DAY)
RETURN
 Intercept + (Slope * XActuel)

Variance_vs_Tendance =
 [CA Total] - [CA_Tendance]

// Prévision Moyenne Mobile
CA_Moyenne_Mobile_7j =
 AVERAGEX(
 DATESINPERIOD(dim_Temps[Date], LASTDATE(dim_Temps[Date]), -7, DAY),
 [CA Total]
 )

CA_Prevision_Demain =
 [CA_Moyenne_Mobile_7j]

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-180-R180-JoursDepuisDerniereVisite-JoursDepuisDer]]
- ⬇️ Next: [[Card-182-R182-Index-Saisonnalité-CAMoisActuel-Total-CA]]
- 📊 MOC: [[_MOC_Ticket receipt data extraction]]

## 🏷️ Topics

- #power-bi
- #code
