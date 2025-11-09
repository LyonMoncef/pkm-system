---
created: 2025-11-01T20:15:00
updated: 2025-11-01T20:15:00
type: shortcut
tags: [shortcut, tmux, tmux-pane, split, layout]
shortcut: "Ctrl+B %"
quicksummary: "Split vertical du pane actif"
category: panes
---

# Ctrl+B % - Split Vertical

## Action

Divise le pane actuel verticalement (│).

## Séquence
```
1. Ctrl+B    (prefix)
2. %         (split vertical)
```

## Résultat
```
Avant:                  Après:
┌──────────────┐       ┌───────┬──────┐
│              │       │       │      │
│    Pane      │  →    │ Pane 1│Pane 2│
│              │       │       │      │
└──────────────┘       └───────┴──────┘
```

## Navigation

Utiliser [[Ctrl+B arrow - Navigate Panes]] pour se déplacer entre les panes.

## Use Case PKM
```
┌─────────────┬────────┐
│   Nvim      │  Git   │
│   Notes     │ Status │
└─────────────┴────────┘
```

---

**Liens:** [[MOC - Tmux Shortcuts]] | [[Ctrl+B " - Split Horizontal]] | [[Ctrl+B z - Toggle Fullscreen]]