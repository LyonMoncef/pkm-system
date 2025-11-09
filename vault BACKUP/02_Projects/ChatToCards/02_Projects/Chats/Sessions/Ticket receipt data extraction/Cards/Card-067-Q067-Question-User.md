---
created: 2025-11-05T20:29:24.890172
updated: 2025-11-05T20:29:24.890172
type: chat-card
chat_message_id: 
chat_message_number: 102
role: user
session: [[MOC-Session-Ticket receipt data extraction]]
tags: [powerbi, expense, chat-card, receipt]
---

# Q067-Question-User

← [[Card-066]] | [[MOC-Session-Ticket receipt data extraction|↑ Session]] | [[Card-068]] →

---

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
                    "@Freq", CALCULATE(COUNTROWS(fact_Achats))
                ),
                [@Freq], DESC
            ),
            dim_Article[NomArticle],
            ", "
        ),
        fact_Achats[TicketID] IN TicketsAvecProduit,
        dim_Article[NomArticle] <> ProduitActuel
    )

---

**Card 67/106** | Message #102 | Role: user