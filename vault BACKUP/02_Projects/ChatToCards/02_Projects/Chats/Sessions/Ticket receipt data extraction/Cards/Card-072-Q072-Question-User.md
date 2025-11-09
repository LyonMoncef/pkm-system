---
created: 2025-11-05T20:29:24.967490
updated: 2025-11-05T20:29:24.967490
type: chat-card
chat_message_id: 
chat_message_number: 107
role: user
session: [[MOC-Session-Ticket receipt data extraction]]
tags: [powerbi, expense, chat-card, receipt]
---

# Q072-Question-User

← [[Card-071]] | [[MOC-Session-Ticket receipt data extraction|↑ Session]] | [[Card-073]] →

---

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

**Card 72/106** | Message #107 | Role: user