---
created: 2025-11-05T20:29:24.813843
updated: 2025-11-05T20:29:24.813843
type: chat-card
chat_message_id: 
chat_message_number: 97
role: user
session: [[MOC-Session-Ticket receipt data extraction]]
tags: [expense, chat-card, receipt]
---

# Q062-Question-User

← [[Card-061]] | [[MOC-Session-Ticket receipt data extraction|↑ Session]] | [[Card-063]] →

---

mlet
    Source = Csv.Document(File.Contents("C:\Data\tickets_raw.csv")),
    PromoHeaders = Table.PromoteHeaders(Source),
    
    // Nettoyer les montants
    CleanAmounts = Table.TransformColumns(PromoHeaders, {
        {"prix_unitaire", each Number.From(Text.Replace(_, ",", ".")), type number},
        {"prix_total", each Number.From(Text.Replace(_, ",", ".")), type number},
        {"remise", each Number.From(Text.Replace(_, ",", ".")), type number}
    }),
    
    // Convertir les dates
    ConvertDates = Table.TransformColumns(CleanAmounts, {
        {"date", each Date.From(_, "fr-FR"), type date}
    }),
    
    // Ajouter des colonnes calculées
    AddCalculated = Table.AddColumn(ConvertDates, "prix_final", 
        each [prix_total] + [remise], type number),
    
    // Créer les IDs uniques
    AddTransactionID = Table.AddIndexColumn(AddCalculated, "TransactionID", 1, 1, Int64.Type),
    
    // Calculer HT et TVA
    AddTVA = Table.AddColumn(AddTransactionID, "montant_ht", 
        each [prix_final] / (1 + [tva_taux]/100), type number),
    
    AddMontantTVA = Table.AddColumn(AddTVA, "montant_tva",
        each [prix_final] - [montant_ht], type number)
in
    AddMontantTVA

---

**Card 62/106** | Message #97 | Role: user