---
created: 2025-11-05T20:29:24.851602
updated: 2025-11-05T20:29:24.851602
type: chat-card
chat_message_id: 
chat_message_number: 100
role: user
session: [[MOC-Session-Ticket receipt data extraction]]
tags: [powerbi, expense, chat-card, receipt]
---

# Q065-Question-User

← [[Card-064]] | [[MOC-Session-Ticket receipt data extraction|↑ Session]] | [[Card-066]] →

---

dax// === COMPARAISONS TEMPORELLES ===
CA Mois Précédent = 
CALCULATE(
    [CA Total],
    DATEADD(dim_Temps[Date], -1, MONTH)
)

CA Année Précédente = 
CALCULATE(
    [CA Total],
    SAMEPERIODLASTYEAR(dim_Temps[Date])
)

Evolution vs Mois-1 = 
VAR CAActuel = [CA Total]
VAR CAMoisPrec = [CA Mois Précédent]
RETURN
    DIVIDE(CAActuel - CAMoisPrec, CAMoisPrec, 0) * 100

Evolution vs N-1 = 
VAR CAActuel = [CA Total]
VAR CAAnPrec = [CA Année Précédente]
RETURN
    DIVIDE(CAActuel - CAAnPrec, CAAnPrec, 0) * 100

// === CUMULS ===
CA YTD = 
TOTALYTD([CA Total], dim_Temps[Date])

CA MTD = 
TOTALMTD([CA Total], dim_Temps[Date])

CA Cumul Mobile 30j = 
CALCULATE(
    [CA Total],
    DATESINPERIOD(dim_Temps[Date], LASTDATE(dim_Temps[Date]), -30, DAY)
)

---

**Card 65/106** | Message #100 | Role: user