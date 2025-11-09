---
created: 2025-11-01T20:15:00
updated: 2025-11-01T20:15:00
type: shortcut
tags: [shortcut, tmux, tmux-session, session-management]
shortcut: "tmux new -s nom"
quicksummary: "Créer une nouvelle session nommée"
category: sessions
---

# tmux new -s - New Session

## Action

Crée une nouvelle session tmux avec un nom spécifique.

## Syntaxe
```bash
tmux new -s nom_session
```

## Exemples
```bash
tmux new -s pkm        # Session pour notes PKM
tmux new -s dev        # Session développement
tmux new -s server     # Session monitoring serveur
```

## Use Case PKM
```bash
tmux new -s pkm
cd ~/vault
nvim .
```

---

**Liens:** [[MOC - Tmux Shortcuts]] | [[tmux attach -t - Attach Session]]