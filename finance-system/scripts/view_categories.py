#!/usr/bin/env python3
"""View all categories and their usage"""
import duckdb

conn = duckdb.connect('finance-system/data/finance.duckdb')

print("="*70)
print("📊 CATEGORIES OVERVIEW")
print("="*70)

# Main categories
results = conn.execute("""
SELECT category_main, COUNT(*) as count, SUM(prix_total) as total
FROM articles_detail
WHERE category_main IS NOT NULL
GROUP BY category_main
ORDER BY total DESC
""").fetchall()

print("\n🏷️  MAIN CATEGORIES\n")
for cat, count, total in results:
    print(f"{cat:20} | {count:3} articles | {total:8.2f}€")

# Subcategories
print("\n" + "="*70)
print("📁 ALL SUBCATEGORIES")
print("="*70 + "\n")

results = conn.execute("""
SELECT category_main, category_sub, COUNT(*) as count, SUM(prix_total) as total
FROM articles_detail
WHERE category_sub IS NOT NULL
GROUP BY category_main, category_sub
ORDER BY category_main, total DESC
""").fetchall()

current_main = None
for cat_main, cat_sub, count, total in results:
    if cat_main != current_main:
        print(f"\n{cat_main}:")
        current_main = cat_main
    print(f"  ├─ {cat_sub:40} | {count:3} | {total:7.2f}€")

conn.close()
