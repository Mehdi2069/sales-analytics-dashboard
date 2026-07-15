import sqlite3

conn = sqlite3.connect("authentication/users.db")
cursor = conn.cursor()

# Check whether the columns already exist

cursor.execute("PRAGMA table_info(users)")
columns = [column[1] for column in cursor.fetchall()]

if "force_password_change" not in columns:
    cursor.execute("ALTER TABLE users ADD COLUMN force_password_change INTEGER NOT NULL DEFAULT 0")

    print("✅ force_password_change column added.")
    
else:
    print("ℹ️ force_password_change column already exists.")
    
conn.commit()
conn.close()


          