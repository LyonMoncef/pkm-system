---
created: 2025-11-01T20:15:00
updated: 2025-11-01T20:15:00
type: shortcut
tags: [shortcut, tmux, tmux-session, session-management]
shortcut: "tmux attach -t nom"
quicksummary: "Réattacher une session existante"
category: sessions
---

# tmux attach -t - Attach Session

## Action

Réattache (reconnecte) à une session tmux existante.

## Syntaxe
```bash
tmux attach -t nom_session
# ou raccourci:
tmux a -t nom_session
```

## Exemples
```bash
tmux attach -t pkm     # Réattacher session pkm
tmux a -t dev          # Raccourci pour attach
tmux a                 # Attache dernière session
```

## Use Case PKM
```bash
# Morning workflow
tmux attach -t pkm     # Reprendre où tu en étais hier
```

---

**Liens:** [[MOC - Tmux Shortcuts]] | [[tmux new -s - New Session]] | [[Ctrl+B d - Detach Session]]