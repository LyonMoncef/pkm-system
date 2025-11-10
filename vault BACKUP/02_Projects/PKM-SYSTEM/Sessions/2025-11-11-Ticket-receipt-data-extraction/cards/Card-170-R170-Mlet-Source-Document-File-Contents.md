---
type: chat-card
parent_export: '[[Export]]'
order: 170
role: assistant
created: '2025-11-11T00:41:53.032997Z'
tags:
- chat-card
- finance
- receipts
attachments_count: 0
---

# 🤖 Message 170 - Assistant

**ID:** msg-170

## 💬 Content


**ID:** msg-170

mlet
 Source = Csv.Document(File.Contents(\"C:\\Data\\tickets_raw.csv\")),
 PromoHeaders = Table.PromoteHeaders(Source),

 // Nettoyer les montants
 CleanAmounts = Table.TransformColumns(PromoHeaders, {
 {\"prix_unitaire\", each Number.From(Text.Replace(_, \",\", \".\")), type number},
 {\"prix_total\", each Number.From(Text.Replace(_, \",\", \".\")), type number},
 {\"remise\", each Number.From(Text.Replace(_, \",\", \".\")), type number}
 }),

 // Convertir les dates
 ConvertDates = Table.TransformColumns(CleanAmounts, {
 {\"date\", each Date.From(_, \"fr-FR\"), type date}
 }),

 // Ajouter des colonnes calculées
 AddCalculated = Table.AddColumn(ConvertDates, \"prix_final\",
 each [prix_total] + [remise], type number),

 // Créer les IDs uniques
 AddTransactionID = Table.AddIndexColumn(AddCalculated, \"TransactionID\", 1, 1, Int64.Type),

 // Calculer HT et TVA
 AddTVA = Table.AddColumn(AddTransactionID, \"montant_ht\",
 each [prix_final] / (1 + [tva_taux]/100), type number),

 AddMontantTVA = Table.AddColumn(AddTVA, \"montant_tva\",
 each [prix_final] - [montant_ht], type number)
in
 AddMontantTVA

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-169-R169-CsvTicketID-Date-HeureID-MagasinID-Paiem]]
- ⬇️ Next: [[Card-171-R171-Mlet-Définir-plage-dates-DateDebut]]
- 📊 MOC: [[_MOC_Ticket receipt data extraction]]

## 🏷️ Topics

- #finance
- #receipts
