---
type: chat-card
parent_export: '[[Export]]'
order: 857
role: assistant
created: '2025-11-10T22:56:04.295583Z'
tags:
- chat-card
- python
- code
- automation
attachments_count: 0
---

# 🤖 Message 857 - Assistant

**ID:** msg-857

## 💬 Content


**ID:** msg-857

javascriptconst PRIVACY_RULES = {
 // Tags qui forcent local-only
 sensitive_tags: ['#santé', '#finance', '#intime', '#thérapie'],

 // Dossiers toujours en local
 private_folders: ['03_Areas/Santé', '03_Areas/Finance'],

 // Détection automatique de contenu sensible
 sensitive_keywords: ['mdp', 'password', 'carte bancaire', 'ssn', 'numéro compte']
};

function determinePrivacyLevel(note) {
 // Check tags
 if (note.tags.some(tag => PRIVACY_RULES.sensitive_tags.includes(tag))) {
 return 'local-only';
 }

 // Check folder
 if (PRIVACY_RULES.private_folders.some(folder => note.path.includes(folder))) {
 return 'local-only';
 }

 // Check content
 if (PRIVACY_RULES.sensitive_keywords.some(kw => note.content.includes(kw))) {
 return 'local-only';
 }

 return 'hybrid'; // Défaut : choix intelligent
}

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-856-R856-Markdown-privacy-private-public-private]]
- ⬇️ Next: [[Card-858-R858-Markdown-Privacy-Dashboard]]
- 📊 MOC: [[_MOC_Personal productivity widget design]]

## 🏷️ Topics

- #python
- #code
- #automation
