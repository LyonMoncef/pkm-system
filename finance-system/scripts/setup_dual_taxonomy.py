#!/usr/bin/env python3
"""
Setup Dual Taxonomy System - v1.1
==================================
Fixed: No foreign key constraints (manual integrity)
"""

import duckdb
from pathlib import Path
import yaml

def create_dual_taxonomy_tables():
    """Crée structure dual-taxonomy."""
    
    print("="*70)
    print("🏗️  DUAL TAXONOMY SETUP v1.1")
    print("="*70)
    
    db_path = Path("finance-system/data/finance.duckdb")
    conn = duckdb.connect(str(db_path))
    
    # Backup
    print("\n💾 Creating backup...")
    conn.execute("EXPORT DATABASE 'finance-system/data/backup_dual_taxonomy'")
    
    # Fix: Ensure articles_detail has primary key
    print("\n🔧 Ensuring articles_detail has primary key...")
    
    # Check current structure
    cols = conn.execute("DESCRIBE articles_detail").fetchall()
    col_names = [c[0] for c in cols]
    
    if 'id' not in col_names:
        print("  ❌ No 'id' column - adding...")
        # Create temp table with id
        conn.execute("""
        CREATE TABLE articles_detail_new AS
        SELECT ROW_NUMBER() OVER (ORDER BY transaction_id) as id, *
        FROM articles_detail
        """)
        conn.execute("DROP TABLE articles_detail")
        conn.execute("ALTER TABLE articles_detail_new RENAME TO articles_detail")
        print("  ✅ Added id column")
    else:
        print("  ✅ id column exists")
    
    # Table : Taxonomies
    print("\n📋 Creating taxonomies table...")
    conn.execute("""
    CREATE TABLE IF NOT EXISTS taxonomies (
        taxonomy_id INTEGER PRIMARY KEY,
        taxonomy_key TEXT UNIQUE,
        display_name TEXT,
        icon TEXT,
        description TEXT,
        is_active BOOLEAN DEFAULT true,
        is_default BOOLEAN DEFAULT false,
        source TEXT DEFAULT 'user',
        version TEXT,
        created_at TIMESTAMP DEFAULT NOW()
    )
    """)
    
    # Table : Taxonomy Categories (N-levels support)
    print("📁 Creating taxonomy_categories table...")
    conn.execute("""
    CREATE TABLE IF NOT EXISTS taxonomy_categories (
        category_id INTEGER PRIMARY KEY,
        taxonomy_id INTEGER,
        category_key TEXT,
        parent_id INTEGER,
        display_name TEXT,
        level INTEGER,
        path TEXT,
        description TEXT,
        metadata TEXT,
        icon TEXT,
        color TEXT,
        is_active BOOLEAN DEFAULT true,
        UNIQUE(taxonomy_id, category_key)
    )
    """)
    
    # Table : Article Classifications (many-to-many)
    # NO FOREIGN KEYS - manual integrity for now
    print("🔗 Creating article_classifications table...")
    conn.execute("""
    CREATE TABLE IF NOT EXISTS article_classifications (
        article_id INTEGER,
        category_id INTEGER,
        taxonomy_id INTEGER,
        confidence DECIMAL(3,2) DEFAULT 1.0,
        source TEXT DEFAULT 'manual',
        created_at TIMESTAMP DEFAULT NOW(),
        created_by TEXT DEFAULT 'user',
        notes TEXT,
        PRIMARY KEY (article_id, category_id)
    )
    """)
    
    # Insert taxonomy 1: Budget (migrate existing)
    print("\n💰 Creating taxonomy: Budget Personnel...")
    conn.execute("""
    INSERT OR IGNORE INTO taxonomies 
    (taxonomy_id, taxonomy_key, display_name, icon, description, is_default, source)
    VALUES 
    (1, 'budget', 'Budget Personnel', '💰', 
     'Classification comptable classique par catégories de dépenses', 
     true, 'system')
    """)
    
    # Insert taxonomy 2: EU Finance
    print("🇪🇺 Creating taxonomy: EU Finance Taxonomy...")
    conn.execute("""
    INSERT OR IGNORE INTO taxonomies 
    (taxonomy_id, taxonomy_key, display_name, icon, description, is_default, source, version)
    VALUES 
    (2, 'eu_finance', 'EU Finance Taxonomy', '🇪🇺', 
     'EU Taxonomy Regulation for sustainable activities', 
     false, 'standard', '2024')
    """)
    
    print("\n✅ Tables created successfully")
    
    # Migrate existing budget classifications
    print("\n🔄 Migrating existing budget classifications...")
    
    # Check if category_taxonomy exists
    tables = [t[0] for t in conn.execute("SHOW TABLES").fetchall()]
    
    if 'category_taxonomy' in tables:
        # Migrate from old taxonomy system
        print("  Found category_taxonomy - migrating...")
        
        # Insert categories from old system
        conn.execute("""
        INSERT OR IGNORE INTO taxonomy_categories
        (category_id, taxonomy_id, category_key, parent_id, display_name, level, path)
        SELECT 
            ROW_NUMBER() OVER (ORDER BY category_key) as category_id,
            1 as taxonomy_id,
            category_key,
            NULL as parent_id,
            display_name,
            level,
            category_key as path
        FROM category_taxonomy
        WHERE level = 1
        """)
        
        # Link articles to budget taxonomy
        conn.execute("""
        INSERT OR IGNORE INTO article_classifications
        (article_id, category_id, taxonomy_id, confidence, source)
        SELECT 
            a.id,
            tc.category_id,
            1,
            1.0,
            'migrated'
        FROM articles_detail a
        JOIN category_taxonomy ct ON a.category_main = ct.display_name
        JOIN taxonomy_categories tc ON ct.category_key = tc.category_key
        WHERE a.category_main IS NOT NULL
        """)
        
        migrated = conn.execute("""
        SELECT COUNT(*) FROM article_classifications WHERE taxonomy_id = 1
        """).fetchone()[0]
        
        print(f"  ✅ Migrated {migrated} article classifications")
    else:
        print("  ⚠️  No old taxonomy to migrate")
    
    # Stats
    tax_count = conn.execute("SELECT COUNT(*) FROM taxonomies").fetchone()[0]
    cat_count = conn.execute("SELECT COUNT(*) FROM taxonomy_categories").fetchone()[0]
    class_count = conn.execute("SELECT COUNT(*) FROM article_classifications").fetchone()[0]
    
    print(f"\n📊 Final stats:")
    print(f"  Taxonomies: {tax_count}")
    print(f"  Categories: {cat_count}")
    print(f"  Classifications: {class_count}")
    
    conn.close()
    
    print("\n" + "="*70)
    print("✅ DUAL TAXONOMY SETUP COMPLETE")
    print("="*70)
    print("\nNext: Run wizard to configure EU taxonomy")
    print("  python3 finance-system/scripts/taxonomy_setup_wizard.py")

if __name__ == '__main__':
    create_dual_taxonomy_tables()
