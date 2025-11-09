---
created: 2025-11-05T20:29:24.957896
updated: 2025-11-05T20:29:24.957896
type: chat-card
chat_message_id: 
chat_message_number: 106
role: user
session: [[MOC-Session-Ticket receipt data extraction]]
tags: [powerbi, expense, chat-card, receipt]
---

# Q071-Question-User

← [[Card-070]] | [[MOC-Session-Ticket receipt data extraction|↑ Session]] | [[Card-072]] →

---

dax        JoursDepuisDerniereVisite <= 90, 3,
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
        ScoreTotal >= 544, "🌟 Champions",
        ScoreTotal >= 434, "💎 Fidèles",
        ScoreTotal >= 334, "⭐ Potentiel",
        ScoreTotal >= 244, "⚠️ À Risque",
        ScoreTotal >= 144, "😴 Hibernants",
        "❌ Perdus"
    )

---

**Card 71/106** | Message #106 | Role: user