## 🔒 Privacy & Security

### [ ] Review Toggl Tasks Privacy

**Priorité:** 🟡 MEDIUM  
**Temps estimé:** 1-2h  
**Tags:** `#privacy` `#security` `#toggl`

**Problème:**
Actuellement, toutes les tâches Toggl sont versionnées dans Git (publiquement accessibles si repo public).

**Données dans tasks Toggl:**
- Temps estimé/réel de travail
- Timestamps précis des sessions
- Patterns de travail personnels
- Potentiellement données sensibles dans descriptions

**Options à explorer:**

**A. Filtrage sélectif .gitignore**
```gitignore
# Versionner structure mais pas contenu
!vault/02_Projects/PKM-SYSTEM/Toggl/
vault/02_Projects/PKM-SYSTEM/Toggl/**
!vault/02_Projects/PKM-SYSTEM/Toggl/README.md
!vault/02_Projects/PKM-SYSTEM/Toggl/Templates/
```

**B. Anonymisation automatique**
- Script qui sanitize les tasks avant commit
- Remplace timestamps précis par plages
- Garde estimations mais supprime temps réel

**C. Split repo**
- Repo public: Code + Doc
- Repo privé: Notes + Toggl

**D. Variables d'environnement**
```markdown
Temps réel: {{TOGGL_TIME_ACTUAL}} # Pas commité
Temps estimé: 30min # Commité
```

**Décision:** À prendre plus tard quand besoin collaboration/partage

**Liens:**
- [[TODO]]
- [[TAG_REGISTRY]]
- Discussion initiale: 2025-11-02 session

---

**Created:** 2025-11-02T11:45:00  
**Review date:** Avant premier partage public du repo