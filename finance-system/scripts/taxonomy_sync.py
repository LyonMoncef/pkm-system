#!/usr/bin/env python3
"""
Taxonomy Sync - YAML to Database
=================================

Synchronise categories.yaml vers DuckDB.
Crée table de référence taxonomy.
"""

import yaml
import duckdb
from pathlib import Path
import sys

def load_taxonomy():
    """Charge taxonomy depuis YAML."""
    yaml_path = Path("finance-system/taxonomy/categories.yaml")
    
    if not yaml_path.exists():
        print(f"❌ Fichier not found: {yaml_path}")
        sys.exit(1)
    
    with open(yaml_path) as f:
        return yaml.safe_load(f)

def sync_to_db():
    """Synchronise YAML → DB."""
    print("="*70)
    print("🔄 TAXONOMY SYNC - YAML → DATABASE")
    print("="*70)
    
    # Load taxonomy
    print("\n📂 Loading taxonomy...")
    taxonomy = load_taxonomy()
    print(f"  Version: {taxonomy['version']}")
    print(f"  Last updated: {taxonomy['last_updated']}")
    
    # Connect DB
    db_path = Path("finance-system/data/finance.duckdb")
    conn = duckdb.connect(str(db_path))
    
    # Backup first
    print("\n💾 Creating backup...")
    conn.execute("EXPORT DATABASE 'finance-system/data/backup_taxonomy_sync'")
    print("  ✅ Backup created")
    
    # Drop existing taxonomy table
    print("\n🗑️  Dropping old taxonomy table...")
    conn.execute("DROP TABLE IF EXISTS category_taxonomy")
    
    # Create taxonomy table
    print("\n🏗️  Creating taxonomy table...")
    conn.execute("""
    CREATE TABLE category_taxonomy (
        category_key TEXT,
        subcategory_key TEXT,
        level INTEGER,
        display_name TEXT,
        full_display TEXT,
        icon TEXT,
        description TEXT,
        color TEXT,
        ordre INTEGER,
        keywords TEXT,
        PRIMARY KEY (category_key, subcategory_key)
    )
    """)
    
    # Insert from YAML
    print("\n📝 Inserting categories...")
    
    total_cats = 0
    total_subs = 0
    
    for cat_key, cat_data in taxonomy['categories'].items():
        # Insert main category
        conn.execute("""
        INSERT INTO category_taxonomy VALUES (?, '', 1, ?, ?, ?, ?, ?, ?, '')
        """, [
            cat_key,
            cat_data['display_name'],
            cat_data['display_name'],
            cat_data.get('icon', ''),
            cat_data.get('description', ''),
            cat_data.get('color', ''),
            cat_data.get('ordre', 99)
        ])
        
        total_cats += 1
        print(f"  ✅ {cat_data['display_name']}")
        
        # Insert subcategories
        for subcat_key, subcat_data in cat_data.get('subcategories', {}).items():
            keywords_str = ','.join(subcat_data.get('keywords', []))
            full_display = f"{cat_data['display_name']} > {subcat_data['display']}"
            
            conn.execute("""
            INSERT INTO category_taxonomy VALUES (?, ?, 2, ?, ?, '', '', '', 0, ?)
            """, [
                cat_key,
                subcat_key,
                subcat_data['display'],
                full_display,
                keywords_str
            ])
            
            total_subs += 1
            print(f"     ├─ {subcat_data['display']}")
    
    # Stats
    print("\n" + "="*70)
    print("📊 SYNC STATS")
    print("="*70)
    print(f"  Main categories: {total_cats}")
    print(f"  Subcategories: {total_subs}")
    print(f"  Total entries: {total_cats + total_subs}")
    
    # Verify
    count = conn.execute("SELECT COUNT(*) FROM category_taxonomy").fetchone()[0]
    print(f"\n✅ Database verified: {count} entries")
    
    conn.close()
    
    print("\n" + "="*70)
    print("✅ SYNC COMPLETE")
    print("="*70)
    print("\nNext steps:")
    print("  1. Run migration: python3 scripts/taxonomy_migrate.py")
    print("  2. Export Power BI: python3 scripts/export_with_categories.py")

if __name__ == '__main__':
    sync_to_db()
