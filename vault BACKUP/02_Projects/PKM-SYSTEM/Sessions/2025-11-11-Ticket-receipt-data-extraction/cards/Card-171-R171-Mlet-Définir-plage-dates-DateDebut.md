---
type: chat-card
parent_export: '[[Export]]'
order: 171
role: assistant
created: '2025-11-11T00:41:53.041670Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 171 - Assistant

**ID:** msg-171

## 💬 Content


**ID:** msg-171

mlet
 // Définir la plage de dates
 DateDebut = #date(2025, 1, 1),
 DateFin = #date(2026, 12, 31),
 NbJours = Duration.Days(DateFin - DateDebut) + 1,

 // Générer toutes les dates
 ListeDates = List.Dates(DateDebut, NbJours, #duration(1,0,0,0)),
 TableDates = Table.FromList(ListeDates, Splitter.SplitByNothing(), {\"Date\"}),

 // Ajouter les colonnes
 AddAnnee = Table.AddColumn(TableDates, \"Annee\", each Date.Year([Date]), Int64.Type),
 AddTrimestre = Table.AddColumn(AddAnnee, \"Trimestre\", each \"Q\" & Text.From(Date.QuarterOfYear([Date]))),
 AddMois = Table.AddColumn(AddTrimestre, \"Mois\", each Date.Month([Date]), Int64.Type),
 AddMoisNom = Table.AddColumn(AddMois, \"MoisNom\", each Date.MonthName([Date], \"fr-FR\")),
 AddSemaine = Table.AddColumn(AddMoisNom, \"Semaine\", each Date.WeekOfYear([Date]), Int64.Type),
 AddJourSemaine = Table.AddColumn(AddSemaine, \"JourSemaine\", each Date.DayOfWeek([Date], Day.Monday) + 1, Int64.Type),
 AddJourNom = Table.AddColumn(AddJourSemaine, \"JourNom\", each Date.DayOfWeekName([Date], \"fr-FR\")),
 AddWeekend = Table.AddColumn(AddJourNom, \"EstWeekend\", each if [JourSemaine] >= 6 then 1 else 0, Int64.Type),

 // Jours fériés français (à personnaliser)
 AddFerie = Table.AddColumn(AddWeekend, \"EstJourFerie\", each
 if List.Contains({
 #date(2025,1,1), // Jour de l'an
 #date(2025,4,21), // Lundi de Pâques
 #date(2025,5,1), // Fête du travail
 #date(2025,5,8), // Victoire 1945
 #date(2025,5,29), // Ascension
 #date(2025,6,9), // Lundi de Pentecôte
 #date(2025,7,14), // Fête nationale
 #date(2025,8,15), // Assomption
 #date(2025,11,1), // Toussaint
 #date(2025,11,11), // Armistice 1918
 #date(2025,12,25) // Noël
 }, [Date]) then 1 else 0, Int64.Type)
in
 AddFerie

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-170-R170-Mlet-Source-Document-File-Contents]]
- ⬇️ Next: [[Card-172-R172-VENTES-Total-PrixFinal-Brut-PrixTotal]]
- 📊 MOC: [[_MOC_Ticket receipt data extraction]]
