#!/usr/bin/env python3
"""
Taxonomy Validation - Check Data Integrity
===========================================

Vérifie que toutes les catégories existent dans taxonomy.
"""

import duckdb
from pathlib import Path

def validate():
    """Valide données vs taxonomy."""
    print("="*70)
    print("✅ TAXONOMY VALIDATION")
    print("="*70)
    
    conn = duckdb.connect('finance-system/data/finance.duckdb')
    
    # Check if taxonomy table exists
    tables = [t[0] for t in conn.execute("SHOW TABLES").fetchall()]
    
    if 'category_taxonomy' not in tables:
        print("\n❌ Taxonomy table not found!")
        print("   Run: python3 scripts/taxonomy_sync.py")
        return
    
    print("\n✅ Taxonomy table exists")
    
    # Check orphan main categories
    print("\n🔍 Checking main categories...")
    
    orphans = conn.execute("""
    SELECT DISTINCT a.category_main, COUNT(*) as count
    FROM articles_detail a
    LEFT JOIN category_taxonomy t 
        ON a.category_main = t.display_name AND t.level = 1
    WHERE a.category_main IS NOT NULL
        AND t.category_key IS NULL
    GROUP BY a.category_main
    """).fetchall()
    
    if orphans:
        print(f"\n⚠️  {len(orphans)} orphan main categories:")
        for cat, count in orphans:
            print(f"  ❌ {cat} ({count} articles)")
    else:
        print("  ✅ All main categories valid")
    
    # Check orphan subcategories
    print("\n🔍 Checking subcategories...")
    
    orphans_sub = conn.execute("""
    SELECT DISTINCT a.category_sub, COUNT(*) as count
    FROM articles_detail a
    LEFT JOIN category_taxonomy t 
        ON a.category_sub = t.display_name AND t.level = 2
    WHERE a.category_sub IS NOT NULL
        AND t.subcategory_key IS NULL
    GROUP BY a.category_sub
    """).fetchall()
    
    if orphans_sub:
        print(f"\n⚠️  {len(orphans_sub)} orphan subcategories:")
        for cat, count in orphans_sub:
            print(f"  ❌ {cat} ({count} articles)")
    else:
        print("  ✅ All subcategories valid")
    
    # Summary
    print("\n" + "="*70)
    print("📊 SUMMARY")
    print("="*70)
    
    total = conn.execute("SELECT COUNT(*) FROM articles_detail").fetchone()[0]
    valid_main = conn.execute("""
    SELECT COUNT(*) FROM articles_detail a
    JOIN category_taxonomy t ON a.category_main = t.display_name AND t.level = 1
    """).fetchone()[0]
    
    print(f"\nTotal articles: {total}")
    print(f"Valid main categories: {valid_main} ({valid_main/total*100:.1f}%)")
    
    if orphans or orphans_sub:
        print("\n⚠️  Action required:")
        print("  1. Add missing categories to categories.yaml")
        print("  2. OR add migration rules in migration_rules.yaml")
        print("  3. Run sync then migrate")
    else:
        print("\n✅ ALL CATEGORIES VALID")
    
    conn.close()

if __name__ == '__main__':
    validate()
