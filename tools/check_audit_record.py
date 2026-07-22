import sqlite3
from pathlib import Path

DATABASE_PATH = Path("audit/audit.db")

conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()

cursor.execute("""
               SELECT *
                FROM AuditLog;
               """
               )

records = cursor.fetchall()

print("Audit Records:")

for record in records:
    print(record)

conn.close()
