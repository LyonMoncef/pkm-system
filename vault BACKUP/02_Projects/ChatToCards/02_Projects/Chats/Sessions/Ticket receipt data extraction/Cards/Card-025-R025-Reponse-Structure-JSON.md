---
created: 2025-11-05T20:29:24.288410
updated: 2025-11-05T20:29:24.288410
type: chat-card
chat_message_id: 
chat_message_number: 60
role: assistant
session: [[MOC-Session-Ticket receipt data extraction]]
tags: [export, expense, chat-card, receipt]
---

# R025-Reponse-Structure-JSON

← [[Card-024]] | [[MOC-Session-Ticket receipt data extraction|↑ Session]] | [[Card-026]] →

---

Parfait ! Voici les deux tickets :
Ticket 1 - TotalEnergies Fontaines sur Saône
json{
  "enseigne": "TotalEnergies",
  "magasin": "RELAIS FONTAINES MARRONNIERS",
  "adresse": "46 AVENUE DES MARRONNIERS, 69270 FONTAINES SUR SAONE",
  "telephone": "0437400001",
  "fax": "0437400001",
  "date": "2025-10-04",
  "heure": "17:37:16",
  "siret": "81246965823",
  "code_naf": "4730",
  "numero_ticket": "105000041846",
  "articles": [
    {
      "description": "DIESEL pompe 05",
      "quantite_litres": 8.99,
      "prix_unitaire": 1.599,
      "prix_total": 14.38,
      "carburant": "DIESEL"
    }
  ],
  "nombre_articles": 1,
  "total_ttc": 14.38,
  "tva_details": {
    "taux_tva": 20.00,
    "montant_ttc": 14.38,
    "montant_tva": 2.40,
    "montant_ht": 11.98
  },
  "montant_paye": 14.38,
  "devise": "EUR",
  "mode_paiement": "Carte bancaire",
  "type_carte": "VISA",
  "numero_autorisation": "384266",
  "station_id": "Nf006333",
  "terminal_id": "00633495",
  "crypto": "F26F36Dxxxxx121A"
}
Ticket 2 - E.Leclerc Station (Retrait espèces)
json{
  "enseigne": "E.Leclerc",
  "magasin": "LECLERC STATION 24/24",
  "adresse": "ZAC LE CROISSANT FERTILE, 38200 VIENNE",
  "telephone": "04 74 31 97 05",
  "date": "2025-09-23",
  "heure": "23:58:53",
  "type_transaction": "Retrait espèces / Billet banques",
  "articles": [
    {
      "description": "Billet banques",
      "quantite": 1,
      "prix_unitaire": 40.00,
      "prix_total": 40.00,
      "type": "retrait"
    }
  ],
  "nombre_articles": 1,
  "montant_total": 40.00,
  "solde": 40.00,
  "mode_paiement": "Carte bancaire",
  "numero_note_credit": "504375",
  "code_barre": "9991005043752",
  "numero_station": "3228",
  "numero_ticket": "2263610094",
  "reference": "51-0214800-64590407",
  "note": "Ticket à conserver à l'abri de la lumière. Montant minimum acceptable > 3€. Ticket d'avoir < 1€ utilisable sur 1 borne après introduction nouveau billet"
}
Version CSV combinée
csvenseigne,magasin,date,heure,type_transaction,article,quantite,unite,prix_unitaire,prix_total,total_ticket,tva_taux,tva_montant
TotalEnergies,RELAIS FONTAINES MARRONNIERS,2025-10-04,17:37:16,achat,DIESEL pompe 05,8.99,litres,1.599,14.38,14.38,20.00,2.40
E.Leclerc,LECLERC STATION 24/24,2025-09-23,23:58:53,retrait,Billet banques,1,unité,40.00,40.00,40.00,,
Prêt pour la suite ! 🚀

---

**Card 25/106** | Message #60 | Role: assistant