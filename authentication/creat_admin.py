import sqlite3
from password_utils import hash_password

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    role TEXT NOT NULL,
                    region TEXT NOT NULL,
                    active INTEGER NOT NULL DEFAULT 1
               
                )''')

admin_password = hash_password("Admin123!")

cursor.execute("INSERT INTO users (username, password, role, region, active) VALUES (?, ?, ?, ?, ?)", ("admin", 
                                                                                                       admin_password, "Admin", "All", 1))
conn.commit()
conn.close()

print("Admin user created successfully with username 'Admin' and password 'Admin123!'")
