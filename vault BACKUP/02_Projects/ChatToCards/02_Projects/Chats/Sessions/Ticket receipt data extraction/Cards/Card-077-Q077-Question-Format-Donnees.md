---
created: 2025-11-05T20:29:25.041174
updated: 2025-11-05T20:29:25.041174
type: chat-card
chat_message_id: 
chat_message_number: 112
role: user
session: [[MOC-Session-Ticket receipt data extraction]]
tags: [powerbi, expense, chat-card, receipt]
---

# Q077-Question-Format-Donnees

← [[Card-076]] | [[MOC-Session-Ticket receipt data extraction|↑ Session]] | [[Card-078]] →

---

dax// Utiliser des variables pour éviter les recalculs
Mesure_Optimisee = 
VAR _CA = [CA Total]
VAR _Tickets = [Nombre Tickets]
VAR _Panier = DIVIDE(_CA, _Tickets, 0)
RETURN
    IF(_Panier > 100, "Premium", "Standard")

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
        Perf > 10, "#00FF00",  // Vert
        Perf > 0, "#90EE90",   // Vert clair
        Perf > -5, "#FFD700",  // Jaune
        Perf > -10, "#FFA500", // Orange
        "#FF0000"               // Rouge
    )

---

**Card 77/106** | Message #112 | Role: user