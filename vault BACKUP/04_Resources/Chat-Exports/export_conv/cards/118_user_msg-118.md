---
type: chat-card
parent_export: '[[🚀 POWER BI / EXCEL POWER PIVOT - Architecture de rêve pour tes tickets
  de caisse !]]'
order: 118
role: user
created: '2025-11-09T20:20:59.088100Z'
tags:
- chat-card
- excel
- python
- obsidian
- finance
- automation
attachments_count: 0
---

# 👤 Message 118 - User

**ID:** msg-118

## 💬 Content

\n\n**ID:** msg-118\n\njson      \"shell\": \"cmd\",\n      \"command\": \"start \\\"\\\" \\\"{{vault_path}}\\\\..\\\\..\\\\NAS\\\\Compta\\\\2025\\\\{{date:MM}}-{{date:MMMM}}\\\\{{title}}.pdf\\\"\",\n      \"alias\": \"📄 Ouvrir PDF\"\n    },\n    {\n      \"id\": \"open-dashboard\",\n      \"name\": \"Ouvrir Dashboard Excel\",\n      \"shell\": \"cmd\",\n      \"command\": \"start \\\"\\\" \\\"\\\\\\\\NAS\\\\Compta\\\\2025\\\\Dashboards\\\\Dashboard_Compta_2025.xlsx\\\"\",\n      \"alias\": \"📊 Dashboard\"\n    },\n    {\n      \"id\": \"sync-nas\",\n      \"name\": \"Synchroniser avec NAS\",\n      \"shell\": \"powershell\",\n      \"command\": \"python \\\"C:\\\\Scripts\\\\sync_compta_nas.py\\\"\",\n      \"alias\": \"🔄 Sync NAS\"\n    },\n    {\n      \"id\": \"import-new-tickets\",\n      \"name\": \"Importer nouveaux tickets\",\n      \"shell\": \"python\",\n      \"command\": \"python \\\"C:\\\\Scripts\\\\import_tickets_obsidian.py\\\"\",\n      \"alias\": \"📥 Import Tickets\"\n    },\n    {\n      \"id\": \"backup-vault\",\n      \"name\": \"Backup Vault vers NAS\",\n      \"shell\": \"powershell\",\n      \"command\": \"robocopy \\\"{{vault_path}}\\\" \\\"\\\\\\\\NAS\\\\Backups\\\\Obsidian\\\\{{date:YYYY-MM-DD}}\\\" /MIR /R:3\",\n      \"alias\": \"💾 Backup\"\n    }\n  ]\n}\n\n---\n\n

## 🔗 Navigation

- ⬆️ Previous: [[117_user_msg-117]]
- ⬇️ Next: [[119_user_msg-119]]
- 📊 MOC: [[_MOC_export_conv]]

## 🏷️ Topics

- #excel
- #python
- #obsidian
- #finance
- #automation
