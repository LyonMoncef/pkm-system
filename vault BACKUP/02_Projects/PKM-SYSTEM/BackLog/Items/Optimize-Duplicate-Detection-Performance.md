---
created: 2025-11-10T18:30:00+01:00
updated: 2025-11-10T18:30:00+01:00
type: backlog-item
tags: [backlog-item, optimization, performance, python, duplicate-detection]
status: todo
priority: medium
estimated_time: "3-4h"
category: improvement
project: pkm-system
phase: phase-2
related_to: 
  - "[[chat_to_cards]]"
  - "[[postprocess_cards]]"
  - "[[DuplicateDetector]]"
---

# 🚀 Optimize Duplicate Detection Performance

> **Améliorer les performances de la détection de doublons pour supporter des sessions de 2000+ cartes**

---

## 📋 Description

La détection de doublons devient extrêmement lente sur les grandes conversations (1000+ cartes).

### Problème Actuel

**Algorithme O(n²) :**
- Compare chaque carte avec toutes les autres
- 1049 cartes = 549,876 comparaisons
- 1887 cartes = 1,779,141 comparaisons
- **Freeze/timeout** sur grosses sessions

**Impact :**
- Batch processing bloqué
- Timeout sur conversations volumineuses
- Expérience utilisateur dégradée

### Contexte Découverte

Identifié lors du batch processing de 35 conversations historiques :
- Sessions < 200 cartes : rapide ✅
- Sessions 500-1000 : lent mais passe ⚠️
- Sessions 1000+ : freeze total 🔴

**Conversations problématiques :**
- "French chat message instructions" : 1049 cartes
- "Ticket receipt data extraction (Power BI)" : 1887 cartes

---

## 🎯 Objectif

Optimiser la détection de doublons pour :
- ✅ Supporter 2000+ cartes sans timeout
- ✅ Temps de traitement < 30s pour 2000 cartes
- ✅ Pas de régression de précision
- ✅ Code maintenable et testé

---

## 🔧 Solutions Possibles

### Option 1 : Hashing + Grouping (Recommandé)

**Principe :**
```python
# Pre-grouper par hash du contenu
groups = {}
for card in cards:
    hash_key = hash(card.content[:200])  # Hash premiers chars
    groups[hash_key].append(card)

# Comparer uniquement dans chaque groupe
for group in groups.values():
    compare_within_group(group)
```

**Avantages :**
- Complexité O(n log n)
- Réduction massive des comparaisons
- Précision conservée

**Inconvénients :**
- Code plus complexe
- Besoin de tuner la fonction de hash

---

### Option 2 : Sampling Intelligent

**Principe :**
```python
# Échantillonner stratégiquement
if len(cards) > 500:
    sample = strategic_sample(cards, max_size=500)
    duplicates = detect_in_sample(sample)
```

**Avantages :**
- Très rapide
- Simple à implémenter

**Inconvénients :**
- Perte de précision
- Peut manquer des doublons

---

### Option 3 : Incremental Detection

**Principe :**
```python
# Cache des comparaisons déjà faites
cache = load_comparison_cache()

# Comparer uniquement nouvelles vs existantes
for new_card in new_cards:
    for existing_card in existing_cards:
        if (new_card.id, existing_card.id) not in cache:
            similarity = compare(new_card, existing_card)
            cache[(new_card.id, existing_card.id)] = similarity
```

**Avantages :**
- Évite recomputation
- Parfait pour ajouts incrémentaux

**Inconvénients :**
- Gestion du cache complexe
- Peu adapté au batch

---

### Option 4 : Multiprocessing

**Principe :**
```python
# Paralléliser les comparaisons
with Pool(cpu_count()) as pool:
    results = pool.starmap(compare_pair, card_pairs)
```

**Avantages :**
- Speedup linéaire avec cores
- Pas de changement d'algorithme

**Inconvénients :**
- Overhead création processes
- Complexité multiprocessing

---

## 📦 Plan d'Implémentation

### Phase 1 : Profiling (30min-1h)

**Objectifs :**
- [ ] Identifier bottlenecks exacts
- [ ] Mesurer temps par étape
- [ ] Établir baseline performance

**Actions :**
```bash
# Profiler avec cProfile
python -m cProfile -o profile.stats scripts/chat-atomizer/chat_to_cards.py ...

# Analyser résultats
python -m pstats profile.stats
```

**Livrables :**
- Rapport de profiling
- Identification goulots
- Métriques baseline

---

### Phase 2 : Implémentation Hashing (1-2h)

**Objectifs :**
- [ ] Implémenter grouping par hash
- [ ] Adapter DuplicateDetector
- [ ] Tests unitaires

**Code skeleton :**
```python
class OptimizedDuplicateDetector:
    @staticmethod
    def hash_content(content: str, length: int = 200) -> int:
        """Hash les premiers chars du contenu."""
        return hash(content[:length])
    
    @staticmethod
    def group_by_hash(cards: List[Card]) -> Dict[int, List[Card]]:
        """Groupe les cartes par hash."""
        groups = {}
        for card in cards:
            h = OptimizedDuplicateDetector.hash_content(card.content)
            groups.setdefault(h, []).append(card)
        return groups
    
    @staticmethod
    def find_duplicates_optimized(
        cards: List[Card], 
        threshold: float = 0.85
    ) -> List[Tuple[Card, Card, float]]:
        """Détection optimisée O(n log n)."""
        groups = OptimizedDuplicateDetector.group_by_hash(cards)
        duplicates = []
        
        for group_cards in groups.values():
            # Comparer uniquement dans le groupe
            duplicates.extend(
                compare_within_group(group_cards, threshold)
            )
        
        return duplicates
```

**Tests :**
```python
def test_optimized_detector_performance():
    # Générer 2000 cartes
    cards = generate_test_cards(2000)
    
    # Mesurer temps
    start = time.time()
    duplicates = OptimizedDuplicateDetector.find_duplicates_optimized(cards)
    duration = time.time() - start
    
    assert duration < 30, f"Too slow: {duration}s"
    assert len(duplicates) >= 0  # Au moins ne crash pas
```

---

### Phase 3 : Benchmarks (30min)

**Objectifs :**
- [ ] Comparer performances avant/après
- [ ] Vérifier précision conservée
- [ ] Documenter gains

**Métriques :**
| Cards | Before | After | Speedup |
|-------|--------|-------|---------|
| 100   | 2s     | ?     | ?x      |
| 500   | 30s    | ?     | ?x      |
| 1000  | 180s   | ?     | ?x      |
| 2000  | timeout| ?     | ?x      |

---

## 🧪 Critères d'Acceptation

### Performance

- [ ] 2000 cartes : < 30s
- [ ] 1000 cartes : < 10s
- [ ] 500 cartes : < 3s

### Qualité

- [ ] Précision détection conservée (>95%)
- [ ] Tests unitaires passent
- [ ] Code documenté
- [ ] Pas de régression sur petites sessions

### Documentation

- [ ] README updated
- [ ] Benchmarks documentés
- [ ] Guide utilisation

---

## 🔗 Références

**Code actuel :**
- `scripts/chat-atomizer/postprocess_cards.py` → `DuplicateDetector`
- `scripts/chat-atomizer/chat_to_cards.py` → Step 2: Duplicate Detection

**Conversations liées :**
- [[Session 2025-11-10 - Chat Atomization Batch]]
- Batch processing 35 conversations

**Ressources techniques :**
- Algorithme similarité actuel : difflib.SequenceMatcher
- Alternative possible : rapidfuzz (plus rapide)

---

## 💡 Notes

### Workaround Actuel

Pour le batch processing, les steps 2-5 ont été commentés :
```python
# Steps 2-5 désactivés temporairement
# - Duplicate detection
# - Duplicate removal
# - Intelligent renaming
# - Link updates
```

Cela permet de finir le batch mais :
- ❌ Doublons non détectés
- ❌ Noms de cartes basiques
- ❌ Pas de cleanup

### Alternative : Script Post-Processing

Créer un script séparé qui :
1. Charge toutes les sessions générées
2. Détecte doublons cross-sessions (optionnel)
3. Nettoie/renomme en batch
4. Plus efficace qu'à la volée

---

## 📅 Timeline Estimée

**Total : 3-4h**

| Phase | Durée | Status |
|-------|-------|--------|
| Profiling | 30min-1h | ⬜ Todo |
| Implementation | 1-2h | ⬜ Todo |
| Testing | 30min | ⬜ Todo |
| Benchmarks | 30min | ⬜ Todo |
| Documentation | 30min | ⬜ Todo |

---

## ✅ Checklist Completion

### Développement

- [ ] Profiling réalisé
- [ ] Hashing implémenté
- [ ] Grouping implémenté
- [ ] Tests unitaires ajoutés
- [ ] Benchmarks réalisés

### Quality Assurance

- [ ] Performance targets atteints
- [ ] Précision vérifiée
- [ ] Pas de régression
- [ ] Code review fait

### Documentation

- [ ] README updated
- [ ] Code commenté
- [ ] Benchmarks documentés
- [ ] Backlog item closed

---

**Créé pendant :** [[Session 2025-11-10 - Chat Atomization Batch]]  
**Phase projet :** Phase 2 - Features & Optimization  
**Assigné à :** À définir  
**Bloquant :** Non (workaround actif)
