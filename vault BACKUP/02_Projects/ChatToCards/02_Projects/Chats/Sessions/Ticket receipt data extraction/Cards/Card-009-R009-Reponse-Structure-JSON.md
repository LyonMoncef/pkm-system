---
created: 2025-11-05T20:29:24.067002
updated: 2025-11-05T20:29:24.067002
type: chat-card
chat_message_id: 
chat_message_number: 44
role: assistant
session: [[MOC-Session-Ticket receipt data extraction]]
tags: [export, expense, chat-card, receipt]
---

# R009-Reponse-Structure-JSON

← [[Card-008]] | [[MOC-Session-Ticket receipt data extraction|↑ Session]] | [[Card-010]] →

---

Voici l'extraction du ticket TotalEnergies :
json{
  "enseigne": "TotalEnergies",
  "magasin": "MESSIMY",
  "adresse": "104 RTE DES MONTS DU LYONNAIS, 69510 MESSIMY",
  "telephone": "0478489639",
  "fax": "0160678061",
  "date": "2025-10-03",
  "heure": "19:43:02",
  "siret": "891018368000095549",
  "code_naf": "4511",
  "articles": [
    {
      "description": "DIESEL pompe 02",
      "quantite_litres": 10.04,
      "prix_unitaire": 1.706,
      "prix_total": 17.13,
      "carburant": "DIESEL"
    }
  ],
  "nombre_articles": 1,
  "total_ttc": 17.13,
  "tva_details": {
    "taux_tva": 20.00,
    "montant_ttc": 17.13,
    "montant_tva": 2.86,
    "montant_ht": 14.27
  },
  "montant_paye": 17.13,
  "devise": "EUR",
  "mode_paiement": "Carte bancaire",
  "type_carte": "VISA",
  "numero_autorisation": "771166",
  "station_id": "Nf002037",
  "terminal_id": "00203798"
}
Version CSV :
csvenseigne,magasin,date,heure,article,quantite,unite,prix_unitaire,prix_total,total_ttc,tva_taux,tva_montant,total_ht
TotalEnergies,MESSIMY,2025-10-03,19:43:02,DIESEL pompe 02,10.04,litres,1.706,17.13,17.13,20.00,2.86,14.27
Prêt pour le prochain ticket !

---

**Card 9/106** | Message #44 | Role: assistant