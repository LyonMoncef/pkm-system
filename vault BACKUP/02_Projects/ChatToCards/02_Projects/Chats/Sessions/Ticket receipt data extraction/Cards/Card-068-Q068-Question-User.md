---
created: 2025-11-05T20:29:24.907124
updated: 2025-11-05T20:29:24.907124
type: chat-card
chat_message_id: 
chat_message_number: 103
role: user
session: [[MOC-Session-Ticket receipt data extraction]]
tags: [powerbi, chat-card]
---

# Q068-Question-User

← [[Card-067]] | [[MOC-Session-Ticket receipt data extraction|↑ Session]] | [[Card-069]] →

---

dax// Score RFM pour segmentation
Score_Recency = 
VAR JoursDepuisDerniereVisite = [Jours Depuis Derniere Visite]
RETURN
    SWITCH(
        TRUE(),
        JoursDepuisDerniereVisite <= 30, 5,
        JoursDepuisDerniereVisite <= 60, 4,
        J

---

**Card 68/106** | Message #103 | Role: user