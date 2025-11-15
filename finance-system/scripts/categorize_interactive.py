#!/usr/bin/env python3
"""
Interactive Categorization Tool - v1.1
===================================
Fixed: Use transaction_id instead of id
"""

import duckdb
from pathlib import Path
import sys

# Taxonomy catégories
CATEGORIES = {
    '1': {'main': 'Alimentation', 'subs': [
        'Frais > Fromage',
        'Frais > Viande', 
        'Frais > Poisson',
        'Frais > Fruits & Légumes',
        'Épicerie > Conserves',
        'Épicerie > Pâtes & Riz',
        'Boissons > Alcool',
        'Boissons > Non-alcoolisé',
        'Restauration > Fast-food',
        'Surgelés',
    ]},
    '2': {'main': 'Transport', 'subs': [
        'Carburant > Diesel',
        'Carburant > Essence',
        'Entretien',
        'Parking',
    ]},
    '3': {'main': 'Loisirs', 'subs': [
        'Gaming > Consoles',
        'Gaming > Jeux',
        'Sorties > Cinéma',
        'Sorties > Concert',
        'Culture > Livres',
    ]},
    '4': {'main': 'Logement', 'subs': [
        'Loyer',
        'Électricité',
        'Eau',
        'Internet',
    ]},
    '5': {'main': 'Habillement', 'subs': ['Vêtements', 'Chaussures']},
    '6': {'main': 'Santé', 'subs': ['Médicaments', 'Médecin']},
    '7': {'main': 'Autres', 'subs': ['Divers']},
}

def suggest_category(article, merchant):
    """Suggère catégorie basée sur article/merchant."""
    article_lower = article.lower()
    merchant_lower = merchant.lower()
    
    # Gaming
    if 'switch' in article_lower or 'mario' in article_lower or 'console' in article_lower or 'jeux' in article_lower or 'jeu' in article_lower:
        if 'console' in article_lower or 'switch' in article_lower:
            return ('3', 'Gaming > Consoles')
        else:
            return ('3', 'Gaming > Jeux')
    
    # Carburant
    if 'diesel' in article_lower or 'essence' in article_lower:
        return ('2', 'Carburant > Diesel' if 'diesel' in article_lower else 'Carburant > Essence')
    
    # Fast-food
    if 'mcdonald' in merchant_lower:
        return ('1', 'Restauration > Fast-food')
    
    # Alimentation par défaut si Leclerc/Carrefour/Action
    if any(m in merchant_lower for m in ['leclerc', 'carrefour', 'action']):
        # Fromage
        if any(k in article_lower for k in ['raclette', 'emmental', 'fromage', 'chevre', 'gruyere']):
            return ('1', 'Frais > Fromage')
        # Viande
        if any(k in article_lower for k in ['viande', 'poulet', 'boeuf', 'porc', 'cordon', 'jambon', 'saucisse']):
            return ('1', 'Frais > Viande')
        # Poisson
        if any(k in article_lower for k in ['poisson', 'saumon', 'thon', 'truite']):
            return ('1', 'Frais > Poisson')
        # Fruits & Légumes
        if any(k in article_lower for k in ['pomme', 'banane', 'tomate', 'salade', 'fruit', 'legume', 'carotte']):
            return ('1', 'Frais > Fruits & Légumes')
        # Boissons
        if any(k in article_lower for k in ['coca', 'eau', 'jus', 'biere', 'vin', 'boisson']):
            if any(k in article_lower for k in ['biere', 'vin', 'alcool']):
                return ('1', 'Boissons > Alcool')
            return ('1', 'Boissons > Non-alcoolisé')
        # Surgelés
        if 'surgel' in article_lower or 'glace' in article_lower:
            return ('1', 'Surgelés')
        # Pâtes & Riz
        if any(k in article_lower for k in ['pate', 'riz', 'farine', 'cereale']):
            return ('1', 'Épicerie > Pâtes & Riz')
        # Épicerie par défaut
        return ('1', 'Épicerie > Conserves')
    
    # Cash
    if 'billet' in article_lower:
        return ('7', 'Autres > Divers')
    
    return None

def display_categories():
    """Affiche menu catégories."""
    print("\n" + "="*70)
    print("CATÉGORIES DISPONIBLES")
    print("="*70)
    for key, cat in CATEGORIES.items():
        print(f"{key}. {cat['main']}")
    print("="*70)

def display_subcategories(cat_key):
    """Affiche sous-catégories."""
    subs = CATEGORIES[cat_key]['subs']
    print(f"\nSous-catégories {CATEGORIES[cat_key]['main']}:")
    for i, sub in enumerate(subs, 1):
        print(f"  {i}. {sub}")
    return subs

def categorize_article(article_row):
    """Catégorise un article interactivement."""
    transaction_id = article_row[0]
    article = article_row[1]
    merchant = article_row[2]
    amount = article_row[3]
    
    print("\n" + "━"*70)
    print(f"📦 Transaction #{transaction_id}")
    print("━"*70)
    print(f"Nom: {article}")
    print(f"Enseigne: {merchant}")
    print(f"Prix: {amount:.2f}€")
    
    # Suggestion
    suggestion = suggest_category(article, merchant)
    if suggestion:
        cat_key, sub_suggested = suggestion
        print(f"\n💡 Suggestion: {CATEGORIES[cat_key]['main']} > {sub_suggested}")
        print(f"   Appuie sur Enter pour accepter, ou tape autre chose...")
    
    # Choix catégorie principale
    display_categories()
    
    if suggestion:
        choice = input(f"\nCatégorie principale [{cat_key}]: ").strip()
        if not choice:
            choice = cat_key
    else:
        choice = input("\nCatégorie principale (1-7): ").strip()
    
    if choice not in CATEGORIES:
        print("⚠️  Choix invalide, défaut = 7 (Autres)")
        choice = '7'
    
    cat_main = CATEGORIES[choice]['main']
    
    # Choix sous-catégorie
    subs = display_subcategories(choice)
    
    if suggestion and choice == cat_key:
        # Trouver index de la suggestion
        try:
            sub_idx = subs.index(sub_suggested) + 1
            sub_choice = input(f"\nSous-catégorie [{sub_idx}]: ").strip()
            if not sub_choice:
                sub_choice = str(sub_idx)
        except:
            sub_choice = input(f"\nSous-catégorie (1-{len(subs)}): ").strip()
    else:
        sub_choice = input(f"\nSous-catégorie (1-{len(subs)}): ").strip()
    
    try:
        sub_idx = int(sub_choice) - 1
        cat_sub = subs[sub_idx]
    except:
        cat_sub = subs[0]
    
    # Tags
    tags_input = input("\nTags (comma-separated, optionnel): ").strip()
    tags = [t.strip() for t in tags_input.split(',')] if tags_input else []
    
    return {
        'transaction_id': transaction_id,
        'category_main': cat_main,
        'category_sub': cat_sub,
        'tags': tags
    }

def main():
    print("="*70)
    print("🏷️  INTERACTIVE CATEGORIZATION TOOL v1.1")
    print("="*70)
    
    db_path = Path("finance-system/data/finance.duckdb")
    if not db_path.exists():
        print(f"❌ Database not found: {db_path}")
        return 1
    
    conn = duckdb.connect(str(db_path))
    
    # Vérifier colonnes
    try:
        conn.execute("ALTER TABLE articles_detail ADD COLUMN category_main TEXT")
        conn.execute("ALTER TABLE articles_detail ADD COLUMN category_sub TEXT")
        conn.execute("ALTER TABLE articles_detail ADD COLUMN tags TEXT")
        print("✅ Colonnes catégories ajoutées\n")
    except:
        print("✅ Colonnes catégories déjà présentes\n")
    
    # Charger articles non catégorisés
    articles = conn.execute("""
    SELECT transaction_id, article, merchant, prix_total
    FROM articles_detail
    WHERE category_main IS NULL
    ORDER BY prix_total DESC
    """).fetchall()
    
    total = len(articles)
    print(f"📊 {total} articles à catégoriser\n")
    
    if total == 0:
        print("✅ Tous les articles sont déjà catégorisés!")
        return 0
    
    print("💡 Tips:")
    print("  - Les suggestions auto s'affichent si détectées")
    print("  - Appuie Enter pour accepter suggestion")
    print("  - Ctrl+C pour arrêter (progression sauvegardée)")
    
    input("\nAppuie Enter pour commencer...")
    
    categorized = 0
    
    try:
        for i, article_row in enumerate(articles, 1):
            print(f"\n{'='*70}")
            print(f"Progress: {i}/{total} ({i/total*100:.1f}%)")
            
            result = categorize_article(article_row)
            
            # Update DB
            tags_str = ','.join(result['tags']) if result['tags'] else ''
            conn.execute("""
            UPDATE articles_detail
            SET category_main = ?,
                category_sub = ?,
                tags = ?
            WHERE transaction_id = ?
            """, [result['category_main'], result['category_sub'], tags_str, result['transaction_id']])
            
            categorized += 1
            print(f"\n✅ Sauvegardé: {result['category_main']} > {result['category_sub']}")
            
    except KeyboardInterrupt:
        print(f"\n\n⚠️  Interrupted! {categorized}/{total} articles sauvegardés.")
    
    conn.close()
    
    print(f"\n{'='*70}")
    print(f"✅ TERMINÉ: {categorized} articles catégorisés")
    print(f"{'='*70}")
    
    return 0

if __name__ == '__main__':
    exit(main())
