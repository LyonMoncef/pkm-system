---
type: chat-card
parent_export: '[[Export]]'
order: 94
role: assistant
created: '2025-11-11T00:40:04.468505Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 94 - Assistant

**ID:** msg-94

## 💬 Content


**ID:** msg-94

Pour supprimer les anciennes versions de Neovim (nvim) sur Ubuntu, voici comment procéder :

Vérifiez d'abord les versions installées avec :

 dpkg -l | grep nvim
ou
 which -a nvim

Si vous avez installé Neovim via apt, supprimez-le avec :

 sudo apt remove neovim
 sudo apt purge neovim

Si vous avez installé via snap :

 sudo snap remove neovim

Pour les versions installées manuellement ou via AppImage, localisez-les (souvent dans /usr/local/bin, ~/.local/bin, ou /opt) puis supprimez-les :

 sudo rm /chemin/vers/nvim

N'oubliez pas de nettoyer les configurations si nécessaire :

 rm -rf ~/.config/nvim
 rm -rf ~/.local/share/nvim
Après la suppression, vous pouvez installer une seule version propre via la méthode de votre choix.
Avez-vous installé vos différentes versions de nvim par des méthodes spécifiques ?Réessayer

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-093-S093-Supprimer-les-anciennes-versions]]
- ⬇️ Next: [[Card-095-R095-Pour-supprimer-anciennes-versions-Neovim]]
- 📊 MOC: [[_MOC_Removing Old Neovim Versions on Ubuntu]]
