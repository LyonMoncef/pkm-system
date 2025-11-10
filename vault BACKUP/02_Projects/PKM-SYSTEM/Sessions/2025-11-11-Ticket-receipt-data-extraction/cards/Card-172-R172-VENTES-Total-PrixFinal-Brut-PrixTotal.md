---
type: chat-card
parent_export: '[[Export]]'
order: 172
role: assistant
created: '2025-11-11T00:41:53.050665Z'
tags:
- chat-card
- power-bi
- finance
- receipts
attachments_count: 0
---

# 🤖 Message 172 - Assistant

**ID:** msg-172

## 💬 Content


**ID:** msg-172

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


## 🔗 Navigation

- ⬆️ Previous: [[Card-171-R171-Mlet-Définir-plage-dates-DateDebut]]
- ⬇️ Next: [[Card-173-R173-COMPARAISONS-TEMPORELLES-Mois-Précédent-]]
- 📊 MOC: [[_MOC_Ticket receipt data extraction]]

## 🏷️ Topics

- #power-bi
- #finance
- #receipts
