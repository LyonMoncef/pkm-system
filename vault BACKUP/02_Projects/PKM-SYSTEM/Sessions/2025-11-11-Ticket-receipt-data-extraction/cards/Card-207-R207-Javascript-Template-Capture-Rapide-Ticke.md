---
type: chat-card
parent_export: '[[Export]]'
order: 207
role: assistant
created: '2025-11-11T00:41:53.365858Z'
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

# 🤖 Message 207 - Assistant

**ID:** msg-207

## 💬 Content


**ID:** msg-207

javascript// Template Capture Rapide Ticket
module.exports = async (params) => {
 const {quickAddApi: qa} = params;

 // Demander les infos essentielles
 const enseigne = await qa.suggester(
 [\"E.Leclerc\", \"Carrefour\", \"TotalEnergies\", \"McDonald's\", \"Action\", \"Autre\"],
 [\"E.Leclerc\", \"Carrefour\", \"TotalEnergies\", \"McDonald's\", \"Action\", \"Autre\"]
 );

 const montant = await qa.inputPrompt(\"Montant total (€)\");

 const date = qa.date.now(\"YYYY-MM-DD\");
 const heure = qa.date.now(\"HH:mm\");

 // Créer note minimale
 const filename = `${date} ${enseigne} - BROUILLON`;
 const folder = \"00-INBOX\";

 const content = `---
type: ticket
date: ${date}
heure: \"${heure}\"
enseigne: \"[[${enseigne}]]\"
montant_total: ${montant}
status: brouillon
tags:
 - compta/inbox
 - compta/a-traiter
---

# 🧾 ${filename}

> [!warning] À compléter
> Ticket capturé rapidement depuis mobile

## 📸 Photo du ticket
![[]]

## ✅ À faire
- [ ] Ajouter détail articles
- [ ] Uploader photo ticket
- [ ] Vérifier montant
- [ ] Copier vers NAS
- [ ] Classer dans dossier mois

---
Créé : ${date} ${heure}
`;

 await qa.createNote(filename, content, folder);

 return;
};
```

### **iOS Shortcuts - Automation complète**
```
📱 SHORTCUT: \"Nouveau Ticket\"

1. Prendre photo du ticket
2. OCR avec Vision API
3. Extraire : date, enseigne, montant
4. Créer note Obsidian via Obsidian URI
5. Uploader photo vers NAS (via SMB ou app Files)
6. Notification : \"✅ Ticket capturé\"
```

---

## 🗂️ **ORGANISATION & CONVENTIONS DE NOMMAGE**

### **Noms de fichiers standardisés**
```
TICKETS:
📄 YYYY-MM-DD Enseigne Ville.md
 2025-10-07 E.Leclerc Vienne.md
 2025-10-12 McDonald's Vienne.md

ENSEIGNES:
📄 Nom Enseigne.md
 E.Leclerc.md
 Carrefour Market.md

PRODUITS:
📄 Nom Produit Marque.md
 Gazpacho Alvalle.md
 Console Nintendo Switch 2.md

BUDGETS:
📄 Budget Mois YYYY.md
 Budget Octobre 2025.md
 Budget Annuel 2025.md

ANALYSES:
📄 Analyse Type Periode.md
 Analyse Mensuelle Oct 2025.md
 Comparatif Enseignes Q4 2025.md

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-206-R206-Coloration-type-graph-view-color]]
- ⬇️ Next: [[Card-208-R208-Yaml-compta-ticket-enseigne-produit]]
- 📊 MOC: [[_MOC_Ticket receipt data extraction]]

## 🏷️ Topics

- #python
- #obsidian
- #finance
- #receipts
- #code
- #automation
