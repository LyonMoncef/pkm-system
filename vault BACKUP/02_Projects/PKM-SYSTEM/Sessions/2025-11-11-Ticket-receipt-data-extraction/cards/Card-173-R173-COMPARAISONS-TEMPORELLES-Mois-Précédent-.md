---
type: chat-card
parent_export: '[[Export]]'
order: 173
role: assistant
created: '2025-11-11T00:41:53.058135Z'
tags:
- chat-card
- power-bi
- code
attachments_count: 0
---

# 🤖 Message 173 - Assistant

**ID:** msg-173

## 💬 Content


**ID:** msg-173

dax// === COMPARAISONS TEMPORELLES ===
CA Mois Précédent =
CALCULATE(
 [CA Total],
 DATEADD(dim_Temps[Date], -1, MONTH)
)

CA Année Précédente =
CALCULATE(
 [CA Total],
 SAMEPERIODLASTYEAR(dim_Temps[Date])
)

Evolution vs Mois-1 =
VAR CAActuel = [CA Total]
VAR CAMoisPrec = [CA Mois Précédent]
RETURN
 DIVIDE(CAActuel - CAMoisPrec, CAMoisPrec, 0) * 100

Evolution vs N-1 =
VAR CAActuel = [CA Total]
VAR CAAnPrec = [CA Année Précédente]
RETURN
 DIVIDE(CAActuel - CAAnPrec, CAAnPrec, 0) * 100

// === CUMULS ===
CA YTD =
TOTALYTD([CA Total], dim_Temps[Date])

CA MTD =
TOTALMTD([CA Total], dim_Temps[Date])

CA Cumul Mobile 30j =
CALCULATE(
 [CA Total],
 DATESINPERIOD(dim_Temps[Date], LASTDATE(dim_Temps[Date]), -30, DAY)
)

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-172-R172-VENTES-Total-PrixFinal-Brut-PrixTotal]]
- ⬇️ Next: [[Card-174-R174-FLOP-PRODUITS-Produits-CALCULATE-Total]]
- 📊 MOC: [[_MOC_Ticket receipt data extraction]]

## 🏷️ Topics

- #power-bi
- #code
