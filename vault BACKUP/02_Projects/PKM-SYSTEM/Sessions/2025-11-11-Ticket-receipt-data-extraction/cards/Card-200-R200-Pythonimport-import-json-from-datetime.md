---
type: chat-card
parent_export: '[[Export]]'
order: 200
role: assistant
created: '2025-11-11T00:41:53.295689Z'
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

# 🤖 Message 200 - Assistant

**ID:** msg-200

## 💬 Content


**ID:** msg-200

pythonimport os
import json
from datetime import datetime
import shutil

# Chemins
CHEMIN_CSV = \"C:/Data/tickets_raw.csv\"
CHEMIN_VAULT = \"D:/Obsidian/MonVault/10-COMPTA/Tickets\"
CHEMIN_NAS = \"//NAS/Compta/2025\"

def creer_note_ticket(ticket_data):
 \"\"\"Génère une note Obsidian depuis un ticket\"\"\"

 date = ticket_data['date']
 enseigne = ticket_data['enseigne']
 montant = ticket_data['total_ttc']

 # Nom du fichier
 nom_fichier = f\"{date} {enseigne}.md\"
 chemin_complet = os.path.join(CHEMIN_VAULT, nom_fichier)

 # Contenu de la note
 contenu = f\"\"\"---
type: ticket
date: {date}
heure: \"{ticket_data['heure']}\"
enseigne: \"[[{enseigne}]]\"
magasin: \"{ticket_data['magasin']}\"
montant_total: {montant}
tags:
 - compta/ticket
 - compta/{date[:4]}/{date[5:7]}
 - enseigne/{enseigne.lower().replace(' ', '-')}
---

# 🧾 Ticket - {enseigne} - {date}

> [!info] Métadonnées
> - **Date** : {date} à {ticket_data['heure']}
> - **Enseigne** : [[{enseigne}]]
> - **Magasin** : {ticket_data['magasin']}
> - **Montant** : {montant} €

## 🛒 Articles achetés

\"\"\"

 # Ajouter les articles
 for article in ticket_data['articles']:
 contenu += f\"- [ ] [[{article['description']}]] - {article['quantite']}x - {article['prix_total']} €\
\"

 # Liens NAS
 mois = date[5:7]
 contenu += f\"\"\"

## 📎 Liens vers NAS

> [!abstract] Fichiers stockés
> - 📄 PDF : `{CHEMIN_NAS}/{mois}-{datetime.strptime(mois, '%m').strftime('%B')}/{date}_{enseigne.replace(' ', '_')}.pdf`
> - 📊 CSV : `{CHEMIN_NAS}/{mois}-{datetime.strptime(mois, '%m').strftime('%B')}/{date}_{enseigne.replace(' ', '_')}.csv`

---

**Créé le** : {datetime.now().strftime('%Y-%m-%d')}
\"\"\"

 # Écrire le fichier
 with open(chemin_complet, 'w', encoding='utf-8') as f:
 f.write(contenu)

 print(f\"✅ Note créée : {nom_fichier}\")

 return chemin_complet

def copier_vers_nas(fichier_source, ticket_data):
 \"\"\"Copie les fichiers vers le NAS\"\"\"

 date = ticket_data['date']
 enseigne = ticket_data['enseigne']
 mois = date[5:7]
 mois_nom = datetime.strptime(mois, '%m').strftime('%B')

 dossier_nas = os.path.join(CHEMIN_NAS, f\"{mois}-{mois_nom}\")
 os.makedirs(dossier_nas, exist_ok=True)

 # Copier PDF, CSV, etc.
 for ext in ['.pdf', '.csv', '.jpg']:
 source = fichier_source.replace('.csv', ext)
 if os.path.exists(source):
 dest = os.path.join(dossier_nas, f\"{date}_{enseigne.replace(' ', '_')}{ext}\")
 shutil.copy2(source, dest)
 print(f\"📁 Copié vers NAS : {dest}\")

# Fonction principale
def traiter_nouveaux_tickets():
 \"\"\"Traite tous les tickets en attente\"\"\"

 # Lire les tickets depuis CSV
 # ... (ton code d'extraction existant)

 for ticket in tickets:
 creer_note_ticket(ticket)
 copier_vers_nas(fichier_csv, ticket)

 print(f\"\
🎉 {len(tickets)} tickets traités !\")

if __name__ == \"__main__\":
 traiter_nouveaux_tickets()

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-199-R199-Markdown-type-budget-mois-Octobre]]
- ⬇️ Next: [[Card-201-R201-Json-commands-open-name-Ouvrir]]
- 📊 MOC: [[_MOC_Ticket receipt data extraction]]

## 🏷️ Topics

- #python
- #obsidian
- #finance
- #receipts
- #code
- #automation
