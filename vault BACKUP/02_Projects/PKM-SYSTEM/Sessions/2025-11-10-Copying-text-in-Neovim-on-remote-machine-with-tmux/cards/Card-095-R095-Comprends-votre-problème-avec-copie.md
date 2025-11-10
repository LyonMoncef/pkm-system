---
type: chat-card
parent_export: '[[Export]]'
order: 95
role: assistant
created: '2025-11-10T21:10:40.959715Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 95 - Assistant

**ID:** msg-95

## 💬 Content


**ID:** msg-95

Je comprends votre problème avec la copie dans Neovim sous tmux sur une machine distante. L'erreur \"clipboard: No provider\" indique que Neovim ne trouve pas de mécanisme pour interagir avec le presse-papiers.
Voici comment résoudre ce problème :

Installez un fournisseur de presse-papiers sur votre machine distante :

Pour Debian/Ubuntu : sudo apt install xclip ou sudo apt install xsel
Pour CentOS/RHEL : sudo yum install xclip
Pour macOS, vous pouvez utiliser pbcopy/pbpaste (déjà installé)


Configurez tmux pour qu'il prenne en charge le presse-papiers :
Ajoutez ces lignes à votre fichier ~/.tmux.conf :

 set-option -g set-clipboard on
 set -g default-terminal \"screen-256color\"

Pour Neovim, vérifiez que vous avez bien le support du presse-papiers :
Exécutez :checkhealth dans Neovim pour voir les détails
Si vous travaillez depuis un terminal local vers une machine distante, vous devrez peut-être configurer le transfert X11 :

Connectez-vous avec ssh -X ou ssh -Y


Alternativement, utilisez la configuration Neovim suivante :

 set clipboard+=unnamedplus

Si rien ne fonctionne, vous pouvez utiliser un plugin comme vim-oscyank qui permet la copie à travers SSH sans dépendances externes.

Avez-vous essayé l'une de ces solutions ? Quel est votre système d'exploitation local et distant ?

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-094-R094-Comprends-votre-problème-avec-copie]]
- ⬇️ Next: [[Card-096-R096-Comprends-votre-problème-avec-copie]]
- 📊 MOC: [[_MOC_Copying text in Neovim on remote machine with tmux]]
