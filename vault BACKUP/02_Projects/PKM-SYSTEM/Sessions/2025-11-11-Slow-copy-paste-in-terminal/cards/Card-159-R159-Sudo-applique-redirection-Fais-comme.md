---
type: chat-card
parent_export: '[[Export]]'
order: 159
role: assistant
created: '2025-11-11T01:06:55.618664Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 159 - Assistant

**ID:** msg-159

## 💬 Content


**ID:** msg-159

Ah oui, le sudo ne s'applique pas à la redirection >. Fais comme ça :
bash# Extrait dans /tmp d'abord
sudo unzip /tmp/win32yank.zip -d /tmp/

# Puis déplace avec sudo
sudo mv /tmp/win32yank.exe /usr/local/bin/win32yank.exe
sudo chmod +x /usr/local/bin/win32yank.exe
Ou en une ligne avec tee :
bashunzip -p /tmp/win32yank.zip win32yank.exe | sudo tee /usr/local/bin/win32yank.exe > /dev/null
sudo chmod +x /usr/local/bin/win32yank.exe
Vérifie que ça marche :
bashwin32yank.exe --version
Puis redémarre Neovim et teste \"+p ! 🎯

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-158-R158-Utilisateur-erreur-permission-problème-s]]
- ⬇️ Next: [[Card-160-R160-Bash-Extrait-dans-abord-sudo]]
- 📊 MOC: [[_MOC_Slow copy-paste in terminal]]
