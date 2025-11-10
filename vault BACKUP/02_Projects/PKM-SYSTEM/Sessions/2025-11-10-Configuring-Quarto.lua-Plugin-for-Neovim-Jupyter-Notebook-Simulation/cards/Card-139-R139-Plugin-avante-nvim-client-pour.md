---
type: chat-card
parent_export: '[[Export]]'
order: 139
role: assistant
created: '2025-11-10T21:08:50.898048Z'
tags:
- chat-card
- python
- automation
attachments_count: 0
---

# 🤖 Message 139 - Assistant

**ID:** msg-139

## 💬 Content


**ID:** msg-139

Le plugin avante.nvim est un client d'IA pour Neovim qui permet d'interagir avec des modèles comme Claude ou GPT directement dans l'éditeur. Voici comment l'utiliser une fois installé :

Installation préalable :

Assurez-vous d'avoir correctement configuré avante.nvim avec Lazy.nvim ou votre gestionnaire de plugins
Vérifiez que vous avez une clé API pour le fournisseur choisi (Claude ou OpenAI dans ce cas)


Configuration des variables d'environnement :

Définissez votre clé API via ANTHROPIC_API_KEY pour Claude ou OPENAI_API_KEY pour OpenAI
Vous pouvez éventuellement personnaliser l'endpoint avec AVANTE_ANTHROPIC_ENDPOINT ou AVANTE_OPENAI_ENDPOINT


Commandes principales :

:Avante - Ouvre une nouvelle conversation avec l'IA
:AvanteToggle - Bascule l'affichage du panneau de conversation
:AvanteInsert - Insère la réponse de l'IA à l'emplacement du curseur
:AvantePrompt - Envoie un prompt à l'IA et insère la réponse
:AvanteCode - Demande à l'IA de générer du code à partir d'une description


Sélection de texte :

Vous pouvez sélectionner du texte en mode visuel puis utiliser :Avante pour envoyer ce texte à l'IA
Ou utiliser :AvanteRewrite, :AvanteExplain, :AvanteRefactor sur la sélection


Raccourcis clavier recommandés :
Vous pouvez ajouter ces raccourcis à votre configuration :

lua vim.keymap.set('n', '<leader>aa', '<cmd>Avante<CR>', { desc = 'Open Avante' })
 vim.keymap.set('n', '<leader>at', '<cmd>AvanteToggle<CR>', { desc = 'Toggle Avante' })
 vim.keymap.set('v', '<leader>ap', '<cmd>AvantePrompt<CR>', { desc = 'Prompt Avante with selection' })
 vim.keymap.set('v', '<leader>ac', '<cmd>AvanteCode<CR>', { desc = 'Generate code with Avante' })

Fonctionnalités avancées :

Support du glisser-déposer d'images grâce au plugin img-clip.nvim
Intégration avec différents sélecteurs de fichiers (mini.pick, telescope, fzf)
Auto-complétion des commandes via nvim-cmp


Personnalisation :

Vous pouvez modifier les paramètres comme temperature, max_tokens dans votre configuration
Changer le modèle utilisé en modifiant model dans la configuration


Cette configuration utilise Claude par défaut (provider = 'claude'), mais vous pouvez facilement passer à OpenAI en changeant cette valeur.Réessayer

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-138-Q138-On-utilise-ce-plugin]]
- ⬇️ Next: [[Card-140-R140-Plugin-avante-nvim-client-pour]]
- 📊 MOC: [[_MOC_Configuring Quarto.lua Plugin for Neovim Jupyter Notebook Simulation]]

## 🏷️ Topics

- #python
- #automation
