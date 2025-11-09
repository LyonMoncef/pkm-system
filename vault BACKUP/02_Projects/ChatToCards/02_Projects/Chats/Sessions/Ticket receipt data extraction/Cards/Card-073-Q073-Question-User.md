---
created: 2025-11-05T20:29:24.979550
updated: 2025-11-05T20:29:24.979550
type: chat-card
chat_message_id: 
chat_message_number: 108
role: user
session: [[MOC-Session-Ticket receipt data extraction]]
tags: [powerbi, expense, chat-card, receipt]
---

# Q073-Question-User

← [[Card-072]] | [[MOC-Session-Ticket receipt data extraction|↑ Session]] | [[Card-074]] →

---

dax// Index de Saisonnalité
Indice_Saisonnier = 
VAR CAMoisActuel = [CA Total]
VAR CAMoyenAnnuel = 
    CALCULATE(
        [CA Total],
        ALL(dim_Temps[Mois])
    ) / 12
RETURN
    DIVIDE(CAMoisActuel, CAMoyenAnnuel, 0) * 100

Mois_le_Plus_Fort = 
    CALCULATE(
        FIRSTNONBLANK(dim_Temps[MoisNom], 1),
        TOPN(1, ALL(dim_Temps[MoisNom]), [CA Total], DESC)
    )

Mois_le_Plus_Faible = 
    CALCULATE(
        FIRSTNONBLANK(dim_Temps[MoisNom], 1),
        TOPN(1, ALL(dim_Temps[MoisNom]), [CA Total], ASC)
    )

// Comparaison Week-end vs Semaine
Performance_Weekend = 
VAR CAWeekend = CALCULATE([CA Total], dim_Temps[EstWeekend] = 1)
VAR CAMoyenJour = DIVIDE([CA Total], DISTINCTCOUNT(dim_Temps[Date]), 0)
RETURN
    DIVIDE(CAWeekend, CAMoyenJour, 0)

---

**Card 73/106** | Message #108 | Role: user