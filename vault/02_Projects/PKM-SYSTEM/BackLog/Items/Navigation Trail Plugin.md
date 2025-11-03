---
created: 2025-11-02T12:00:00
updated: 2025-11-02T12:00:00
type: backlog-item
category: feature
priority: medium
status: todo
tags: [plugin, navigation, ux, obsidian]
estimated_time: "8-12h"
estimated_time_minutes: 600
actual_time: ""
related:
  - "[[Next Action Choice]]"
  - "[[TODO]]"
---

# Navigation Trail Plugin - Visual Breadcrumb

## 🎯 Description

Plugin Obsidian pour afficher un trail visuel de navigation dans le file explorer avec surbrillance dégradée.

## 📋 Contexte

**Problème:**
Quand on navigue entre notes (A→B→C), on perd le contexte visuel dans l'explorer.

**Use Case:**
- Navigation entre snapshots (Meta → Full → Living)
- Édition multi-notes avec retours fréquents
- Garderie contexte du "d'où je viens"

**Inspiration:**
Session 2025-11-02 snapshots - navigation circulaire Living→Meta→Full

## 🔧 Solutions Possibles

### Option A: Plugin Custom Obsidian ⭐
**Description:** Plugin natif utilisant API Obsidian  
**Avantages:**
- Intégration native
- Access API workspace
- Performance optimale

**Inconvénients:**
- Développement 8-12h
- Maintenance plugin

**Temps estimé:** 8-12h

**Architecture:**
```typescript
class NavigationTrailPlugin {
  trail: string[] = [];
  maxTrail = 5;
  
  onload() {
    workspace.on('active-leaf-change', this.updateTrail);
  }
  
  updateTrail(leaf) {
    // Update stack
    // Add CSS classes to explorer items
  }
}
```

### Option B: CSS Snippet
**Description:** Simple CSS avec data attributes  
**Avantages:**
- Quick fix (30min)
- Pas de dev plugin

**Inconvénients:**
- Faut script externe pour data attributes
- Moins flexible

**Temps estimé:** 30min-1h

## 🎨 Comportement Souhaité

**Surbrillance:**
- Note active: opacity 1.0, couleur accent MAX
- Trail -1: opacity 0.6
- Trail -2: opacity 0.3
- Trail -3+: opacity 0.1

**Options:**
- Button "X" pour remove item du trail
- Button "Reset" pour clear tout le trail
- Config: max trail size (3-10)

**Decay:**
- Option A: Par ordre de navigation (LIFO)
- Option B: Par temps (expire après 5min)

## 📊 Critères Acceptation

- [ ] Surbrillance visible note active
- [ ] Trail visible (3-5 notes précédentes)
- [ ] Dégradé visuel clair
- [ ] Performance OK (pas de lag)
- [ ] Option reset trail
- [ ] Config max trail size

## 🔗 Ressources

**Plugins similaires:**
- Pane Relief (breadcrumbs mais pas explorer)
- Recent Files (liste séparée)
- Quiet Outline (highlight active)

**API Obsidian:**
- `workspace.on('active-leaf-change')`
- `app.vault.getAbstractFileByPath()`
- DOM: `.nav-file-title`

**Liens:**
- [Obsidian Plugin API](https://docs.obsidian.md/Plugins)
- [[Next Action Choice]] - Use case source

---

## 📝 Notes

**Décision:** Commencer par Option B (CSS snippet) pour tester UX.  
Si usage intensif → Migrer vers Option A (plugin custom).

---

**Créé:** 2025-11-02T12:00:00  
**Inspiration:** Session navigation snapshots