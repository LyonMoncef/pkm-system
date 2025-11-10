---
type: chat-card
parent_export: '[[Export]]'
order: 132
role: assistant
created: '2025-11-10T21:08:50.814753Z'
tags:
- chat-card
attachments_count: 0
---

# 🤖 Message 132 - Assistant

**ID:** msg-132

## 💬 Content


**ID:** msg-132

Dans ce fichier, les raccourcis clavier sont définis dans le contexte de l'autocomplétion avec nvim-cmp et LuaSnip. Plus précisément :
Ces raccourcis sont actifs uniquement pendant le mode d'insertion (insert mode) et spécifiquement lorsque :

Le menu d'autocomplétion est visible
Vous êtes en train d'éditer un snippet

Les touches configurées sont principalement définies dans le bloc mapping = cmp.mapping.preset.insert { ... } et sont actives dans ces contextes spécifiques :

Navigation dans le menu d'autocomplétion :

<C-n> et <C-p> : Navigation entre les suggestions (suivant/précédent)
<Tab> et <S-Tab> : Navigation alternative entre les suggestions


Documentation et confirmation :

<C-b> et <C-f> : Défilement de la fenêtre de documentation
<C-y> : Accepter la suggestion sélectionnée
<C-Space> : Déclencher manuellement le menu d'autocomplétion


Navigation dans les snippets :

<C-l> : Avancer dans les points d'expansion d'un snippet
<C-h> : Reculer dans les points d'expansion d'un snippet
<Tab> et <S-Tab> : Ont une double fonction - navigation dans les suggestions si le menu est visible, ou navigation dans les snippets si un snippet est actif


Tous ces raccourcis fonctionnent principalement en mode insertion ('i') et certains également en mode snippet ('s') comme indiqué par { 'i', 's' } dans la définition de certains mappages.
Le système est conçu pour être contextuel : par exemple, la touche Tab aura un comportement différent selon que le menu d'autocomplétion est visible, qu'un snippet est en cours d'édition, ou aucun des deux (dans ce dernier cas, il revient au comportement par défaut avec fallback()).

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-131-R131-Dans-fichier-raccourcis-clavier-sont]]
- ⬇️ Next: [[Card-133-R133-Dans-fichier-raccourcis-clavier-sont]]
- 📊 MOC: [[_MOC_Configuring Quarto.lua Plugin for Neovim Jupyter Notebook Simulation]]
