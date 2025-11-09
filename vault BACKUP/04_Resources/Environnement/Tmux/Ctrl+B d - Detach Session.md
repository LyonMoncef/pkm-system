---
created: 2025-11-01T20:15:00
updated: 2025-11-01T20:15:00
type: shortcut
tags: [shortcut, tmux, tmux-session, session-management]
shortcut: "Ctrl+B d"
quicksummary: "Détacher de la session (continue en background)"
category: sessions
---

# Ctrl+B d - Detach Session

## Action

Détache de la session actuelle. La session continue de tourner en background.

## Séquence
```
1. Ctrl+B    (prefix)
2. d         (detach)
```

## Résultat
```
[detached (from session pkm)]
```

La session reste active et peut être réattachée plus tard avec [[tmux attach -t - Attach Session]].

## Use Case PKM
```bash
# En train d'éditer des notes
Ctrl+B d                # Détacher session
# Faire autre chose...
tmux attach -t pkm      # Reprendre plus tard
```

---

**Liens:** [[MOC - Tmux Shortcuts]] | [[tmux attach -t - Attach Session]]