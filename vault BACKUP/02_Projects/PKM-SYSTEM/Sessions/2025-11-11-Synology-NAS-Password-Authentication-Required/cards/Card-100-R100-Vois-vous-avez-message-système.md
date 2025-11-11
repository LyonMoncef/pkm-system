---
type: chat-card
parent_export: '[[Export]]'
order: 100
role: assistant
created: '2025-11-11T00:41:37.540078Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 100 - Assistant

**ID:** msg-100

## 💬 Content


**ID:** msg-100

Je vois que vous avez un message système qui apparaît régulièrement et vous souhaitez résoudre ce problème de façon permanente. Voici comment procéder :
Ce message \"Password entry required\" qui apparaît périodiquement indique qu'un processus systemd attend une saisie de mot de passe. C'est probablement lié à une tâche planifiée ou un service qui nécessite une authentification.
Pour résoudre ce problème de façon persistante via SSH :

Identifier le service concerné :

bash systemctl --all | grep password
 systemctl list-units --state=waiting

Vérifier les demandes de mot de passe en attente :

bash systemd-ask-password --list

Solutions possibles :

Configurer l'authentification sans mot de passe pour le service concerné, généralement via un fichier de configuration dans /etc/systemd/
Utiliser un keyfile ou un stockage sécurisé si c'est pour un montage crypté
Modifier le service pour qu'il ne demande plus d'authentification :


bash sudo systemctl edit [nom-du-service]
 Puis ajouter des paramètres comme `NoPasswordLogin=yes` ou équivalent selon le type de service

Désactiver le service s'il n'est pas nécessaire :

bash sudo systemctl disable [nom-du-service]

Pour Synology spécifiquement :
Ce problème peut être lié à des montages automatiques, des tâches de sauvegarde, ou des services spécifiques à Synology. Vérifiez les tâches planifiées dans l'interface DSM.

Une fois que vous avez identifié le service précis qui demande le mot de passe, la solution sera plus claire.
Voulez-vous que je vous guide dans l'identification du service spécifique qui cause ce problème ?

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-099-R099-Vois-vous-avez-message-système]]
- ⬇️ Next: [[Card-101-R101-Bash-systemctl-grep-password-systemctl]]
- 📊 MOC: [[_MOC_Synology NAS Password Authentication Required]]
