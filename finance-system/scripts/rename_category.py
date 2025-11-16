#!/usr/bin/env python3
"""
Rename Category Uniformly Across Database
"""
import duckdb
from pathlib import Path
import sys

def rename_category_main(old_name, new_name):
    """Renomme catégorie principale partout."""
    conn = duckdb.connect('finance-system/data/finance.duckdb')
    
    # Check combien d'articles concernés
    count = conn.execute("""
    SELECT COUNT(*) FROM articles_detail WHERE category_main = ?
    """, [old_name]).fetchone()[0]
    
    if count == 0:
        print(f"❌ Aucun article avec category_main = '{old_name}'")
        conn.close()
        return
    
    print(f"📊 {count} articles trouvés avec '{old_name}'")
    confirm = input(f"Renommer en '{new_name}' ? (y/n): ")
    
    if confirm.lower() == 'y':
        conn.execute("""
        UPDATE articles_detail 
        SET category_main = ? 
        WHERE category_main = ?
        """, [new_name, old_name])
        
        print(f"✅ {count} articles renommés : '{old_name}' → '{new_name}'")
    else:
        print("❌ Annulé")
    
    conn.close()

def rename_category_sub(old_name, new_name):
    """Renomme sous-catégorie partout."""
    conn = duckdb.connect('finance-system/data/finance.duckdb')
    
    count = conn.execute("""
    SELECT COUNT(*) FROM articles_detail WHERE category_sub = ?
    """, [old_name]).fetchone()[0]
    
    if count == 0:
        print(f"❌ Aucun article avec category_sub = '{old_name}'")
        conn.close()
        return
    
    print(f"📊 {count} articles trouvés avec '{old_name}'")
    confirm = input(f"Renommer en '{new_name}' ? (y/n): ")
    
    if confirm.lower() == 'y':
        conn.execute("""
        UPDATE articles_detail 
        SET category_sub = ? 
        WHERE category_sub = ?
        """, [new_name, old_name])
        
        print(f"✅ {count} articles renommés : '{old_name}' → '{new_name}'")
    else:
        print("❌ Annulé")
    
    conn.close()

if __name__ == '__main__':
    print("="*70)
    print("🏷️  CATEGORY RENAME TOOL")
    print("="*70)
    
    print("\n1. Renommer catégorie principale")
    print("2. Renommer sous-catégorie")
    choice = input("\nChoix (1 ou 2): ").strip()
    
    if choice == '1':
        old = input("Ancien nom catégorie principale: ").strip()
        new = input("Nouveau nom: ").strip()
        rename_category_main(old, new)
    elif choice == '2':
        old = input("Ancien nom sous-catégorie: ").strip()
        new = input("Nouveau nom: ").strip()
        rename_category_sub(old, new)
    else:
        print("❌ Choix invalide")
