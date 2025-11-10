---
type: chat-card
parent_export: '[[Export]]'
order: 184
role: assistant
created: '2025-11-11T00:41:53.151214Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 184 - Assistant

**ID:** msg-184

## 💬 Content


**ID:** msg-184

m// Fonction pour importer tous les CSV d'un dossier
let
 FonctionImportCSV = (CheminDossier as text) =>
 let
 Source = Folder.Files(CheminDossier),
 FiltreCSV = Table.SelectRows(Source, each Text.EndsWith([Name], \".csv\")),
 AjouterContenu = Table.AddColumn(FiltreCSV, \"Contenu\",
 each Csv.Document([Content], [Delimiter=\",\", Encoding=65001, QuoteStyle=QuoteStyle.None])),
 DevelopperContenu = Table.ExpandTableColumn(AjouterContenu, \"Contenu\",
 {\"Column1\", \"Column2\", \"Column3\"}, {\"Col1\", \"Col2\", \"Col3\"}),
 SupprimerAutresColonnes = Table.SelectColumns(DevelopperContenu, {\"Name\", \"Col1\", \"Col2\", \"Col3\"})
 in
 SupprimerAutresColonnes
in
 FonctionImportCSV

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-183-R183-Marge-Brute-coût-achat-Total]]
- ⬇️ Next: [[Card-185-R185-VbaSub-RefreshAllData-Rafraîchir-tous-co]]
- 📊 MOC: [[_MOC_Ticket receipt data extraction]]
