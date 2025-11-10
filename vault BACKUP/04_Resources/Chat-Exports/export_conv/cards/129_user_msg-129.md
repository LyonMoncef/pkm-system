---
type: chat-card
parent_export: '[[🚀 POWER BI / EXCEL POWER PIVOT - Architecture de rêve pour tes tickets
  de caisse !]]'
order: 129
role: user
created: '2025-11-09T20:20:59.275672Z'
tags:
- chat-card
- python
- obsidian
- finance
- receipts
attachments_count: 0
---

# 👤 Message 129 - User

**ID:** msg-129

## 💬 Content

\n\n**ID:** msg-129\n\npython# sync_obsidian_notion.py\nimport requests\nimport os\nfrom datetime import datetime\n\nNOTION_API_KEY = \"secret_XXX\"\nDATABASE_ID = \"xxx\"\n\ndef sync_ticket_to_notion(ticket_md_path):\n    \"\"\"Synchronise un ticket Obsidian vers Notion\"\"\"\n    \n    # Lire le frontmatter\n    with open(ticket_md_path, 'r', encoding='utf-8') as f:\n        content = f.read()\n    \n    # Parser YAML frontmatter\n    # ... (extraction métadonnées)\n    \n    # Créer page Notion\n    headers = {\n        \"Authorization\": f\"Bearer {NOTION_API_KEY}\",\n        \"Content-Type\": \"application/json\",\n        \"Notion-Version\": \"2022-06-28\"\n    }\n    \n    data = {\n        \"parent\": {\"database_id\": DATABASE_ID},\n        \"properties\": {\n            \"Date\": {\"date\": {\"start\": ticket_data['date']}},\n            \"Enseigne\": {\"select\": {\"name\": ticket_data['enseigne']}},\n            \"Montant\": {\"number\": ticket_data['montant']},\n            \"Lien Obsidian\": {\"url\": f\"obsidian://open?vault=MonVault&file={ticket_md_path}\"}\n        }\n    }\n    \n    response = requests.post(\n        \"https://api.notion.com/v1/pages\",\n        headers=headers,\n        json=data\n    )\n    \n    print(f\"✅ Synchronisé vers Notion : {ticket_data['date']}\")\n\n---\n\n

## 🔗 Navigation

- ⬆️ Previous: [[128_user_msg-128]]
- ⬇️ Next: [[130_assistant_msg-130]]
- 📊 MOC: [[_MOC_export_conv]]

## 🏷️ Topics

- #python
- #obsidian
- #finance
- #receipts
