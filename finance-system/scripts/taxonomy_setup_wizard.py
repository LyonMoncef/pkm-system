#!/usr/bin/env python3
"""
Taxonomy Setup Wizard - v1.1
=============================
Fixed: YAML structure parsing
"""

import duckdb
import yaml
from pathlib import Path

def load_eu_taxonomy():
    """Charge EU taxonomy config."""
    with open('finance-system/taxonomy/eu_finance_taxonomy.yaml') as f:
        return yaml.safe_load(f)

def run_wizard():
    """Lance wizard interactif."""
    
    print("="*70)
    print("🧙 TAXONOMY SETUP WIZARD")
    print("="*70)
    print("\nCe wizard va vous aider à configurer les catégories")
    print("pertinentes pour VOTRE usage.\n")
    
    eu_tax = load_eu_taxonomy()
    questions = eu_tax['setup_wizard']['questions']
    
    user_config = {
        'enabled_objectives': [],
        'enabled_categories': []
    }
    
    for q in questions:
        print("─" * 70)
        print(f"\n❓ {q['question']}")
        print(f"   💡 {q['help']}")
        
        default = q.get('default', True)
        default_str = "O/n" if default else "o/N"
        
        response = input(f"\n   [{default_str}] : ").strip().lower()
        
        # Parse response
        if response == '':
            enabled = default
        elif response in ['o', 'oui', 'y', 'yes']:
            enabled = True
        elif response in ['n', 'non', 'no']:
            enabled = False
        else:
            enabled = default
        
        if enabled:
            user_config['enabled_categories'].extend(q['enables'])
            print(f"   ✅ Activé")
        else:
            print(f"   ⏭️  Ignoré")
    
    # Summary
    print("\n" + "="*70)
    print("📋 RÉCAPITULATIF CONFIGURATION")
    print("="*70)
    
    print(f"\n✅ Catégories activées : {len(user_config['enabled_categories'])}")
    for cat in user_config['enabled_categories']:
        print(f"   • {cat}")
    
    print("\n─" * 70)
    confirm = input("\n💾 Appliquer cette configuration ? [O/n] : ").strip().lower()
    
    if confirm in ['', 'o', 'oui', 'y', 'yes']:
        apply_config(user_config, eu_tax)
        print("\n✅ Configuration appliquée !")
    else:
        print("\n❌ Configuration annulée")

def apply_config(user_config, eu_tax):
    """Applique configuration à la DB."""
    
    conn = duckdb.connect('finance-system/data/finance.duckdb')
    
    # Parse enabled categories
    enabled_objectives = set()
    
    for cat_path in user_config['enabled_categories']:
        parts = cat_path.split('.')
        if len(parts) >= 1:
            enabled_objectives.add(parts[0])
    
    # FIX: objectives est au niveau racine, pas sous taxonomy
    objectives = eu_tax.get('objectives', {})
    
    if not objectives:
        print("\n⚠️  Warning: No objectives found in taxonomy YAML")
        conn.close()
        return
    
    # Get max category_id to continue numbering
    max_id = conn.execute("""
    SELECT COALESCE(MAX(category_id), 999) FROM taxonomy_categories
    """).fetchone()[0]
    
    category_id = max_id + 1
    inserted = 0
    
    for obj_key in enabled_objectives:
        if obj_key not in objectives:
            print(f"  ⚠️  Objective '{obj_key}' not found in YAML")
            continue
        
        obj = objectives[obj_key]
        
        # Insert objective (level 1)
        conn.execute("""
        INSERT OR IGNORE INTO taxonomy_categories
        (category_id, taxonomy_id, category_key, parent_id, display_name, level, path, icon, color, is_active)
        VALUES (?, 2, ?, NULL, ?, 1, ?, ?, ?, true)
        """, [
            category_id,
            obj_key,
            obj['display_name'],
            f"eu_finance/{obj_key}",
            obj.get('icon', ''),
            obj.get('color', '')
        ])
        
        objective_id = category_id
        category_id += 1
        inserted += 1
        
        # Insert categories (level 2)
        for cat_key, cat_data in obj.get('categories', {}).items():
            conn.execute("""
            INSERT OR IGNORE INTO taxonomy_categories
            (category_id, taxonomy_id, category_key, parent_id, display_name, level, path, is_active)
            VALUES (?, 2, ?, ?, ?, 2, ?, true)
            """, [
                category_id,
                cat_key,
                objective_id,
                cat_data['display'],
                f"eu_finance/{obj_key}/{cat_key}"
            ])
            
            category_id += 1
            inserted += 1
    
    # Mark taxonomy as configured and active
    conn.execute("""
    UPDATE taxonomies 
    SET is_active = true 
    WHERE taxonomy_key = 'eu_finance'
    """)
    
    conn.close()
    
    print(f"\n📊 {inserted} catégories EU configurées dans la base")

if __name__ == '__main__':
    run_wizard()
