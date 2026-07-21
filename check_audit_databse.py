import sqlite3
from pathlib import Path


DATABASE_PATH = Path("audit/audit.db")


conn = sqlite3.connect(DATABASE_PATH)

cursor = conn.cursor()


cursor.execute("""
    SELECT name 
    FROM sqlite_master 
    WHERE type='table';
""")

tables = cursor.fetchall()

print("Tables:")
for table in tables:
    print(table[0])


cursor.execute("""
    PRAGMA table_info(AuditLog);
""")

columns = cursor.fetchall()

print("\nColumns:")
for column in columns:
    print(column)


conn.close()
