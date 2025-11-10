---
type: chat-card
parent_export: '[[Export]]'
order: 132
role: assistant
created: '2025-11-10T04:27:17.851099Z'
tags:
- chat-card
- code
attachments_count: 0
---

# 🤖 Message 132 - Assistant

**ID:** msg-132

## 💬 Content

\n\n**ID:** msg-132\n\nPour accéder à ton NAS depuis WSL Ubuntu, le plus approprié c'est CIFS/SMB avec un point de montage permanent. Voici comment faire :\nInstallation\nbashsudo apt update\nsudo apt install cifs-utils\nMontage permanent\n1. Crée un point de montage :\nbashsudo mkdir -p /mnt/nas\n2. Crée un fichier de credentials (plus sécurisé) :\nbashsudo nano /root/.nascredentials\n```\n\nContenu :\n```\nusername=ton_user_nas\npassword=ton_password_nas\ndomain=WORKGROUP\nProtège le fichier :\nbashsudo chmod 600 /root/.nascredentials\n3. Monte le NAS :\nbashsudo mount -t cifs //IP_DU_NAS/nom_partage /mnt/nas -o credentials=/root/.nascredentials,uid=$(id -u),gid=$(id -g),iocharset=utf8\n4. Montage automatique au démarrage (optionnel) :\nAjoute cette ligne dans /etc/fstab :\nbashsudo nano /etc/fstab\n```\n\nAjoute :\n```\n//IP_DU_NAS/nom_partage /mnt/nas cifs credentials=/root/.nascredentials,uid=1000,gid=1000,iocharset=utf8,nofail 0 0\nTest\nbashls /mnt/nas\nAlternative : sshfs (si ton NAS a SSH)\nSi ton NAS supporte SSH, c'est encore plus simple :\nbashsudo apt install sshfs\nmkdir ~/nas\nsshfs user@IP_NAS:/chemin ~/nas\nTu as quoi comme NAS ? (Synology, QNAP, TrueNAS ?) Et tu connais l'IP et le nom du partage ?Réessayer\n\n---\n\n

## 🔗 Navigation

- ⬆️ Previous: [[131_user_msg-131]]
- ⬇️ Next: [[133_assistant_msg-133]]
- 📊 MOC: [[_MOC_Tmux icons missing]]

## 🏷️ Topics

- #code
