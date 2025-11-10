---
type: chat-card
parent_export: '[[🚀 POWER BI / EXCEL POWER PIVOT - Architecture de rêve pour tes tickets
  de caisse !]]'
order: 120
role: user
created: '2025-11-09T20:20:59.109287Z'
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

# 👤 Message 120 - User

**ID:** msg-120

## 💬 Content

\n\n**ID:** msg-120\n\njavascript// Template Capture Rapide Ticket\nmodule.exports = async (params) => {\n    const {quickAddApi: qa} = params;\n    \n    // Demander les infos essentielles\n    const enseigne = await qa.suggester(\n        [\"E.Leclerc\", \"Carrefour\", \"TotalEnergies\", \"McDonald's\", \"Action\", \"Autre\"],\n        [\"E.Leclerc\", \"Carrefour\", \"TotalEnergies\", \"McDonald's\", \"Action\", \"Autre\"]\n    );\n    \n    const montant = await qa.inputPrompt(\"Montant total (€)\");\n    \n    const date = qa.date.now(\"YYYY-MM-DD\");\n    const heure = qa.date.now(\"HH:mm\");\n    \n    // Créer note minimale\n    const filename = `${date} ${enseigne} - BROUILLON`;\n    const folder = \"00-INBOX\";\n    \n    const content = `---\ntype: ticket\ndate: ${date}\nheure: \"${heure}\"\nenseigne: \"[[${enseigne}]]\"\nmontant_total: ${montant}\nstatus: brouillon\ntags:\n  - compta/inbox\n  - compta/a-traiter\n---\n\n# 🧾 ${filename}\n\n> [!warning] À compléter\n> Ticket capturé rapidement depuis mobile\n\n## 📸 Photo du ticket\n![[]]\n\n## ✅ À faire\n- [ ] Ajouter détail articles\n- [ ] Uploader photo ticket\n- [ ] Vérifier montant\n- [ ] Copier vers NAS\n- [ ] Classer dans dossier mois\n\n---\nCréé : ${date} ${heure}\n`;\n    \n    await qa.createNote(filename, content, folder);\n    \n    return;\n};\n```\n\n### **iOS Shortcuts - Automation complète**\n```\n📱 SHORTCUT: \"Nouveau Ticket\"\n\n1. Prendre photo du ticket\n2. OCR avec Vision API\n3. Extraire : date, enseigne, montant\n4. Créer note Obsidian via Obsidian URI\n5. Uploader photo vers NAS (via SMB ou app Files)\n6. Notification : \"✅ Ticket capturé\"\n```\n\n---\n\n## 🗂️ **ORGANISATION & CONVENTIONS DE NOMMAGE**\n\n### **Noms de fichiers standardisés**\n```\nTICKETS:\n📄 YYYY-MM-DD Enseigne Ville.md\n   2025-10-07 E.Leclerc Vienne.md\n   2025-10-12 McDonald's Vienne.md\n\nENSEIGNES:\n📄 Nom Enseigne.md\n   E.Leclerc.md\n   Carrefour Market.md\n\nPRODUITS:\n📄 Nom Produit Marque.md\n   Gazpacho Alvalle.md\n   Console Nintendo Switch 2.md\n\nBUDGETS:\n📄 Budget Mois YYYY.md\n   Budget Octobre 2025.md\n   Budget Annuel 2025.md\n\nANALYSES:\n📄 Analyse Type Periode.md\n   Analyse Mensuelle Oct 2025.md\n   Comparatif Enseignes Q4 2025.md\n\n---\n\n

## 🔗 Navigation

- ⬆️ Previous: [[119_user_msg-119]]
- ⬇️ Next: [[121_user_msg-121]]
- 📊 MOC: [[_MOC_export_conv]]

## 🏷️ Topics

- #python
- #obsidian
- #finance
- #receipts
- #code
- #automation
