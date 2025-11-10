---
type: chat-card
parent_export: '[[🚀 POWER BI / EXCEL POWER PIVOT - Architecture de rêve pour tes tickets
  de caisse !]]'
order: 93
role: user
created: '2025-11-09T20:20:58.839631Z'
tags:
- chat-card
- finance
- receipts
attachments_count: 0
---

# 👤 Message 93 - User

**ID:** msg-93

## 💬 Content

\n\n**ID:** msg-93\n\nmlet\n    Source = Csv.Document(File.Contents(\"C:\\Data\\tickets_raw.csv\")),\n    PromoHeaders = Table.PromoteHeaders(Source),\n    \n    // Nettoyer les montants\n    CleanAmounts = Table.TransformColumns(PromoHeaders, {\n        {\"prix_unitaire\", each Number.From(Text.Replace(_, \",\", \".\")), type number},\n        {\"prix_total\", each Number.From(Text.Replace(_, \",\", \".\")), type number},\n        {\"remise\", each Number.From(Text.Replace(_, \",\", \".\")), type number}\n    }),\n    \n    // Convertir les dates\n    ConvertDates = Table.TransformColumns(CleanAmounts, {\n        {\"date\", each Date.From(_, \"fr-FR\"), type date}\n    }),\n    \n    // Ajouter des colonnes calculées\n    AddCalculated = Table.AddColumn(ConvertDates, \"prix_final\", \n        each [prix_total] + [remise], type number),\n    \n    // Créer les IDs uniques\n    AddTransactionID = Table.AddIndexColumn(AddCalculated, \"TransactionID\", 1, 1, Int64.Type),\n    \n    // Calculer HT et TVA\n    AddTVA = Table.AddColumn(AddTransactionID, \"montant_ht\", \n        each [prix_final] / (1 + [tva_taux]/100), type number),\n    \n    AddMontantTVA = Table.AddColumn(AddTVA, \"montant_tva\",\n        each [prix_final] - [montant_ht], type number)\nin\n    AddMontantTVA\n\n---\n\n

## 🔗 Navigation

- ⬆️ Previous: [[092_user_msg-92]]
- ⬇️ Next: [[094_user_msg-94]]
- 📊 MOC: [[_MOC_export_conv]]

## 🏷️ Topics

- #finance
- #receipts
