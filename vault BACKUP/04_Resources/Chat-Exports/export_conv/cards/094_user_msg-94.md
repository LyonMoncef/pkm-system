---
type: chat-card
parent_export: '[[🚀 POWER BI / EXCEL POWER PIVOT - Architecture de rêve pour tes tickets
  de caisse !]]'
order: 94
role: user
created: '2025-11-09T20:20:58.847757Z'
tags:
- chat-card
attachments_count: 0
---

# 👤 Message 94 - User

**ID:** msg-94

## 💬 Content

\n\n**ID:** msg-94\n\nmlet\n    // Définir la plage de dates\n    DateDebut = #date(2025, 1, 1),\n    DateFin = #date(2026, 12, 31),\n    NbJours = Duration.Days(DateFin - DateDebut) + 1,\n    \n    // Générer toutes les dates\n    ListeDates = List.Dates(DateDebut, NbJours, #duration(1,0,0,0)),\n    TableDates = Table.FromList(ListeDates, Splitter.SplitByNothing(), {\"Date\"}),\n    \n    // Ajouter les colonnes\n    AddAnnee = Table.AddColumn(TableDates, \"Annee\", each Date.Year([Date]), Int64.Type),\n    AddTrimestre = Table.AddColumn(AddAnnee, \"Trimestre\", each \"Q\" & Text.From(Date.QuarterOfYear([Date]))),\n    AddMois = Table.AddColumn(AddTrimestre, \"Mois\", each Date.Month([Date]), Int64.Type),\n    AddMoisNom = Table.AddColumn(AddMois, \"MoisNom\", each Date.MonthName([Date], \"fr-FR\")),\n    AddSemaine = Table.AddColumn(AddMoisNom, \"Semaine\", each Date.WeekOfYear([Date]), Int64.Type),\n    AddJourSemaine = Table.AddColumn(AddSemaine, \"JourSemaine\", each Date.DayOfWeek([Date], Day.Monday) + 1, Int64.Type),\n    AddJourNom = Table.AddColumn(AddJourSemaine, \"JourNom\", each Date.DayOfWeekName([Date], \"fr-FR\")),\n    AddWeekend = Table.AddColumn(AddJourNom, \"EstWeekend\", each if [JourSemaine] >= 6 then 1 else 0, Int64.Type),\n    \n    // Jours fériés français (à personnaliser)\n    AddFerie = Table.AddColumn(AddWeekend, \"EstJourFerie\", each \n        if List.Contains({\n            #date(2025,1,1),   // Jour de l'an\n            #date(2025,4,21),  // Lundi de Pâques\n            #date(2025,5,1),   // Fête du travail\n            #date(2025,5,8),   // Victoire 1945\n            #date(2025,5,29),  // Ascension\n            #date(2025,6,9),   // Lundi de Pentecôte\n            #date(2025,7,14),  // Fête nationale\n            #date(2025,8,15),  // Assomption\n            #date(2025,11,1),  // Toussaint\n            #date(2025,11,11), // Armistice 1918\n            #date(2025,12,25)  // Noël\n        }, [Date]) then 1 else 0, Int64.Type)\nin\n    AddFerie\n\n---\n\n

## 🔗 Navigation

- ⬆️ Previous: [[093_user_msg-93]]
- ⬇️ Next: [[095_user_msg-95]]
- 📊 MOC: [[_MOC_export_conv]]
