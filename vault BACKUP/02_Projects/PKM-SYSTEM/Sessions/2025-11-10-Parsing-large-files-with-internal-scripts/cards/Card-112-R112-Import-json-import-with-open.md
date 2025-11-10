---
type: chat-card
parent_export: '[[Export]]'
order: 112
role: assistant
created: '2025-11-10T21:43:33.604114Z'
tags:
- chat-card
- python
attachments_count: 0
---

# 🤖 Message 112 - Assistant

**ID:** msg-112

## 💬 Content


**ID:** msg-112

python3 << 'EOF'
import json
import re

with open('/mnt/project/export_conv.md', 'r') as f:
 content = json.loads(f.read())

# Chercher tous les messages User (probablement où commence le vrai contenu)
user_messages = []
lines = content.split('\
')

for i, line in enumerate(lines):
 if 'Message' in line and 'User' in line:
 # Extraire le numéro du message
 match = re.search(r'Message (\\d+)', line)
 if match:
 msg_num = int(match.group(1))
 # Prendre jusqu'à 50 lignes suivantes (ou jusqu'au prochain message)
 next_msg_line = i + 50
 for j in range(i+1, min(i+100, len(lines))):
 if lines[j].startswith('## ') and 'Message' in lines[j]:
 next_msg_line = j
 break

 msg_content = '\
'.join(lines[i:next_msg_line])
 user_messages.append({
 'line': i,
 'number': msg_num,
 'preview': msg_content[:500]
 })

print(f\"Messages User trouvés: {len(user_messages)}\
\")
print(\"=== 3 PREMIERS MESSAGES USER ===\
\")
for msg in user_messages[:3]:
 print(f\"--- Message {msg['number']} (ligne {msg['line']}) ---\")
 print(msg['preview'])
 print()
EOF

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-111-R111-Import-json-import-with-open]]
- ⬇️ Next: [[Card-113-R113-SortieMessages-User-trouvés-PREMIERS-MES]]
- 📊 MOC: [[_MOC_Parsing large files with internal scripts]]

## 🏷️ Topics

- #python
