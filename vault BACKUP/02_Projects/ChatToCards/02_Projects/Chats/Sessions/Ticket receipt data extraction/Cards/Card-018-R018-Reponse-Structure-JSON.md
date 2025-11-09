---
created: 2025-11-05T20:29:24.200853
updated: 2025-11-05T20:29:24.200853
type: chat-card
chat_message_id: 
chat_message_number: 53
role: assistant
session: [[MOC-Session-Ticket receipt data extraction]]
tags: [export, expense, chat-card, receipt]
---

# R018-Reponse-Structure-JSON

← [[Card-017]] | [[MOC-Session-Ticket receipt data extraction|↑ Session]] | [[Card-019]] →

---

Merci ! 😄 Voici l'extraction du ticket McDonald's :
json{
  "enseigne": "McDonald's",
  "magasin": "Restaurant McDonald's Vienne DT38",
  "adresse": "30 Quai Pasteur, 38200 VIENNE",
  "telephone": "04.74.85.50.60",
  "siret": "399 034 826 00012",
  "code_ape": "5610C",
  "rcs": "VIENNE",
  "tva_intra": "FR39399034826",
  "date": "2025-10-12",
  "heure": "23:09:38",
  "numero_caisse": "38 - Caisse 3",
  "id_equipier": "97141",
  "restaurant_id": "25000358",
  "articles": [
    {
      "description": "Menu McSmart",
      "quantite": 1,
      "prix_unitaire": 5.00,
      "prix_total": 5.00,
      "composition": [
        "Petit Coke:Menu",
        "Frite Pt ds Menu",
        "Mn Ptit Chicken",
        "Mn McFish Mayo"
      ]
    },
    {
      "description": "Menu McSmart+",
      "quantite": 1,
      "prix_unitaire": 6.00,
      "prix_total": 6.00,
      "composition": [
        "Mn McFish Mayo (x2)",
        "Coke Best Of"
      ]
    },
    {
      "description": "BOFrites Db1Ched",
      "quantite": 1,
      "prix_unitaire": 1.50,
      "prix_total": 1.50,
      "type": "supplement"
    },
    {
      "description": "Detail menu",
      "quantite": 1,
      "prix_unitaire": 0.00,
      "prix_total": 0.00,
      "type": "info"
    }
  ],
  "nombre_articles": 4,
  "total_ttc": 12.50,
  "montant_paye": 12.50,
  "mode_paiement": "CB AUTO (Carte Bancaire sans contact)",
  "type_carte": "Visa Debit",
  "type_commande": "A Emporter",
  "tva_details": {
    "base_ht": 12.50,
    "taux_tva": 10.00,
    "montant_tva": 1.14,
    "montant_ttc": 12.50
  },
  "numero_autorisation": "A00000000310010"
}
Version CSV :
csvenseigne,magasin,date,heure,article,quantite,prix_unitaire,prix_total,composition,type,total_ticket,tva_taux,tva_montant
McDonald's,Restaurant McDonald's Vienne DT38,2025-10-12,23:09:38,Menu McSmart,1,5.00,5.00,"Petit Coke:Menu|Frite Pt ds Menu|Mn Ptit Chicken|Mn McFish Mayo",menu,12.50,10.00,1.14
McDonald's,Restaurant McDonald's Vienne DT38,2025-10-12,23:09:38,Menu McSmart+,1,6.00,6.00,"Mn McFish Mayo x2|Coke Best Of",menu,12.50,10.00,1.14
McDonald's,Restaurant McDonald's Vienne DT38,2025-10-12,23:09:38,BOFrites Db1Ched,1,1.50,1.50,,supplement,12.50,10.00,1.14
Envoie le suivant ! 🔥Réessayer

---

**Card 18/106** | Message #53 | Role: assistant