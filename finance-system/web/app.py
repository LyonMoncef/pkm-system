#!/usr/bin/env python3
"""
Finance System - Web UI
========================

Flask app for category management and statistics.
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for
import duckdb
import yaml
from pathlib import Path
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-key-change-in-production'

# Paths
DB_PATH = Path("../data/finance.duckdb")
TAXONOMY_PATH = Path("../taxonomy/categories.yaml")

# ============================================================================
# DATABASE HELPERS
# ============================================================================

def get_db():
    """Get database connection."""
    return duckdb.connect(str(DB_PATH))

def load_taxonomy():
    """Load taxonomy from YAML."""
    with open(TAXONOMY_PATH) as f:
        return yaml.safe_load(f)

def save_taxonomy(taxonomy):
    """Save taxonomy to YAML."""
    with open(TAXONOMY_PATH, 'w') as f:
        yaml.dump(taxonomy, f, allow_unicode=True, sort_keys=False)

# ============================================================================
# ROUTES - DASHBOARD
# ============================================================================

@app.route('/')
def index():
    """Dashboard principal."""
    conn = get_db()
    
    # Stats globales
    stats = {
        'total_articles': conn.execute("SELECT COUNT(*) FROM articles_detail").fetchone()[0],
        'total_amount': conn.execute("SELECT COALESCE(SUM(prix_total), 0) FROM articles_detail").fetchone()[0],
        'total_categories': conn.execute("SELECT COUNT(DISTINCT category_main) FROM articles_detail WHERE category_main IS NOT NULL").fetchone()[0],
        'uncategorized': conn.execute("SELECT COUNT(*) FROM articles_detail WHERE category_main IS NULL").fetchone()[0],
    }
    
    # Top catégories
    top_categories = conn.execute("""
    SELECT category_main, COUNT(*) as count, SUM(prix_total) as total
    FROM articles_detail
    WHERE category_main IS NOT NULL
    GROUP BY category_main
    ORDER BY total DESC
    LIMIT 5
    """).fetchall()
    
    # Timeline derniers jours
    timeline = conn.execute("""
    SELECT date, COUNT(*) as count, SUM(prix_total) as total
    FROM articles_detail
    GROUP BY date
    ORDER BY date DESC
    LIMIT 7
    """).fetchall()
    
    conn.close()
    
    return render_template('index.html', 
                         stats=stats,
                         top_categories=top_categories,
                         timeline=timeline)

# ============================================================================
# ROUTES - CATEGORIES
# ============================================================================

@app.route('/categories')
def categories():
    """Gestion catégories."""
    conn = get_db()
    taxonomy = load_taxonomy()
    
    # Get usage stats for each category
    category_stats = {}
    
    results = conn.execute("""
    SELECT 
        category_main,
        COUNT(*) as count,
        SUM(prix_total) as total
    FROM articles_detail
    WHERE category_main IS NOT NULL
    GROUP BY category_main
    """).fetchall()
    
    for cat, count, total in results:
        category_stats[cat] = {'count': count, 'total': total}
    
    conn.close()
    
    return render_template('categories.html',
                         taxonomy=taxonomy['categories'],
                         stats=category_stats)

@app.route('/categories/rename', methods=['POST'])
def rename_category():
    """Renommer catégorie."""
    data = request.json
    old_name = data.get('old_name')
    new_name = data.get('new_name')
    level = data.get('level', 'main')  # 'main' or 'sub'
    
    if not old_name or not new_name:
        return jsonify({'error': 'Missing parameters'}), 400
    
    conn = get_db()
    
    # Update database
    if level == 'main':
        count = conn.execute("""
        UPDATE articles_detail 
        SET category_main = ? 
        WHERE category_main = ?
        """, [new_name, old_name]).fetchone()
    else:
        count = conn.execute("""
        UPDATE articles_detail 
        SET category_sub = ? 
        WHERE category_sub = ?
        """, [new_name, old_name]).fetchone()
    
    conn.close()
    
    return jsonify({'success': True, 'message': f'Renamed {old_name} to {new_name}'})

@app.route('/categories/delete', methods=['POST'])
def delete_category():
    """Supprimer catégorie (réassigne à 'Autres')."""
    data = request.json
    category_name = data.get('name')
    level = data.get('level', 'main')
    
    conn = get_db()
    
    if level == 'main':
        conn.execute("""
        UPDATE articles_detail 
        SET category_main = 'Autres' 
        WHERE category_main = ?
        """, [category_name])
    else:
        conn.execute("""
        UPDATE articles_detail 
        SET category_sub = 'Divers' 
        WHERE category_sub = ?
        """, [category_name])
    
    conn.close()
    
    return jsonify({'success': True})

# ============================================================================
# ROUTES - ARTICLES
# ============================================================================

@app.route('/articles')
def articles():
    """Liste articles avec filtres."""
    # Filtres
    category = request.args.get('category')
    merchant = request.args.get('merchant')
    search = request.args.get('search')
    
    conn = get_db()
    
    # Base query
    query = """
    SELECT 
        id, transaction_id, date, merchant, article, 
        prix_total, category_main, category_sub
    FROM articles_detail
    WHERE 1=1
    """
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
    
    query += " ORDER BY date DESC, prix_total DESC LIMIT 100"
    
    articles_list = conn.execute(query, params).fetchall()
    
    # Get distinct values for filters
    categories = conn.execute("""
    SELECT DISTINCT category_main FROM articles_detail 
    WHERE category_main IS NOT NULL 
    ORDER BY category_main
    """).fetchall()
    
    merchants = conn.execute("""
    SELECT DISTINCT merchant FROM articles_detail 
    ORDER BY merchant
    """).fetchall()
    
    conn.close()
    
    return render_template('articles.html',
                         articles=articles_list,
                         categories=[c[0] for c in categories],
                         merchants=[m[0] for m in merchants])

@app.route('/articles/update', methods=['POST'])
def update_article():
    """Mettre à jour catégorie d'un article."""
    data = request.json
    article_id = data.get('id')
    category_main = data.get('category_main')
    category_sub = data.get('category_sub')
    
    conn = get_db()
    
    conn.execute("""
    UPDATE articles_detail
    SET category_main = ?, category_sub = ?
    WHERE id = ?
    """, [category_main, category_sub, article_id])
    
    conn.close()
    
    return jsonify({'success': True})

@app.route('/articles/bulk-update', methods=['POST'])
def bulk_update_articles():
    """Mise à jour en masse."""
    data = request.json
    article_ids = data.get('ids', [])
    category_main = data.get('category_main')
    category_sub = data.get('category_sub')
    
    if not article_ids:
        return jsonify({'error': 'No articles selected'}), 400
    
    conn = get_db()
    
    placeholders = ','.join(['?' for _ in article_ids])
    conn.execute(f"""
    UPDATE articles_detail
    SET category_main = ?, category_sub = ?
    WHERE id IN ({placeholders})
    """, [category_main, category_sub] + article_ids)
    
    conn.close()
    
    return jsonify({'success': True, 'count': len(article_ids)})

# ============================================================================
# ROUTES - STATISTICS
# ============================================================================

@app.route('/stats')
def stats():
    """Statistiques détaillées."""
    conn = get_db()
    
    # Par catégorie
    by_category = conn.execute("""
    SELECT 
        category_main,
        COUNT(*) as count,
        SUM(prix_total) as total,
        AVG(prix_total) as avg,
        MIN(prix_total) as min,
        MAX(prix_total) as max
    FROM articles_detail
    WHERE category_main IS NOT NULL
    GROUP BY category_main
    ORDER BY total DESC
    """).fetchall()
    
    # Par enseigne
    by_merchant = conn.execute("""
    SELECT 
        merchant,
        COUNT(*) as count,
        SUM(prix_total) as total
    FROM articles_detail
    GROUP BY merchant
    ORDER BY total DESC
    """).fetchall()
    
    # Timeline mensuelle
    monthly = conn.execute("""
    SELECT 
        strftime('%Y-%m', date) as month,
        COUNT(*) as count,
        SUM(prix_total) as total
    FROM articles_detail
    GROUP BY month
    ORDER BY month
    """).fetchall()
    
    conn.close()
    
    return render_template('stats.html',
                         by_category=by_category,
                         by_merchant=by_merchant,
                         monthly=monthly)

# ============================================================================
# API ENDPOINTS
# ============================================================================

@app.route('/api/categories')
def api_categories():
    """API: Liste catégories."""
    conn = get_db()
    
    categories = conn.execute("""
    SELECT DISTINCT category_main 
    FROM articles_detail 
    WHERE category_main IS NOT NULL
    ORDER BY category_main
    """).fetchall()
    
    conn.close()
    
    return jsonify([c[0] for c in categories])

@app.route('/api/stats/summary')
def api_stats_summary():
    """API: Stats résumées."""
    conn = get_db()
    
    stats = {
        'total': conn.execute("SELECT COUNT(*) FROM articles_detail").fetchone()[0],
        'total_amount': float(conn.execute("SELECT COALESCE(SUM(prix_total), 0) FROM articles_detail").fetchone()[0]),
        'by_category': {}
    }
    
    results = conn.execute("""
    SELECT category_main, COUNT(*), SUM(prix_total)
    FROM articles_detail
    WHERE category_main IS NOT NULL
    GROUP BY category_main
    """).fetchall()
    
    for cat, count, total in results:
        stats['by_category'][cat] = {
            'count': count,
            'total': float(total)
        }
    
    conn.close()
    
    return jsonify(stats)

# ============================================================================
# MAIN
# ============================================================================

if __name__ == '__main__':
    print("="*70)
    print("🌐 FINANCE SYSTEM - WEB UI")
    print("="*70)
    print("\n📍 http://localhost:5000")
    print("\nPages:")
    print("  - Dashboard: http://localhost:5000/")
    print("  - Categories: http://localhost:5000/categories")
    print("  - Articles: http://localhost:5000/articles")
    print("  - Stats: http://localhost:5000/stats")
    print("\n🛑 Press Ctrl+C to stop\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
