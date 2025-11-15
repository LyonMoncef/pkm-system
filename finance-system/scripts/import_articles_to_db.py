#!/usr/bin/env python3
"""
Import articles_detail.xlsx into DuckDB
"""
import duckdb
import pandas as pd
from pathlib import Path

db_path = Path("finance-system/data/finance.duckdb")
excel_path = Path("finance-system/exports/powerbi/articles_detail.xlsx")

print("📥 Importing articles_detail into DuckDB...")

# Load Excel
df = pd.read_excel(excel_path)
print(f"  Loaded {len(df)} rows from Excel")

# Connect DB
conn = duckdb.connect(str(db_path))

# Drop if exists
conn.execute("DROP TABLE IF EXISTS articles_detail")

# Create from DataFrame
conn.execute("CREATE TABLE articles_detail AS SELECT * FROM df")

# Add category columns
conn.execute("ALTER TABLE articles_detail ADD COLUMN category_main TEXT")
conn.execute("ALTER TABLE articles_detail ADD COLUMN category_sub TEXT")
conn.execute("ALTER TABLE articles_detail ADD COLUMN tags TEXT")

# Verify
count = conn.execute("SELECT COUNT(*) FROM articles_detail").fetchone()[0]
print(f"✅ Created articles_detail table: {count} rows")

# Show columns
cols = conn.execute("DESCRIBE articles_detail").fetchall()
print("\nColumns:")
for col in cols:
    print(f"  - {col[0]}: {col[1]}")

conn.close()
print("\n✅ Done! Ready for categorization.")
