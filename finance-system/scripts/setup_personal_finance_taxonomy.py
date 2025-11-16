#!/usr/bin/env python3
"""Setup Personal Finance Detailed Taxonomy"""
import duckdb
import yaml
from pathlib import Path

def setup():
    # Load
    with open('finance-system/taxonomy/personal_finance_detailed.yaml') as f:
        tax = yaml.safe_load(f)
    
    conn = duckdb.connect('finance-system/data/finance.duckdb')
    
    cat_id = 2000
    
    for cat_key, cat_data in tax['categories'].items():
        # Level 1
        conn.execute("""
        INSERT OR IGNORE INTO taxonomy_categories
        (category_id, taxonomy_id, category_key, display_name, level, path, icon, color)
        VALUES (?, 2, ?, ?, 1, ?, ?, ?)
        """, [cat_id, cat_key, cat_data['display_name'], 
              f"finance_detailed/{cat_key}",
              cat_data.get('icon', ''), cat_data.get('color', '')])
        
        parent_id = cat_id
        cat_id += 1
        
        # Level 2
        for sub_key, sub_data in cat_data.get('subcategories', {}).items():
            conn.execute("""
            INSERT OR IGNORE INTO taxonomy_categories
            (category_id, taxonomy_id, category_key, parent_id, display_name, level, path)
            VALUES (?, 2, ?, ?, ?, 2, ?)
            """, [cat_id, sub_key, parent_id, sub_data['display'], 
                  f"finance_detailed/{cat_key}/{sub_key}"])
            
            sub_parent = cat_id
            cat_id += 1
            
            # Level 3
            for cat3_key, cat3_data in sub_data.get('categories', {}).items():
                conn.execute("""
                INSERT OR IGNORE INTO taxonomy_categories
                (category_id, taxonomy_id, category_key, parent_id, display_name, level, path)
                VALUES (?, 2, ?, ?, ?, 3, ?)
                """, [cat_id, cat3_key, sub_parent, cat3_data['display'],
                      f"finance_detailed/{cat_key}/{sub_key}/{cat3_key}"])
                cat_id += 1
    
    print(f"✅ {cat_id - 2000} catégories créées")
    conn.close()

if __name__ == '__main__':
    setup()
