---
created: 2025-11-05T20:29:24.838875
updated: 2025-11-05T20:29:24.838875
type: chat-card
chat_message_id: 
chat_message_number: 99
role: user
session: [[MOC-Session-Ticket receipt data extraction]]
tags: [powerbi, expense, chat-card, receipt]
---

# Q064-Question-User

← [[Card-063]] | [[MOC-Session-Ticket receipt data extraction|↑ Session]] | [[Card-065]] →

---

dax// === VENTES ===
CA Total = SUM(fact_Achats[PrixFinal])

CA Brut = SUM(fact_Achats[PrixTotal])

Total Remises = SUM(fact_Achats[MontantRemise])

Taux Remise % = 
DIVIDE([Total Remises], [CA Brut], 0) * 100

Panier Moyen = 
DIVIDE([CA Total], DISTINCTCOUNT(fact_Achats[TicketID]), 0)

Nombre Articles = SUM(fact_Achats[Quantite])

Articles par Ticket = 
DIVIDE([Nombre Articles], DISTINCTCOUNT(fact_Achats[TicketID]), 0)

// === TVA ===
Total TVA = SUM(fact_Achats[MontantTVA])

Total HT = SUM(fact_Achats[MontantHT])

// === TRANSACTIONS ===
Nombre Tickets = DISTINCTCOUNT(fact_Achats[TicketID])

Nombre Transactions = COUNTROWS(fact_Achats)

---

**Card 64/106** | Message #99 | Role: user