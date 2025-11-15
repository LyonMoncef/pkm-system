#!/usr/bin/env python3
"""
Taxonomy Report - Complete Overview
====================================

Génère rapport complet taxonomy + usage.
"""

import duckdb
from pathlib import Path

def generate_report():
    """Génère rapport."""
    print("="*70)
    print("📊 TAXONOMY REPORT")
    print("="*70)
    
    conn = duckdb.connect('finance-system/data/finance.duckdb')
    
    # Main categories with usage
    print("\n🏷️  MAIN CATEGORIES\n")
    
    results = conn.execute("""
    SELECT 
        t.category_key,
        t.display_name,
        t.icon,
        COUNT(a.id) as article_count,
        COALESCE(SUM(a.prix_total), 0) as total_euros,
        ROUND(COALESCE(SUM(a.prix_total), 0) / 
            (SELECT SUM(prix_total) FROM articles_detail) * 100, 1) as pct
    FROM category_taxonomy t
    LEFT JOIN articles_detail a ON t.display_name = a.category_main
    WHERE t.level = 1
    GROUP BY t.category_key, t.display_name, t.icon, t.ordre
    ORDER BY t.ordre
    """).fetchall()
    
    for key, name, icon, count, total, pct in results:
        print(f"{icon} {name:20} | {count:3} articles | {total:8.2f}€ | {pct:5.1f}%")
    
    # Subcategories by main
    print("\n" + "="*70)
    print("📁 SUBCATEGORIES USAGE")
    print("="*70)
    
    results = conn.execute("""
    SELECT 
        t.category_key,
        t.display_name as subcat_name,
        COUNT(a.id) as article_count,
        COALESCE(SUM(a.prix_total), 0) as total_euros
    FROM category_taxonomy t
    LEFT JOIN articles_detail a ON t.display_name = a.category_sub
    WHERE t.level = 2
    GROUP BY t.category_key, t.subcategory_key, t.display_name
    HAVING COUNT(a.id) > 0
    ORDER BY t.category_key, total_euros DESC
    """).fetchall()
    
    current_cat = None
    for cat_key, subcat, count, total in results:
        if cat_key != current_cat:
            # Get main cat name
            main_name = conn.execute("""
            SELECT display_name FROM category_taxonomy
            WHERE category_key = ? AND level = 1
            """, [cat_key]).fetchone()[0]
            
            print(f"\n{main_name}:")
            current_cat = cat_key
        
        print(f"  ├─ {subcat:40} | {count:3} | {total:7.2f}€")
    
    # Unused subcategories
    print("\n" + "="*70)
    print("🔍 UNUSED SUBCATEGORIES")
    print("="*70)
    
    unused = conn.execute("""
    SELECT 
        t.full_display,
        t.keywords
    FROM category_taxonomy t
    LEFT JOIN articles_detail a ON t.display_name = a.category_sub
    WHERE t.level = 2
    GROUP BY t.category_key, t.subcategory_key, t.full_display, t.keywords
    HAVING COUNT(a.id) = 0
    """).fetchall()
    
    if unused:
        print("\n⚠️  Subcategories without articles:")
        for full, keywords in unused:
            kw_str = f"[{keywords}]" if keywords else ""
            print(f"  - {full:50} {kw_str}")
    else:
        print("\n✅ All subcategories are used")
    
    conn.close()
    
    print("\n" + "="*70)

if __name__ == '__main__':
    generate_report()
