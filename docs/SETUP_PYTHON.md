# 🐍 Python Setup - PKM System

## 📋 Installation Python + venv

### 1. Installer Python

```bash
# Vérifier si déjà installé
python3 --version

# Si pas installé (WSL/Linux)
sudo apt update
sudo apt install python3 python3-pip python3-venv

# Vérifier installation
python3 --version  # Python 3.8+
pip3 --version     # pip installé
```

### 2. Créer l'environnement virtuel

```bash
cd /mnt/c/Users/idsmf/Projects/pkm-system

# Créer venv
python3 -m venv venv

# ✅ Dossier venv/ créé
```

### 3. Activer le venv

```bash
# Activer
source venv/bin/activate

# Ton prompt devient :
# (venv) user@machine:~/pkm-system$
#  ^^^^^ = venv activé ✅
```

### 4. Installer les dépendances

```bash
# Dans le venv activé
pip install -r scripts/chat-atomizer/requirements.txt

# Vérifier
pip list
# → PyYAML 6.0+
```

### 5. Mettre à jour .gitignore

```bash
# Ajouter au .gitignore existant
cat >> .gitignore << 'EOF'

# Python
venv/
__pycache__/
*.pyc
*.pyo
*.egg-info/
EOF
```

---

## 🔧 Usage Quotidien

### Démarrer une session

```bash
cd /mnt/c/Users/idsmf/Projects/pkm-system

# Activer venv
source venv/bin/activate

# Ou utilise le helper
source activate-venv.sh

# Travailler
python scripts/chat-atomizer/atomize_chat.py ...
```

### Terminer une session

```bash
# Désactiver venv
deactivate

# Ton prompt redevient normal
```

---

## 📦 Gestion des Dépendances

### Ajouter une dépendance

```bash
# 1. Activer venv
source venv/bin/activate

# 2. Installer
pip install nouvelle-lib

# 3. Freezer les deps
pip freeze > scripts/chat-atomizer/requirements.txt

# 4. Commit
git add scripts/chat-atomizer/requirements.txt
git commit -m "deps: add nouvelle-lib"
```

### Mettre à jour une dépendance

```bash
# Activer venv
source venv/bin/activate

# Mettre à jour
pip install --upgrade PyYAML

# Freezer
pip freeze > scripts/chat-atomizer/requirements.txt

# Commit
git add scripts/chat-atomizer/requirements.txt
git commit -m "deps: upgrade PyYAML to X.X.X"
```

### Synchroniser sur une nouvelle machine

```bash
# 1. Clone le repo
git clone <url>
cd pkm-system

# 2. Créer venv
python3 -m venv venv

# 3. Activer
source venv/bin/activate

# 4. Installer deps
pip install -r scripts/chat-atomizer/requirements.txt

# ✅ Prêt !
```

---

## 🚀 Scripts Helpers

### activate-venv.sh

```bash
# Utilisation
source activate-venv.sh

# Fait automatiquement :
# - Vérifie si venv existe
# - Crée venv si besoin
# - Active le venv
# - Installe les deps si besoin
```

### Ajouter un alias (optionnel)

```bash
# Dans ton ~/.bashrc ou ~/.zshrc
echo 'alias pkm-venv="cd /mnt/c/Users/idsmf/Projects/pkm-system && source venv/bin/activate"' >> ~/.bashrc

# Recharger
source ~/.bashrc

# Maintenant tu peux juste taper :
pkm-venv
# → Active directement le venv du projet !
```

---

## 🧪 Tester que tout marche

```bash
# 1. Activer venv
source venv/bin/activate

# 2. Vérifier Python
which python
# → /path/to/pkm-system/venv/bin/python ✅

# 3. Vérifier PyYAML
python -c "import yaml; print(yaml.__version__)"
# → 6.0 (ou +) ✅

# 4. Tester le script
python scripts/chat-atomizer/test_atomizer.py --help
# → Usage: ... ✅

# 5. Désactiver
deactivate
```

---

## 📁 Structure Finale

```
pkm-system/
├── venv/                           # ← Ignoré par git
│   ├── bin/
│   ├── lib/
│   └── ...
│
├── scripts/
│   └── chat-atomizer/
│       ├── atomize_chat.py
│       ├── test_atomizer.py
│       ├── requirements.txt        # ← Versionné
│       └── README.md
│
├── activate-venv.sh                # ← Helper script
├── .gitignore                      # ← venv/ dedans
└── README.md
```

---

## ❓ FAQ

### Pourquoi venv et pas juste pip global ?

**Problèmes avec pip global :**
- 💥 Conflits entre projets
- 💥 Pollution du Python système
- 💥 Difficile à reproduire
- 💥 Pas isolé

**Avantages venv :**
- ✅ Isolation complète
- ✅ Reproductible (requirements.txt)
- ✅ Pas de pollution système
- ✅ Peut avoir plusieurs versions d'une lib

### Le venv prend beaucoup de place ?

```bash
# Vérifier taille
du -sh venv/
# → ~10-50 MB (juste PyYAML)

# Acceptable pour un projet
```

### Puis-je supprimer venv/ ?

**OUI**, tu peux toujours le recréer :

```bash
rm -rf venv/
python3 -m venv venv
source venv/bin/activate
pip install -r scripts/chat-atomizer/requirements.txt
```

### Windows (non-WSL) ?

```bash
# Créer venv
python -m venv venv

# Activer
venv\Scripts\activate

# Désactiver
deactivate
```

---

## ✅ Checklist Setup

- [ ] Python 3.8+ installé
- [ ] pip installé
- [ ] venv/ créé
- [ ] venv activable avec `source venv/bin/activate`
- [ ] PyYAML installé dans venv
- [ ] venv/ dans .gitignore
- [ ] requirements.txt à jour
- [ ] Test script fonctionne
- [ ] Helper script créé (optionnel)
- [ ] Alias créé (optionnel)

---

**Setup time:** ~5 minutes  
**Benefit:** Projet Python professionnel, reproductible, isolé ✅
