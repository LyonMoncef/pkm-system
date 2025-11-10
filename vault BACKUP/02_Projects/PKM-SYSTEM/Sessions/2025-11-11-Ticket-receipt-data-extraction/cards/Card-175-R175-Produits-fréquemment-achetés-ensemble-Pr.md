---
type: chat-card
parent_export: '[[Export]]'
order: 175
role: assistant
created: '2025-11-11T00:41:53.074311Z'
tags:
- chat-card
- power-bi
- finance
- code
attachments_count: 0
---

# 🤖 Message 175 - Assistant

**ID:** msg-175

## 💬 Content


**ID:** msg-175

dax// Produits fréquemment achetés ensemble
Produits Associes =
VAR ProduitActuel = SELECTEDVALUE(dim_Article[NomArticle])
VAR TicketsAvecProduit =
 CALCULATETABLE(
 VALUES(fact_Achats[TicketID]),
 dim_Article[NomArticle] = ProduitActuel
 )
RETURN
 CALCULATE(
 CONCATENATEX(
 TOPN(5,
 ADDCOLUMNS(
 VALUES(dim_Article[NomArticle]),
 \"@Freq\", CALCULATE(COUNTROWS(fact_Achats))
 ),
 [@Freq], DESC
 ),
 dim_Article[NomArticle],
 \", \"
 ),
 fact_Achats[TicketID] IN TicketsAvecProduit,
 dim_Article[NomArticle] <> ProduitActuel
 )

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-174-R174-FLOP-PRODUITS-Produits-CALCULATE-Total]]
- ⬇️ Next: [[Card-176-R176-Score-pour-segmentation-JoursDepuisDerni]]
- 📊 MOC: [[_MOC_Ticket receipt data extraction]]

## 🏷️ Topics

- #power-bi
- #finance
- #code
