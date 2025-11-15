#!/usr/bin/env python3
"""
Taxonomy Migration - Apply Migration Rules
===========================================

Migre données existantes selon migration_rules.yaml
"""

import yaml
import duckdb
from pathlib import Path

def load_migration_rules():
    """Charge règles migration."""
    yaml_path = Path("finance-system/taxonomy/migration_rules.yaml")
    
    if not yaml_path.exists():
        print("⚠️  No migration rules found")
        return None
    
    with open(yaml_path) as f:
        return yaml.safe_load(f)

def migrate():
    """Applique migrations."""
    print("="*70)
    print("🔄 TAXONOMY MIGRATION")
    print("="*70)
    
    # Load rules
    print("\n📂 Loading migration rules...")
    rules = load_migration_rules()
    
    if not rules:
        print("  No rules to apply")
        return
    
    # Connect DB
    conn = duckdb.connect('finance-system/data/finance.duckdb')
    
    # Backup
    print("\n💾 Creating backup...")
    conn.execute("EXPORT DATABASE 'finance-system/data/backup_pre_migration'")
    
    # Apply main category mappings
    print("\n🔄 Migrating main categories...")
    
    for old_name, new_key in rules.get('category_main_mapping', {}).items():
        # Get display name from taxonomy
        display = conn.execute("""
        SELECT display_name FROM category_taxonomy
        WHERE category_key = ? AND level = 1
        """, [new_key]).fetchone()
        
        if display:
            display_name = display[0]
            
            count = conn.execute("""
            SELECT COUNT(*) FROM articles_detail WHERE category_main = ?
            """, [old_name]).fetchone()[0]
            
            if count > 0:
                conn.execute("""
                UPDATE articles_detail
                SET category_main = ?
                WHERE category_main = ?
                """, [display_name, old_name])
                
                print(f"  ✅ {old_name} → {display_name} ({count} articles)")
    
    # Apply subcategory mappings
    print("\n🔄 Migrating subcategories...")
    
    for old_name, new_key in rules.get('category_sub_mapping', {}).items():
        # Get display name
        display = conn.execute("""
        SELECT display_name FROM category_taxonomy
        WHERE subcategory_key = ? AND level = 2
        """, [new_key]).fetchone()
        
        if display:
            display_name = display[0]
            
            count = conn.execute("""
            SELECT COUNT(*) FROM articles_detail WHERE category_sub = ?
            """, [old_name]).fetchone()[0]
            
            if count > 0:
                conn.execute("""
                UPDATE articles_detail
                SET category_sub = ?
                WHERE category_sub = ?
                """, [display_name, old_name])
                
                print(f"  ✅ {old_name} → {display_name} ({count} articles)")
    
    # Verify
    print("\n" + "="*70)
    print("📊 POST-MIGRATION STATS")
    print("="*70)
    
    results = conn.execute("""
    SELECT category_main, COUNT(*) as count
    FROM articles_detail
    WHERE category_main IS NOT NULL
    GROUP BY category_main
    ORDER BY count DESC
    """).fetchall()
    
    for cat, count in results:
        print(f"  {cat:20} : {count:3} articles")
    
    conn.close()
    
    print("\n✅ MIGRATION COMPLETE")

if __name__ == '__main__':
    migrate()
