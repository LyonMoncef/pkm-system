---
type: chat-card
parent_export: '[[Export]]'
order: 186
role: assistant
created: '2025-11-11T00:41:53.169017Z'
tags:
- chat-card
- power-bi
- finance
- code
attachments_count: 0
---

# 🤖 Message 186 - Assistant

**ID:** msg-186

## 💬 Content


**ID:** msg-186

dax// Utiliser des variables pour éviter les recalculs
Mesure_Optimisee =
VAR _CA = [CA Total]
VAR _Tickets = [Nombre Tickets]
VAR _Panier = DIVIDE(_CA, _Tickets, 0)
RETURN
 IF(_Panier > 100, \"Premium\", \"Standard\")

// Plutôt que de recalculer [CA Total] et [Nombre Tickets] plusieurs fois
```

### **Formatage conditionnel avancé :**
```
// Dans Power BI, créer une mesure pour le format
Couleur_Performance =
VAR Perf = [Evolution vs N-1]
RETURN
 SWITCH(
 TRUE(),
 Perf > 10, \"#00FF00\", // Vert
 Perf > 0, \"#90EE90\", // Vert clair
 Perf > -5, \"#FFD700\", // Jaune
 Perf > -10, \"#FFA500\", // Orange
 \"#FF0000\" // Rouge
 )

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-185-R185-VbaSub-RefreshAllData-Rafraîchir-tous-co]]
- ⬇️ Next: [[Card-187-R187-MFOk-gars-contre-entre-temps]]
- 📊 MOC: [[_MOC_Ticket receipt data extraction]]

## 🏷️ Topics

- #power-bi
- #finance
- #code
