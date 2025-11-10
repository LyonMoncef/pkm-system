---
type: chat-card
parent_export: '[[Export]]'
order: 464
role: assistant
created: '2025-11-10T21:46:12.224161Z'
tags:
- chat-card
- obsidian
- code
attachments_count: 0
---

# 🤖 Message 464 - Assistant

**ID:** msg-464

## 💬 Content


**ID:** msg-464

Diagnosed YAML array syntax issue and prescribed block notation solution.L'utilisateur a un problème avec la syntaxe des propriétés related dans le frontmatter YAML. Il semble que Obsidian n'accepte pas la syntaxe avec virgules pour les liens dans une propriété array.
En YAML, pour les arrays, il y a plusieurs syntaxes possibles :

related: [item1, item2, item3] - syntaxe inline
related: suivi de lignes avec - item - syntaxe block

Le problème ici est que les [[liens]] dans un array inline avec virgules peuvent poser problème. Il faut soit :

Utiliser la syntaxe block (avec des tirets)
Ou mettre les liens entre guillemets dans l'array inline

La meilleure solution pour Obsidian est la syntaxe block :
yamlrelated:
 - \"[[MOC Raccourcis]]\"
 - \"[[Ctrl+Shift+F - Toggle Reference]]\"
 - \"[[Ctrl+Shift+H - Toggle Hub]]\"
Ou sans guillemets si Obsidian les accepte :
yamlrelated:
 - [[MOC Raccourcis]]
 - [[Ctrl+Shift+F - Toggle Reference]]
 - [[Ctrl+Shift+H - Toggle Hub]]⚠️ SYNTAXE YAML POUR ARRAYS DE LIENS
🔍 LE PROBLÈME
Obsidian n'aime pas la syntaxe inline pour les arrays de liens WikiLinks :
yamlrelated: [[Link1]], [[Link2]], [[Link3]] ❌

✅ SOLUTIONS
SOLUTION 1 : Syntaxe Block (Recommandée) ⭐
yaml---
created: 2025-10-24T15:45:00
updated: 2025-11-01T14:45:00
type: feature
status: broken
tags: [feature, shortcut, pkm-system, global, layer-1, toggle-window]
related:
 - \"[[MOC Raccourcis]]\"
 - \"[[Ctrl+Shift+F - Toggle Reference]]\"
 - \"[[Ctrl+Shift+H - Toggle Hub]]\"
source: \"développement pkm-system phase 1.5\"
---
Avec guillemets pour plus de sécurité.

SOLUTION 2 : Sans guillemets (si ton Obsidian accepte)
yamlrelated:
 - [[MOC Raccourcis]]
 - [[Ctrl+Shift+F - Toggle Reference]]
 - [[Ctrl+Shift+H - Toggle Hub]]
Teste les deux, certaines versions Obsidian préfèrent l'une ou l'autre.

SOLUTION 3 : Array de strings simples
yamlrelated: [MOC Raccourcis, Ctrl+Shift+F - Toggle Reference, Ctrl+Shift+H - Toggle Hub]
Puis tu utilises des liens dans le texte :
markdown## Liens

- [[MOC Raccourcis]]
- [[Ctrl+Shift+F - Toggle Reference]]
Inconvénient : Pas cliquable depuis les métadonnées.

🎯 FORMAT FINAL RECOMMANDÉ
yaml---
created: 2025-10-24T15:45:00
updated: 2025-11-01T14:45:00
type: feature
status: broken
priority: high
tags: [feature, shortcut, pkm-system, global, layer-1, toggle-window]
tech_stack: [electron, ipc]
dependencies: [smartToggle, preload.js]
related:
 - \"[[MOC Raccourcis]]\"
 - \"[[Ctrl+Shift+F - Toggle Reference]]\"
 - \"[[Ctrl+Shift+H - Toggle Hub]]\"
source: \"développement pkm-system phase 1.5\"
---

📝 FRONTMATTER COMPLET MIS À JOUR
Pour les 3 cartes de raccourcis :
Ctrl+Shift+Space
yaml---
created: 2025-10-24T15:45:00
updated: 2025-11-01T15:20:00
type: feature
status: broken
priority: high
tags: [feature, shortcut, pkm-system, global, layer-1, toggle-window]
tech_stack: [electron, ipc]
dependencies: [smartToggle, currentPage, preload.js]
related:
 - \"[[MOC Raccourcis]]\"
 - \"[[Ctrl+Shift+F - Toggle Reference]]\"
 - \"[[Ctrl+Shift+H - Toggle Hub]]\"
 - \"[[smartToggle Function]]\"
 - \"[[Backlog]]\"
source: \"développement pkm-system phase 1.5\"
---
Ctrl+Shift+F
yaml---
created: 2025-10-24T15:45:00
updated: 2025-11-01T15:20:00
type: feature
status: broken
priority: medium
tags: [feature, shortcut, pkm-system, global, layer-1, toggle-window]
tech_stack: [electron, ipc]
dependencies: [smartToggle, currentPage, preload.js]
related:
 - \"[[MOC Raccourcis]]\"
 - \"[[Ctrl+Shift+Space - Toggle Capture]]\"
 - \"[[Ctrl+Shift+H - Toggle Hub]]\"
 - \"[[smartToggle Function]]\"
 - \"[[Backlog]]\"
source: \"développement pkm-system phase 1.5\"
---
Ctrl+Shift+H
yaml---
created: 2025-10-24T15:45:00
updated: 2025-11-01T15:20:00
type: feature
status: broken
priority: medium
tags: [feature, shortcut, pkm-system, global, layer-1, toggle-window]
tech_stack: [electron, ipc]
dependencies: [smartToggle, currentPage, preload.js]
related:
 - \"[[MOC Raccourcis]]\"
 - \"[[Ctrl+Shift+Space - Toggle Capture]]\"
 - \"[[Ctrl+Shift+F - Toggle Reference]]\"
 - \"[[smartToggle Function]]\"
 - \"[[Backlog]]\"
source: \"développement pkm-system phase 1.5\"
---

✅ UPDATE LES 3 FICHIERS
Remplace les frontmatters des 3 cartes par ceux ci-dessus.
Ça devrait régler le problème d'invalid properties !

🤔 PROCHAINE ÉTAPE ?
A. On met à jour le MOC Raccourcis avec les liens vers ces 3 cartes
B. On crée une carte pour un raccourci qui fonctionne (Ctrl+B par exemple)
C. On passe à une autre note à refactoriser (VisuMethode, Backlog, etc.)
D. On crée le template FeatureNote.md
Ton choix ? 🚀Réessayer

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-463-S463-ID-msg-463]]
- ⬇️ Next: [[Card-465-R465-Diagnosed-YAML-array-syntax-issue]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #obsidian
- #code
