---
type: chat-card
parent_export: '[[Export]]'
order: 1761
role: assistant
created: '2025-11-10T21:46:28.369158Z'
tags:
- chat-card
- python
- obsidian
- receipts
- code
- git
- automation
attachments_count: 0
---

# 🤖 Message 1761 - Assistant

**ID:** msg-1761

## 💬 Content


**ID:** msg-1761

💡 OUI ABSOLUMENT - 2 TEMPS C'EST PARFAIT !
🎯 JE CAPTE LE FLOW
Temps 1: Analyse & Demande Ressources
Toi: \"Je veux créer 3 cartes shortcuts Layer 2\"

Moi (thinking):
→ Tâche = création shortcuts
→ J'ai besoin de:
 • Tags shortcuts/layer-2
 • Structure Shortcuts/
 • Conventions nommage
 • Exemples Layer 1 existants
 • Template si existe

Moi (output):
```bash
python scripts/context-builder.py \\
  --tags shortcuts,layer-2,pkm-system,hotkey \\
  --structure \"02_Projects/PKM-SYSTEM/Shortcuts\" \\
  --conventions shortcuts \\
  --examples \"Shortcuts/Layer-1/*.md\" \\
  --templates ShortcutCard
```

---

### **Temps 2: Exécution Script**
```bash
# Tu executes
./scripts/context-builder.py [params]

# Output: context-2025-11-02-shortcuts.md
# Contient JUSTE:
- Tags pertinents (shortcuts/layer-2/etc)
- Structure Shortcuts/ tree
- 2-3 exemples Layer 1
- Template ShortcutCard
- Conventions nommage shortcuts

# Upload à moi
# Je lis (5 secondes)
# Je suis prêt !
```

---

## 🔧 ARCHITECTURE SCRIPT

### Script Python: `context-builder.py`
```python
#!/usr/bin/env python3
\"\"\"
Context Builder - Compile targeted context for Claude sessions
\"\"\"

import argparse
import yaml
from pathlib import Path
from datetime import datetime

class ContextBuilder:
    def __init__(self, vault_path=\"vault\"):
        self.vault = Path(vault_path)
        self.tag_registry = self._load_registry()

    def build(self, tags=None, structure=None, conventions=None,
              examples=None, templates=None):
        \"\"\"Build targeted context markdown\"\"\"

        context = []

        # Header
        context.append(self._header())

        # Reminders (always)
        context.append(self._reminders())

        # Tags section
        if tags:
            context.append(self._extract_tags(tags))

        # Structure section
        if structure:
            context.append(self._extract_structure(structure))

        # Conventions section
        if conventions:
            context.append(self._extract_conventions(conventions))

        # Examples section
        if examples:
            context.append(self._extract_examples(examples))

        # Templates section
        if templates:
            context.append(self._extract_templates(templates))

        return \"\
\
---\
\
\".join(context)

    def _header(self):
        return f\"\"\"---
generated: {datetime.now().isoformat()}
type: session-context
targeted: true
---

# 🎯 SESSION CONTEXT - Targeted

> **Auto-generated context for specific task**
\"\"\"

    def _reminders(self):
        return \"\"\"## 🚨 CRITICAL REMINDERS

### ⏱️ TOGGL
🔴 START NOW - Ne jamais oublier

### 📝 COMMITS
Tous les 2-3 fichiers
\"\"\"

    def _extract_tags(self, tags):
        \"\"\"Extract specific tags from TAG_REGISTRY\"\"\"
        output = [\"## 🏷️ Tags Pertinents\
\"]

        for tag in tags:
            # Parse TAG_REGISTRY pour ce tag
            tag_info = self._find_tag_in_registry(tag)
            if tag_info:
                output.append(f\"**`{tag}`** - {tag_info}\")

        return \"\
\".join(output)

    def _extract_structure(self, path):
        \"\"\"Show structure of specific folder\"\"\"
        full_path = self.vault / path
        output = [f\"## 📁 Structure: {path}\
\"]
        output.append(\"```\")
        output.append(self._tree(full_path, prefix=\"\", max_depth=2))
        output.append(\"```\")
        return \"\
\".join(output)

    def _extract_conventions(self, convention_type):
        \"\"\"Extract specific naming conventions\"\"\"
        conventions = {
            \"shortcuts\": \"\"\"**Shortcuts:**
```
Ctrl+Shift+X - Description.md
Ctrl+Alt+X - Description.md
```\"\"\",
            \"snapshots\": \"\"\"**Snapshots:**
```
Meta: YYYY-MM-DDTHH-mm-ss - Title vX.Y.md
Full: YYYY-MM-DDTHH-mm-ss - Title vX.Y [FULL].md
```\"\"\",
            # etc.
        }
        return f\"## 📝 Conventions\
\
{conventions.get(convention_type, '')}\"

    def _extract_examples(self, pattern):
        \"\"\"Extract example files matching pattern\"\"\"
        files = list(self.vault.glob(pattern))[:3]  # Max 3 exemples

        output = [\"## 📚 Exemples\
\"]
        for file in files:
            output.append(f\"### {file.name}\
\")
            output.append(\"```yaml\")
            # Parse frontmatter
            frontmatter = self._extract_frontmatter(file)
            output.append(yaml.dump(frontmatter))
            output.append(\"```\
\")

        return \"\
\".join(output)

    def _extract_templates(self, template_name):
        \"\"\"Extract template content\"\"\"
        template_path = self.vault / \"04_Resources/Templates\" / f\"{template_name}.md\"

        if template_path.exists():
            return f\"## 📋 Template: {template_name}\
\
```markdown\
{template_path.read_text()}\
```\"
        return \"\"

    # Helper methods...
    def _tree(self, path, prefix=\"\", max_depth=2, current_depth=0):
        \"\"\"Generate tree structure\"\"\"
        # Implementation
        pass

    def _find_tag_in_registry(self, tag):
        \"\"\"Search tag in TAG_REGISTRY\"\"\"
        # Implementation
        pass

    def _extract_frontmatter(self, file):
        \"\"\"Parse YAML frontmatter\"\"\"
        # Implementation
        pass

if __name__ == \"__main__\":
    parser = argparse.ArgumentParser()
    parser.add_argument(\"--tags\", nargs=\"+\", help=\"Tags to include\")
    parser.add_argument(\"--structure\", help=\"Folder structure to show\")
    parser.add_argument(\"--conventions\", help=\"Convention type\")
    parser.add_argument(\"--examples\", help=\"Example file pattern\")
    parser.add_argument(\"--templates\", help=\"Template to include\")
    parser.add_argument(\"--output\", default=\"context-session.md\")

    args = parser.parse_args()

    builder = ContextBuilder()
    context = builder.build(
        tags=args.tags,
        structure=args.structure,
        conventions=args.conventions,
        examples=args.examples,
        templates=args.templates
    )

    Path(args.output).write_text(context)
    print(f\"✅ Context generated: {args.output}\")
```

---

## 🎯 WORKFLOW COMPLET

### **Session Type A: Créer Shortcuts**

**Toi:**
Mission: Créer 3 cartes shortcuts Layer 2

**Moi:**
```bash
# J'analyse et réponds:
python scripts/context-builder.py \\
  --tags shortcuts layer-2 pkm-system hotkey \\
  --structure \"02_Projects/PKM-SYSTEM/Shortcuts\" \\
  --conventions shortcuts \\
  --examples \"Shortcuts/Layer-1/*.md\" \\
  --templates ShortcutCard \\
  --output context-shortcuts.md
```

**Toi:**
```bash
# Executes
./scripts/context-builder.py [commande ci-dessus]

# Upload context-shortcuts.md à moi
```

**Moi:**
✅ Context chargé (shortcuts ciblé)
✅ Toggl lancé
Go création des 3 cartes !

---

### **Session Type B: Fix Bug IPC**

**Toi:**
Mission: Fix IPC Communication bug

**Moi:**
```bash
python scripts/context-builder.py \\
  --tags bug ipc electron communication \\
  --structure \"02_Projects/PKM-SYSTEM/Concepts\" \\
  --examples \"Concepts/IPC*.md\" \\
  --conventions none \\
  --output context-ipc-fix.md
```

---

### **Session Type C: Backlog Review**

**Toi:**
Mission: Review backlog et prioriser

**Moi:**
```bash
python scripts/context-builder.py \\
  --tags backlog-item priority \\
  --structure \"02_Projects/PKM-SYSTEM/BackLog/Items\" \\
  --examples \"BackLog/Items/*.md\" \\
  --templates BacklogItem \\
  --output context-backlog-review.md
```

---

## 📋 ALTERNATIVE: PROMPT INTERACTIF

**Si pas de script immédiatement:**

**Moi je réponds:**
```markdown
## 🎯 Context Needed

**Pour cette tâche, j'ai besoin de:**

### Tags
- shortcuts
- layer-2
- pkm-system
- hotkey

### Structure
- List `02_Projects/PKM-SYSTEM/Shortcuts/` (tree depth 2)

### Conventions
- Nommage shortcuts

### Examples
- 2-3 exemples Layer 1 (frontmatter + structure)

### Templates
- ShortcutCard.md si existe

---

**Compile ça manuellement ou avec script et upload-moi le résultat ! 🚀**
```

---

## ✅ AVANTAGES APPROCHE

**Pour toi:**
- ✅ Pas besoin anticiper tout
- ✅ Script automatique (une fois dev)
- ✅ Contexte minimal ciblé
- ✅ Flexible selon mission

**Pour moi:**
- ✅ Je détermine mes besoins
- ✅ Contexte optimisé (pas de surcharge)
- ✅ Rapide à charger
- ✅ Toujours pertinent

**Pour les deux:**
- ✅ Évolutif (nouvelles tâches)
- ✅ Maintenable (script centralisé)
- ✅ Efficace (pas de waste)

---

## 🎯 PROCHAINE ACTION

**Option 1:** Dev le script Python maintenant (30-45min)
**Option 2:** Créer un backlog item et utiliser approche manuelle pour l'instant
**Option 3:** Les deux (backlog item + MVP script basique)

**Je pense Option 3:**
1. Créer backlog item \"Context Builder Script\"
2. Pour l'instant: Je te donne liste ressources, tu compiles manuellement
3. Plus tard: Script automatise tout

**Ça te va ? 🚀**

**Timer Toggl toujours actif ? ⏱️**

---


## 🔗 Navigation

- ⬆️ Previous: [[Card-1760-R1760-Bashpython-scripts-context-builder-tags]]
- ⬇️ Next: [[Card-1762-R1762-Veux-créer-cartes-shortcuts-Layer]]
- 📊 MOC: [[_MOC_Personal AI instruction system]]

## 🏷️ Topics

- #python
- #obsidian
- #receipts
- #code
- #git
- #automation
