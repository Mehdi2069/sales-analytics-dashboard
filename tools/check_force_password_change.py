import sqlite3

from config.paths import DB_PATH

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
    SELECT username, force_password_change
    FROM users
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()