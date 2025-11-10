---
type: chat-card
parent_export: '[[🚀 POWER BI / EXCEL POWER PIVOT - Architecture de rêve pour tes tickets
  de caisse !]]'
order: 116
role: user
created: '2025-11-09T20:20:59.066155Z'
tags:
- chat-card
- python
- obsidian
- finance
- receipts
- code
- automation
attachments_count: 0
---

# 👤 Message 116 - User

**ID:** msg-116

## 💬 Content

\n\n**ID:** msg-116\n\npythonimport os\nimport json\nfrom datetime import datetime\nimport shutil\n\n# Chemins\nCHEMIN_CSV = \"C:/Data/tickets_raw.csv\"\nCHEMIN_VAULT = \"D:/Obsidian/MonVault/10-COMPTA/Tickets\"\nCHEMIN_NAS = \"//NAS/Compta/2025\"\n\ndef creer_note_ticket(ticket_data):\n    \"\"\"Génère une note Obsidian depuis un ticket\"\"\"\n    \n    date = ticket_data['date']\n    enseigne = ticket_data['enseigne']\n    montant = ticket_data['total_ttc']\n    \n    # Nom du fichier\n    nom_fichier = f\"{date} {enseigne}.md\"\n    chemin_complet = os.path.join(CHEMIN_VAULT, nom_fichier)\n    \n    # Contenu de la note\n    contenu = f\"\"\"---\ntype: ticket\ndate: {date}\nheure: \"{ticket_data['heure']}\"\nenseigne: \"[[{enseigne}]]\"\nmagasin: \"{ticket_data['magasin']}\"\nmontant_total: {montant}\ntags:\n  - compta/ticket\n  - compta/{date[:4]}/{date[5:7]}\n  - enseigne/{enseigne.lower().replace(' ', '-')}\n---\n\n# 🧾 Ticket - {enseigne} - {date}\n\n> [!info] Métadonnées\n> - **Date** : {date} à {ticket_data['heure']}\n> - **Enseigne** : [[{enseigne}]]\n> - **Magasin** : {ticket_data['magasin']}\n> - **Montant** : {montant} €\n\n## 🛒 Articles achetés\n\n\"\"\"\n    \n    # Ajouter les articles\n    for article in ticket_data['articles']:\n        contenu += f\"- [ ] [[{article['description']}]] - {article['quantite']}x - {article['prix_total']} €\\n\"\n    \n    # Liens NAS\n    mois = date[5:7]\n    contenu += f\"\"\"\n\n## 📎 Liens vers NAS\n\n> [!abstract] Fichiers stockés\n> - 📄 PDF : `{CHEMIN_NAS}/{mois}-{datetime.strptime(mois, '%m').strftime('%B')}/{date}_{enseigne.replace(' ', '_')}.pdf`\n> - 📊 CSV : `{CHEMIN_NAS}/{mois}-{datetime.strptime(mois, '%m').strftime('%B')}/{date}_{enseigne.replace(' ', '_')}.csv`\n\n---\n\n**Créé le** : {datetime.now().strftime('%Y-%m-%d')}\n\"\"\"\n    \n    # Écrire le fichier\n    with open(chemin_complet, 'w', encoding='utf-8') as f:\n        f.write(contenu)\n    \n    print(f\"✅ Note créée : {nom_fichier}\")\n    \n    return chemin_complet\n\ndef copier_vers_nas(fichier_source, ticket_data):\n    \"\"\"Copie les fichiers vers le NAS\"\"\"\n    \n    date = ticket_data['date']\n    enseigne = ticket_data['enseigne']\n    mois = date[5:7]\n    mois_nom = datetime.strptime(mois, '%m').strftime('%B')\n    \n    dossier_nas = os.path.join(CHEMIN_NAS, f\"{mois}-{mois_nom}\")\n    os.makedirs(dossier_nas, exist_ok=True)\n    \n    # Copier PDF, CSV, etc.\n    for ext in ['.pdf', '.csv', '.jpg']:\n        source = fichier_source.replace('.csv', ext)\n        if os.path.exists(source):\n            dest = os.path.join(dossier_nas, f\"{date}_{enseigne.replace(' ', '_')}{ext}\")\n            shutil.copy2(source, dest)\n            print(f\"📁 Copié vers NAS : {dest}\")\n\n# Fonction principale\ndef traiter_nouveaux_tickets():\n    \"\"\"Traite tous les tickets en attente\"\"\"\n    \n    # Lire les tickets depuis CSV\n    # ... (ton code d'extraction existant)\n    \n    for ticket in tickets:\n        creer_note_ticket(ticket)\n        copier_vers_nas(fichier_csv, ticket)\n    \n    print(f\"\\n🎉 {len(tickets)} tickets traités !\")\n\nif __name__ == \"__main__\":\n    traiter_nouveaux_tickets()\n\n---\n\n

## 🔗 Navigation

- ⬆️ Previous: [[115_user_msg-115]]
- ⬇️ Next: [[117_user_msg-117]]
- 📊 MOC: [[_MOC_export_conv]]

## 🏷️ Topics

- #python
- #obsidian
- #finance
- #receipts
- #code
- #automation
