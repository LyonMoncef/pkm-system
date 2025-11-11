---
type: chat-card
parent_export: '[[Export]]'
order: 134
role: assistant
created: '2025-11-11T00:45:56.471032Z'
tags:
- chat-card
- code
attachments_count: 0
---

# 🤖 Message 134 - Assistant

**ID:** msg-134

## 💬 Content


**ID:** msg-134

Pour accéder à ton NAS depuis WSL Ubuntu, le plus approprié c'est CIFS/SMB avec un point de montage permanent. Voici comment faire :
Installation
bashsudo apt update
sudo apt install cifs-utils
Montage permanent
1. Crée un point de montage :
bashsudo mkdir -p /mnt/nas
2. Crée un fichier de credentials (plus sécurisé) :
bashsudo nano /root/.nascredentials
```

Contenu :
```
username=ton_user_nas
password=ton_password_nas
domain=WORKGROUP
Protège le fichier :
bashsudo chmod 600 /root/.nascredentials
3. Monte le NAS :
bashsudo mount -t cifs //IP_DU_NAS/nom_partage /mnt/nas -o credentials=/root/.nascredentials,uid=$(id -u),gid=$(id -g),iocharset=utf8
4. Montage automatique au démarrage (optionnel) :
Ajoute cette ligne dans /etc/fstab :
bashsudo nano /etc/fstab
```

Ajoute :
```
//IP_DU_NAS/nom_partage /mnt/nas cifs credentials=/root/.nascredentials,uid=1000,gid=1000,iocharset=utf8,nofail 0 0
Test
bashls /mnt/nas
Alternative : sshfs (si ton NAS a SSH)
Si ton NAS supporte SSH, c'est encore plus simple :
bashsudo apt install sshfs
mkdir ~/nas
sshfs user@IP_NAS:/chemin ~/nas
Tu as quoi comme NAS ? (Synology, QNAP, TrueNAS ?) Et tu connais l'IP et le nom du partage ?

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-133-R133-Pour-accéder-depuis-Ubuntu-plus]]
- ⬇️ Next: [[Card-135-R135-Bashsudo-update-sudo-install-cifs]]
- 📊 MOC: [[_MOC_Tmux icons missing]]

## 🏷️ Topics

- #code
