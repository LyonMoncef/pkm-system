#!/usr/bin/env python3
"""Finance System - Web UI v2.0 - Dual Taxonomy"""

from flask import Flask, render_template, request, jsonify
import duckdb
from pathlib import Path

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-key'

DB_PATH = Path("../data/finance.duckdb")

def get_db():
    return duckdb.connect(str(DB_PATH))

@app.route('/')
def index():
    conn = get_db()
    
    stats = {
        'total_articles': conn.execute("SELECT COUNT(*) FROM articles_detail").fetchone()[0],
        'total_amount': conn.execute("SELECT COALESCE(SUM(prix_total), 0) FROM articles_detail").fetchone()[0],
        'total_taxonomies': conn.execute("SELECT COUNT(*) FROM taxonomies WHERE is_active = true").fetchone()[0],
        'uncategorized': conn.execute("SELECT COUNT(*) FROM articles_detail WHERE category_main IS NULL").fetchone()[0],
    }
    
    top_categories = conn.execute("""
    SELECT category_main, COUNT(*) as count, SUM(prix_total) as total
    FROM articles_detail
    WHERE category_main IS NOT NULL
    GROUP BY category_main
    ORDER BY total DESC
    LIMIT 5
    """).fetchall()
    
    timeline = conn.execute("""
    SELECT date, COUNT(*) as count, SUM(prix_total) as total
    FROM articles_detail
    GROUP BY date
    ORDER BY date DESC
    LIMIT 7
    """).fetchall()
    
    taxonomies = conn.execute("""
    SELECT taxonomy_id, taxonomy_key, display_name, icon, is_default
    FROM taxonomies
    WHERE is_active = true
    ORDER BY is_default DESC
    """).fetchall()
    
    conn.close()
    
    return render_template('index.html', 
                         stats=stats,
                         top_categories=top_categories,
                         timeline=timeline,
                         taxonomies=taxonomies)

@app.route('/categories')
@app.route('/categories/<taxonomy_key>')
def categories(taxonomy_key='budget'):
    conn = get_db()
    
    # Get taxonomy
    taxonomy = conn.execute("""
    SELECT taxonomy_id, taxonomy_key, display_name, icon, description
    FROM taxonomies
    WHERE taxonomy_key = ?
    """, [taxonomy_key]).fetchone()
    
    if not taxonomy:
        taxonomy = conn.execute("""
        SELECT taxonomy_id, taxonomy_key, display_name, icon, description
        FROM taxonomies WHERE is_default = true
        """).fetchone()
        taxonomy_key = taxonomy[1] if taxonomy else 'budget'
    
    taxonomy_id = taxonomy[0]
    
    # Build tree - CRITICAL: Initialize empty dict
    categories_tree = {}
    
    # Level 1
    level1 = conn.execute("""
    SELECT category_id, category_key, display_name, icon, color
    FROM taxonomy_categories
    WHERE taxonomy_id = ? AND (level = 1 OR parent_id IS NULL)
    ORDER BY category_id
    """, [taxonomy_id]).fetchall()
    
    for cat_id, cat_key, display, icon, color in level1:
        if not cat_key:
            continue
        
        categories_tree[cat_key] = {
            'id': cat_id,
            'display_name': display,
            'icon': icon or '📁',
            'color': color or '',
            'subcategories': []
        }
        
        # Get children
        subs = conn.execute("""
        SELECT category_id, category_key, display_name, level
        FROM taxonomy_categories
        WHERE taxonomy_id = ? AND parent_id = ?
        ORDER BY category_id
        """, [taxonomy_id, cat_id]).fetchall()
        
        for sub_id, sub_key, sub_display, level in subs:
            categories_tree[cat_key]['subcategories'].append({
                'id': sub_id,
                'key': sub_key or 'unknown',
                'display': sub_display,
                'level': level or 2
            })
    
    # Stats
    category_stats = {}
    stats_data = conn.execute("""
    SELECT category_main, COUNT(*) as count, SUM(prix_total) as total
    FROM articles_detail
    WHERE category_main IS NOT NULL
    GROUP BY category_main
    """).fetchall()
    
    for cat, count, total in stats_data:
        category_stats[cat] = {'count': count, 'total': total}
    
    # All taxonomies
    taxonomies = conn.execute("""
    SELECT taxonomy_id, taxonomy_key, display_name, icon
    FROM taxonomies WHERE is_active = true
    ORDER BY is_default DESC
    """).fetchall()
    
    conn.close()
    
    # MUST pass all variables
    return render_template('categories.html',
                         taxonomy=taxonomy,
                         categories_tree=categories_tree,
                         stats=category_stats,
                         taxonomies=taxonomies,
                         current_taxonomy=taxonomy_key)

@app.route('/categories/rename', methods=['POST'])
def rename_category():
    data = request.json
    old_name = data.get('old_name')
    new_name = data.get('new_name')
    level = data.get('level', 'main')
    
    if not old_name or not new_name:
        return jsonify({'error': 'Missing parameters'}), 400
    
    conn = get_db()
    
    if level == 'main':
        conn.execute("UPDATE articles_detail SET category_main = ? WHERE category_main = ?", 
                    [new_name, old_name])
        affected = conn.execute("SELECT COUNT(*) FROM articles_detail WHERE category_main = ?", 
                              [new_name]).fetchone()[0]
    else:
        conn.execute("UPDATE articles_detail SET category_sub = ? WHERE category_sub = ?", 
                    [new_name, old_name])
        affected = conn.execute("SELECT COUNT(*) FROM articles_detail WHERE category_sub = ?", 
                              [new_name]).fetchone()[0]
    
    conn.close()
    
    return jsonify({'success': True, 'affected': affected})

@app.route('/articles')
def articles():
    category = request.args.get('category')
    merchant = request.args.get('merchant')
    search = request.args.get('search')
    
    conn = get_db()
    
    query = "SELECT id, transaction_id, date, merchant, article, prix_total, category_main, category_sub FROM articles_detail WHERE 1=1"
    params = []
    
    if category:
        query += " AND category_main = ?"
        params.append(category)
    if merchant:
        query += " AND merchant = ?"
        params.append(merchant)
    if search:
        query += " AND article LIKE ?"
        params.append(f'%{search}%')
    
    query += " ORDER BY date DESC LIMIT 100"
    
    articles_list = conn.execute(query, params).fetchall()
    
    categories = [c[0] for c in conn.execute(
        "SELECT DISTINCT category_main FROM articles_detail WHERE category_main IS NOT NULL ORDER BY category_main"
    ).fetchall()]
    
    merchants = [m[0] for m in conn.execute(
        "SELECT DISTINCT merchant FROM articles_detail ORDER BY merchant"
    ).fetchall()]
    
    conn.close()
    
    return render_template('articles.html',
                         articles=articles_list,
                         categories=categories,
                         merchants=merchants)

@app.route('/articles/update', methods=['POST'])
def update_article():
    data = request.json
    conn = get_db()
    conn.execute("UPDATE articles_detail SET category_main = ?, category_sub = ? WHERE id = ?",
                [data['category_main'], data['category_sub'], data['id']])
    conn.close()
    return jsonify({'success': True})

@app.route('/articles/bulk-update', methods=['POST'])
def bulk_update_articles():
    data = request.json
    ids = data.get('ids', [])
    
    if not ids:
        return jsonify({'error': 'No articles'}), 400
    
    conn = get_db()
    placeholders = ','.join(['?' for _ in ids])
    conn.execute(f"UPDATE articles_detail SET category_main = ?, category_sub = ? WHERE id IN ({placeholders})",
                [data['category_main'], data['category_sub']] + ids)
    conn.close()
    
    return jsonify({'success': True, 'count': len(ids)})

@app.route('/stats')
def stats():
    conn = get_db()
    
    by_category = conn.execute("""
    SELECT category_main, COUNT(*), SUM(prix_total), AVG(prix_total), MIN(prix_total), MAX(prix_total)
    FROM articles_detail WHERE category_main IS NOT NULL
    GROUP BY category_main ORDER BY SUM(prix_total) DESC
    """).fetchall()
    
    by_merchant = conn.execute("""
    SELECT merchant, COUNT(*), SUM(prix_total)
    FROM articles_detail GROUP BY merchant ORDER BY SUM(prix_total) DESC
    """).fetchall()
    
    monthly = conn.execute("""
    SELECT strftime('%Y-%m', date), COUNT(*), SUM(prix_total)
    FROM articles_detail GROUP BY strftime('%Y-%m', date) ORDER BY 1
    """).fetchall()
    
    conn.close()
    
    return render_template('stats.html',
                         by_category=by_category,
                         by_merchant=by_merchant,
                         monthly=monthly)

@app.route('/api/taxonomies')
def api_taxonomies():
    conn = get_db()
    taxonomies = conn.execute("""
    SELECT taxonomy_id, taxonomy_key, display_name, icon, is_default,
           (SELECT COUNT(*) FROM taxonomy_categories WHERE taxonomy_id = t.taxonomy_id)
    FROM taxonomies t WHERE is_active = true
    ORDER BY is_default DESC
    """).fetchall()
    conn.close()
    
    return jsonify([{
        'id': t[0], 'key': t[1], 'name': t[2], 
        'icon': t[3], 'is_default': bool(t[4]), 'categories': t[5]
    } for t in taxonomies])

if __name__ == '__main__':
    print("="*70)
    print("🌐 FINANCE SYSTEM - WEB UI v2.0 (Dual Taxonomy)")
    print("="*70)
    print("\n📍 http://localhost:5000")
    print("\nPages:")
    print("  - Dashboard: http://localhost:5000/")
    print("  - Categories Budget: http://localhost:5000/categories")
    print("  - Categories Detailed: http://localhost:5000/categories/finance_detailed")
    print("  - Articles: http://localhost:5000/articles")
    print("  - Stats: http://localhost:5000/stats")
    print("\n🛑 Ctrl+C to stop\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
