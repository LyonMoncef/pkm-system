---
type: chat-card
parent_export: '[[Export]]'
order: 216
role: assistant
created: '2025-11-11T00:41:53.449967Z'
tags:
- chat-card
- python
- obsidian
- finance
- receipts
attachments_count: 0
---

# 🤖 Message 216 - Assistant

**ID:** msg-216

## 💬 Content


**ID:** msg-216

python# sync_obsidian_notion.py
import requests
import os
from datetime import datetime

NOTION_API_KEY = \"secret_XXX\"
DATABASE_ID = \"xxx\"

def sync_ticket_to_notion(ticket_md_path):
 \"\"\"Synchronise un ticket Obsidian vers Notion\"\"\"

 # Lire le frontmatter
 with open(ticket_md_path, 'r', encoding='utf-8') as f:
 content = f.read()

 # Parser YAML frontmatter
 # ... (extraction métadonnées)

 # Créer page Notion
 headers = {
 \"Authorization\": f\"Bearer {NOTION_API_KEY}\",
 \"Content-Type\": \"application/json\",
 \"Notion-Version\": \"2022-06-28\"
 }

 data = {
 \"parent\": {\"database_id\": DATABASE_ID},
 \"properties\": {
 \"Date\": {\"date\": {\"start\": ticket_data['date']}},
 \"Enseigne\": {\"select\": {\"name\": ticket_data['enseigne']}},
 \"Montant\": {\"number\": ticket_data['montant']},
 \"Lien Obsidian\": {\"url\": f\"obsidian://open?vault=MonVault&file={ticket_md_path}\"}
 }
 }

 response = requests.post(
 \"https://api.notion.com/v1/pages\",
 headers=headers,
 json=data
 )

 print(f\"✅ Synchronisé vers Notion : {ticket_data['date']}\")

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-215-R215-Dashboard-style-markdown-preview-view]]
- ⬇️ Next: [[Card-217-R217-Claude-peut-faire-erreurs-Assurez]]
- 📊 MOC: [[_MOC_Ticket receipt data extraction]]

## 🏷️ Topics

- #python
- #obsidian
- #finance
- #receipts
