---
type: chat-card
parent_export: '[[🚀 POWER BI / EXCEL POWER PIVOT - Architecture de rêve pour tes tickets
  de caisse !]]'
order: 95
role: user
created: '2025-11-09T20:20:58.854480Z'
tags:
- chat-card
- power-bi
- finance
- receipts
attachments_count: 0
---

# 👤 Message 95 - User

**ID:** msg-95

## 💬 Content

\n\n**ID:** msg-95\n\ndax// === VENTES ===\nCA Total = SUM(fact_Achats[PrixFinal])\n\nCA Brut = SUM(fact_Achats[PrixTotal])\n\nTotal Remises = SUM(fact_Achats[MontantRemise])\n\nTaux Remise % = \nDIVIDE([Total Remises], [CA Brut], 0) * 100\n\nPanier Moyen = \nDIVIDE([CA Total], DISTINCTCOUNT(fact_Achats[TicketID]), 0)\n\nNombre Articles = SUM(fact_Achats[Quantite])\n\nArticles par Ticket = \nDIVIDE([Nombre Articles], DISTINCTCOUNT(fact_Achats[TicketID]), 0)\n\n// === TVA ===\nTotal TVA = SUM(fact_Achats[MontantTVA])\n\nTotal HT = SUM(fact_Achats[MontantHT])\n\n// === TRANSACTIONS ===\nNombre Tickets = DISTINCTCOUNT(fact_Achats[TicketID])\n\nNombre Transactions = COUNTROWS(fact_Achats)\n\n---\n\n

## 🔗 Navigation

- ⬆️ Previous: [[094_user_msg-94]]
- ⬇️ Next: [[096_user_msg-96]]
- 📊 MOC: [[_MOC_export_conv]]

## 🏷️ Topics

- #power-bi
- #finance
- #receipts
