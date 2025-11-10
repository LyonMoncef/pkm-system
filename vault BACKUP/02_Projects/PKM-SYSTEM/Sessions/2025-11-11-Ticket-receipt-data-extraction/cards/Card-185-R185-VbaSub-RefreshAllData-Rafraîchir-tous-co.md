---
type: chat-card
parent_export: '[[Export]]'
order: 185
role: assistant
created: '2025-11-11T00:41:53.159795Z'
tags:
- chat-card
- power-bi
attachments_count: 0
---

# 🤖 Message 185 - Assistant

**ID:** msg-185

## 💬 Content


**ID:** msg-185

vbaSub RefreshAllData()
 ' Rafraîchir tous les TCD et connexions

 Application.ScreenUpdating = False
 Application.Calculation = xlCalculationManual

 ' Rafraîchir toutes les connexions Power Query
 ThisWorkbook.Connections.Refresh

 ' Rafraîchir tous les TCD
 Dim pt As PivotTable
 Dim ws As Worksheet

 For Each ws In ThisWorkbook.Worksheets
 For Each pt In ws.PivotTables
 pt.RefreshTable
 Next pt
 Next ws

 ' Rafraîchir le modèle de données
 If ThisWorkbook.Model.DataModelConnection.State = xlOpen Then
 ThisWorkbook.Model.Refresh
 End If

 Application.Calculation = xlCalculationAutomatic
 Application.ScreenUpdating = True

 MsgBox \"Données rafraîchies avec succès !\", vbInformation
End Sub

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-184-R184-Fonction-pour-importer-tous-dossier]]
- ⬇️ Next: [[Card-186-R186-Utiliser-variables-pour-éviter-recalculs]]
- 📊 MOC: [[_MOC_Ticket receipt data extraction]]

## 🏷️ Topics

- #power-bi
