---
type: chat-card
parent_export: '[[🚀 POWER BI / EXCEL POWER PIVOT - Architecture de rêve pour tes tickets
  de caisse !]]'
order: 105
role: user
created: '2025-11-09T20:20:58.959304Z'
tags:
- chat-card
attachments_count: 0
---

# 👤 Message 105 - User

**ID:** msg-105

## 💬 Content

\n\n**ID:** msg-105\n\nm// Fonction pour importer tous les CSV d'un dossier\nlet\n    FonctionImportCSV = (CheminDossier as text) =>\n    let\n        Source = Folder.Files(CheminDossier),\n        FiltreCSV = Table.SelectRows(Source, each Text.EndsWith([Name], \".csv\")),\n        AjouterContenu = Table.AddColumn(FiltreCSV, \"Contenu\", \n            each Csv.Document([Content], [Delimiter=\",\", Encoding=65001, QuoteStyle=QuoteStyle.None])),\n        DevelopperContenu = Table.ExpandTableColumn(AjouterContenu, \"Contenu\", \n            {\"Column1\", \"Column2\", \"Column3\"}, {\"Col1\", \"Col2\", \"Col3\"}),\n        SupprimerAutresColonnes = Table.SelectColumns(DevelopperContenu, {\"Name\", \"Col1\", \"Col2\", \"Col3\"})\n    in\n        SupprimerAutresColonnes\nin\n    FonctionImportCSV\n\n---\n\n

## 🔗 Navigation

- ⬆️ Previous: [[104_user_msg-104]]
- ⬇️ Next: [[106_user_msg-106]]
- 📊 MOC: [[_MOC_export_conv]]
