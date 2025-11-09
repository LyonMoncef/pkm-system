---
created: 2025-11-05T20:29:25.008198
updated: 2025-11-05T20:29:25.008198
type: chat-card
chat_message_id: 
chat_message_number: 110
role: user
session: [[MOC-Session-Ticket receipt data extraction]]
tags: [chat-card]
---

# Q075-Question-User

← [[Card-074]] | [[MOC-Session-Ticket receipt data extraction|↑ Session]] | [[Card-076]] →

---

m// Fonction pour importer tous les CSV d'un dossier
let
    FonctionImportCSV = (CheminDossier as text) =>
    let
        Source = Folder.Files(CheminDossier),
        FiltreCSV = Table.SelectRows(Source, each Text.EndsWith([Name], ".csv")),
        AjouterContenu = Table.AddColumn(FiltreCSV, "Contenu", 
            each Csv.Document([Content], [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.None])),
        DevelopperContenu = Table.ExpandTableColumn(AjouterContenu, "Contenu", 
            {"Column1", "Column2", "Column3"}, {"Col1", "Col2", "Col3"}),
        SupprimerAutresColonnes = Table.SelectColumns(DevelopperContenu, {"Name", "Col1", "Col2", "Col3"})
    in
        SupprimerAutresColonnes
in
    FonctionImportCSV

---

**Card 75/106** | Message #110 | Role: user