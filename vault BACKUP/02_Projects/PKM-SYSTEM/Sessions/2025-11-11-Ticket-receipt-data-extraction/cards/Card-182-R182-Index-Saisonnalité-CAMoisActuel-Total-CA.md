---
type: chat-card
parent_export: '[[Export]]'
order: 182
role: assistant
created: '2025-11-11T00:41:53.134799Z'
tags:
- chat-card
- power-bi
- code
attachments_count: 0
---

# 🤖 Message 182 - Assistant

**ID:** msg-182

## 💬 Content


**ID:** msg-182

dax// Index de Saisonnalité
Indice_Saisonnier =
VAR CAMoisActuel = [CA Total]
VAR CAMoyenAnnuel =
 CALCULATE(
 [CA Total],
 ALL(dim_Temps[Mois])
 ) / 12
RETURN
 DIVIDE(CAMoisActuel, CAMoyenAnnuel, 0) * 100

Mois_le_Plus_Fort =
 CALCULATE(
 FIRSTNONBLANK(dim_Temps[MoisNom], 1),
 TOPN(1, ALL(dim_Temps[MoisNom]), [CA Total], DESC)
 )

Mois_le_Plus_Faible =
 CALCULATE(
 FIRSTNONBLANK(dim_Temps[MoisNom], 1),
 TOPN(1, ALL(dim_Temps[MoisNom]), [CA Total], ASC)
 )

// Comparaison Week-end vs Semaine
Performance_Weekend =
VAR CAWeekend = CALCULATE([CA Total], dim_Temps[EstWeekend] = 1)
VAR CAMoyenJour = DIVIDE([CA Total], DISTINCTCOUNT(dim_Temps[Date]), 0)
RETURN
 DIVIDE(CAWeekend, CAMoyenJour, 0)

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-181-R181-Tendance-Linéaire-simple-MinDate-Date]]
- ⬇️ Next: [[Card-183-R183-Marge-Brute-coût-achat-Total]]
- 📊 MOC: [[_MOC_Ticket receipt data extraction]]

## 🏷️ Topics

- #power-bi
- #code
