---
created: 2025-11-05T20:29:25.023695
updated: 2025-11-05T20:29:25.023695
type: chat-card
chat_message_id: 
chat_message_number: 111
role: user
session: [[MOC-Session-Ticket receipt data extraction]]
tags: [chat-card]
---

# Q076-Question-User

← [[Card-075]] | [[MOC-Session-Ticket receipt data extraction|↑ Session]] | [[Card-077]] →

---

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
    
    MsgBox "Données rafraîchies avec succès !", vbInformation
End Sub

---

**Card 76/106** | Message #111 | Role: user