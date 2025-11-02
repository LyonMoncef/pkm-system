# 🐛 PKM System - Backlog

## 🔴 BUGS (Priorité Haute)

### Navigation & Hotkeys

- [ ] **Ctrl+Shift+F ne fonctionne pas** depuis les widgets
    
    - Issue: Les iframes bloquent les events du parent
    - Solution probable: PostMessage entre iframe et parent
    - Priorité: **HAUTE**
- [ ] **ESC ne retourne pas au hub** depuis les widgets
    
    - Issue: Même problème d'isolation iframe
    - Solution: PostMessage communication
    - Priorité: **HAUTE**

---

## 🟡 AMÉLIORATIONS (Priorité Moyenne)

### Features Quick Capture

- [ ] Save vers fichiers RÉELS (pas localStorage)
    
    - Implémenter file system API ou Electron
    - Sauvegarder dans vault Obsidian
- [ ] Tags system
    
    - Auto-completion des tags
    - Filtrage par tags
- [ ] Templates rapides
    
    - Daily note, Project, Idea, etc.

### Features Quick Reference

- [ ] Ajouter/éditer cheatsheets depuis l'interface
    
    - Bouton "+ New Cheatsheet"
    - Editor inline
- [ ] Pin/Unpin fonctionnel
    
    - Toggle pin state
    - Persist dans localStorage
- [ ] Export cheatsheets en PDF/MD
    

### UI/UX

- [ ] Animations de transition plus smooth
- [ ] Dark mode toggle (actuellement fixe)
- [ ] Personnalisation couleurs/thème
- [ ] Responsive mobile

---

## 🟢 FEATURES FUTURES (Priorité Basse)

### Phase 2

- [ ] Migration vers Electron (vraie app desktop)
- [ ] Hotkeys système natifs (fonctionne partout)
- [ ] Tray icon
- [ ] Auto-start au démarrage

### Intégration Obsidian

- [ ] Bouton "Pin to Widget" dans Obsidian
- [ ] Sync bidirectionnel vault ↔ widget
- [ ] Import notes Obsidian dans Quick Ref

### Collaboration (Phase 3)

- [ ] Sharing notes avec cercles
- [ ] Contributions externes
- [ ] Public platform

---

## 🔧 TECHNICAL DEBT

- [ ] Refactor code en modules ES6
- [ ] Séparer CSS dans fichiers externes
- [ ] Tests unitaires (Jest)
- [ ] CI/CD pipeline
- [ ] Minification assets

---

## 📝 NOTES

**Problème iframe :** Les widgets sont chargés dans des iframes, ce qui isole complètement leurs events du parent. Les hotkeys globaux ne fonctionnent que dans le contexte de la page parente (hub.html), pas dans les iframes.

**Solutions possibles :**

1. **PostMessage API** - Communication parent ↔ iframe
2. **Migration Electron** - Pas d'iframe, vraies fenêtres
3. **Service Worker** - Intercepter events globalement

**Pour le MVP :** On peut vivre sans (navigation via boutons fonctionne).  
**Pour V2 :** Migration Electron = solution propre.

---

_Mis à jour : 2025-10-18_

==============================

## 📋 **AJOUT AU BACKLOG**

**Amélioration UX Save :**

- [ ]  Popup unique "Note saved. Start new note?" avec checkbox "Don't ask again"
- [ ]  Préférence sauvegardée (localStorage ou config file)
- [ ]  Priorité : Moyenne (ergonomie)

-- Le 20/10/2025 à 04:11


## 🔮 Features Futures

### [ ] Navigation Trail Plugin - Visual Breadcrumb

**Priorité:** 🟡 MEDIUM  
**Temps estimé:** 8-12h (développement plugin)  
**Tags:** `#plugin #navigation #ux #obsidian`

**Besoin:**
Surbrillance visuelle dans file explorer du trail de navigation.

**Comportement souhaité:**
- Note active: surbrillance MAX
- Notes visitées: dégradé en fonction ancienneté/ordre
- Option "X" pour remove du trail
- Option reset complet du trail
- Configurable: max trail size (3-10 notes)

**Approches:**
1. **Plugin custom Obsidian** (recommandé)
   - Hook `active-leaf-change`
   - Stack navigation LIFO
   - Classes CSS dynamiques sur explorer
   
2. **CSS Snippet** (quick fix temporaire)
   - Moins flexible
   - Faut script externe pour data attributes

**Ressources:**
- Obsidian API: workspace events
- Plugins similaires: Pane Relief, Recent Files
- DOM: `.nav-file-title` manipulation

**Exemples use case:**
- Naviguer A→B→C, garder contexte visuel
- Éditer B, voir que vient de A, va vers C
- Reset trail quand changement de sujet

**Décision:** Plugin custom si utilisation intensive, sinon CSS snippet

**Liens:**
- [[TODO]]
- Discussion: 2025-11-02 session snapshots

---

**Created:** 2025-11-02T12:00:00  
**Inspiration:** Session navigation entre snapshots Meta/Full/Living

