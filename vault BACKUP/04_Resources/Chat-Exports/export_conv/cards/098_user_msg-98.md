---
type: chat-card
parent_export: '[[🚀 POWER BI / EXCEL POWER PIVOT - Architecture de rêve pour tes tickets
  de caisse !]]'
order: 98
role: user
created: '2025-11-09T20:20:58.891733Z'
tags:
- chat-card
- power-bi
- finance
- code
attachments_count: 0
---

# 👤 Message 98 - User

**ID:** msg-98

## 💬 Content

\n\n**ID:** msg-98\n\ndax// Produits fréquemment achetés ensemble\nProduits Associes = \nVAR ProduitActuel = SELECTEDVALUE(dim_Article[NomArticle])\nVAR TicketsAvecProduit = \n    CALCULATETABLE(\n        VALUES(fact_Achats[TicketID]),\n        dim_Article[NomArticle] = ProduitActuel\n    )\nRETURN\n    CALCULATE(\n        CONCATENATEX(\n            TOPN(5, \n                ADDCOLUMNS(\n                    VALUES(dim_Article[NomArticle]),\n                    \"@Freq\", CALCULATE(COUNTROWS(fact_Achats))\n                ),\n                [@Freq], DESC\n            ),\n            dim_Article[NomArticle],\n            \", \"\n        ),\n        fact_Achats[TicketID] IN TicketsAvecProduit,\n        dim_Article[NomArticle] <> ProduitActuel\n    )\n\n---\n\n

## 🔗 Navigation

- ⬆️ Previous: [[097_user_msg-97]]
- ⬇️ Next: [[099_user_msg-99]]
- 📊 MOC: [[_MOC_export_conv]]

## 🏷️ Topics

- #power-bi
- #finance
- #code
