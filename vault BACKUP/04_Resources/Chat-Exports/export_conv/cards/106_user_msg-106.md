---
type: chat-card
parent_export: '[[🚀 POWER BI / EXCEL POWER PIVOT - Architecture de rêve pour tes tickets
  de caisse !]]'
order: 106
role: user
created: '2025-11-09T20:20:58.968197Z'
tags:
- chat-card
- power-bi
attachments_count: 0
---

# 👤 Message 106 - User

**ID:** msg-106

## 💬 Content

\n\n**ID:** msg-106\n\nvbaSub RefreshAllData()\n    ' Rafraîchir tous les TCD et connexions\n    \n    Application.ScreenUpdating = False\n    Application.Calculation = xlCalculationManual\n    \n    ' Rafraîchir toutes les connexions Power Query\n    ThisWorkbook.Connections.Refresh\n    \n    ' Rafraîchir tous les TCD\n    Dim pt As PivotTable\n    Dim ws As Worksheet\n    \n    For Each ws In ThisWorkbook.Worksheets\n        For Each pt In ws.PivotTables\n            pt.RefreshTable\n        Next pt\n    Next ws\n    \n    ' Rafraîchir le modèle de données\n    If ThisWorkbook.Model.DataModelConnection.State = xlOpen Then\n        ThisWorkbook.Model.Refresh\n    End If\n    \n    Application.Calculation = xlCalculationAutomatic\n    Application.ScreenUpdating = True\n    \n    MsgBox \"Données rafraîchies avec succès !\", vbInformation\nEnd Sub\n\n---\n\n

## 🔗 Navigation

- ⬆️ Previous: [[105_user_msg-105]]
- ⬇️ Next: [[107_user_msg-107]]
- 📊 MOC: [[_MOC_export_conv]]

## 🏷️ Topics

- #power-bi
