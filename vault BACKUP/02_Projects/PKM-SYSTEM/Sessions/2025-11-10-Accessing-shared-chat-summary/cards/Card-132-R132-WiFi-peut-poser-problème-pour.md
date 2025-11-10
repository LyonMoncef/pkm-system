---
type: chat-card
parent_export: '[[Export]]'
order: 132
role: assistant
created: '2025-11-10T21:06:08.682412Z'
tags:
- chat-card
- git
attachments_count: 0
---

# 🤖 Message 132 - Assistant

**ID:** msg-132

## 💬 Content


**ID:** msg-132

Ah, le WiFi peut poser problème pour rejoindre un domaine ! Voici comment diagnostiquer :
Vérifications rapides :
1. Vérifier la configuration réseau

Ouvrir cmd en admin
Taper : ipconfig /all
Vérifier que les serveurs DNS pointent bien vers votre contrôleur de domaine (et pas 8.8.8.8 ou autres DNS publics)

2. Tester la connectivité avec le DC
cmdping nom-de-votre-domaine.local
ping adresse-ip-du-controleur-domaine
nslookup nom-de-votre-domaine.local
Solutions possibles :
Solution 1 : Câble Ethernet (recommandé)

Si possible, branchez le PC en Ethernet pour rejoindre le domaine
C'est beaucoup plus fiable que le WiFi pour cette opération
Une fois sur le domaine, le WiFi fonctionnera normalement

Solution 2 : Configurer les DNS manuellement

Paramètres → Réseau → WiFi → Propriétés de votre réseau
Passer le DNS en manuel
Entrer l'IP de votre contrôleur de domaine comme DNS primaire

Question :

Avez-vous un câble Ethernet à disposition ?
Connaissez-vous l'adresse IP de votre contrôleur de domaine ?

Dites-moi ce que donnent les ping/nslookup ! 🔍

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-131-R131-Utilisateur-essaie-rejoindre-domaine-mai]]
- ⬇️ Next: [[Card-133-R133-Cmdping-votre-domaine-local-ping]]
- 📊 MOC: [[_MOC_Accessing shared chat summary]]

## 🏷️ Topics

- #git
