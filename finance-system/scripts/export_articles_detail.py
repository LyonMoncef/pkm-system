#!/usr/bin/env python3
"""
Export Article Details from DuckDB - v1
======================================

Extrait le détail des articles depuis raw_data JSON.
"""

import duckdb
import pandas as pd
import json
from pathlib import Path


def extract_articles_from_transaction(row):
    """Extrait les articles d'une transaction."""
    articles = []
    
    try:
        raw_data = json.loads(row['raw_data'])
        
        # Si données CSV simple (pas d'articles détaillés)
        if 'article' in raw_data:
            articles.append({
                'transaction_id': row['id'],
                'date': row['date'],
                'merchant': row['merchant'],
                'magasin': row['magasin'],
                'article': raw_data.get('article', 'N/A'),
                'quantite': raw_data.get('quantite', 1),
                'prix_unitaire': raw_data.get('prix_unitaire', row['amount']),
                'prix_total': row['amount']
            })
        
        # Si JSON avec array articles
        elif 'articles' in raw_data:
            for art in raw_data['articles']:
                articles.append({
                    'transaction_id': row['id'],
                    'date': row['date'],
                    'merchant': row['merchant'],
                    'magasin': row['magasin'],
                    'article': art.get('description', art.get('article', 'N/A')),
                    'quantite': art.get('quantite', art.get('quantite_litres', 1)),
                    'prix_unitaire': art.get('prix_unitaire', 0),
                    'prix_total': art.get('prix_total', 0)
                })
        
        # Fallback : ligne simple
        else:
            articles.append({
                'transaction_id': row['id'],
                'date': row['date'],
                'merchant': row['merchant'],
                'magasin': row['magasin'],
                'article': 'Transaction globale',
                'quantite': row['articles_count'],
                'prix_unitaire': row['amount'] / max(row['articles_count'], 1),
                'prix_total': row['amount']
            })
    
    except Exception as e:
        # Erreur parsing : créer ligne générique
        articles.append({
            'transaction_id': row['id'],
            'date': row['date'],
            'merchant': row['merchant'],
            'magasin': row['magasin'],
            'article': f'Error: {str(e)[:50]}',
            'quantite': 1,
            'prix_unitaire': row['amount'],
            'prix_total': row['amount']
        })
    
    return articles


def main():
    print("=" * 70)
    print("🛒 EXPORT ARTICLE DETAILS - v1")
    print("=" * 70)
    print()
    
    db_path = Path("finance-system/data/finance.duckdb")
    export_dir = Path("finance-system/exports/powerbi")
    
    if not db_path.exists():
        print(f"❌ Database not found: {db_path}")
        return 1
    
    print(f"📂 Database: {db_path}")
    print(f"📂 Export to: {export_dir}\n")
    
    # Charger transactions
    conn = duckdb.connect(str(db_path))
    df_trans = conn.execute("""
    SELECT id, date, merchant, magasin, amount, articles_count, raw_data
    FROM transactions
    ORDER BY date, merchant
    """).df()
    conn.close()
    
    print(f"📋 Processing {len(df_trans)} transactions...")
    
    # Extraire articles
    all_articles = []
    for idx, row in df_trans.iterrows():
        articles = extract_articles_from_transaction(row)
        all_articles.extend(articles)
        
        if (idx + 1) % 20 == 0:
            print(f"  Processed {idx + 1}/{len(df_trans)} transactions...")
    
    print(f"\n✅ Extracted {len(all_articles)} article lines")
    
    # Créer DataFrame
    df_articles = pd.DataFrame(all_articles)
    
    # Sauvegarder
    articles_path = export_dir / "articles_detail.xlsx"
    df_articles.to_excel(articles_path, index=False, engine='openpyxl')
    print(f"\n💾 Saved: {articles_path}")
    
    # Stats
    print("\n📊 Article Stats:")
    print(f"  Total articles: {len(df_articles)}")
    print(f"  Unique articles: {df_articles['article'].nunique()}")
    print(f"  Total value: {df_articles['prix_total'].sum():.2f}€")
    
    print("\n  Top 10 articles:")
    top_articles = df_articles.groupby('article').agg({
        'quantite': 'sum',
        'prix_total': 'sum'
    }).sort_values('prix_total', ascending=False).head(10)
    
    for article, row in top_articles.iterrows():
        print(f"    - {article}: {row['prix_total']:.2f}€ (qty: {row['quantite']})")
    
    print("\n🎯 Next: Import articles_detail.xlsx in Power BI")
    
    return 0


if __name__ == '__main__':
    exit(main())
