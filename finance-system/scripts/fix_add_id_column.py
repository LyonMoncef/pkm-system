#!/usr/bin/env python3
"""
Add id column to articles_detail for Power BI compatibility
"""
import duckdb
from pathlib import Path

db_path = Path("finance-system/data/finance.duckdb")

print("🔧 Adding id column to articles_detail...")

conn = duckdb.connect(str(db_path))

# Check if id already exists
cols = [c[0] for c in conn.execute("DESCRIBE articles_detail").fetchall()]

if 'id' in cols:
    print("✅ Column id already exists")
else:
    # Create temp table with id
    print("  Creating id column...")
    
    conn.execute("""
    CREATE TABLE articles_detail_new AS
    SELECT 
        ROW_NUMBER() OVER (ORDER BY transaction_id) as id,
        *
    FROM articles_detail
    """)
    
    # Drop old, rename new
    conn.execute("DROP TABLE articles_detail")
    conn.execute("ALTER TABLE articles_detail_new RENAME TO articles_detail")
    
    print("✅ Column id added (auto-incremented)")

# Verify
result = conn.execute("SELECT COUNT(*), MIN(id), MAX(id) FROM articles_detail").fetchone()
print(f"\n📊 Verification:")
print(f"  Total rows: {result[0]}")
print(f"  ID range: {result[1]} to {result[2]}")

# Show structure
print("\n📋 New structure:")
for col in conn.execute("DESCRIBE articles_detail").fetchall():
    print(f"  - {col[0]}: {col[1]}")

conn.close()

print("\n✅ Done! Ready for Power BI refresh.")
