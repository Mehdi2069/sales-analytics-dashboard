import sqlite3
from pathlib import Path


# -------------------------
# DATABASE LOCATION
# -------------------------

BASE_DIR = Path(__file__).resolve().parent
DATABASE_PATH = BASE_DIR / "audit.db"

#----------------------------------
# DATABASE CONNECTIN 
#---------------------------------

def get_connection():
    """Creates and returns a connection to the audit database."""

    return sqlite3.connect(DATABASE_PATH)


# -------------------------
# CREATE DATABASE
# -------------------------

def initialize_audit_database():

    conn = sqlite3.connect(DATABASE_PATH)
  
    cursor = conn.cursor()
   
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS AuditLog (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            username TEXT NOT NULL,
            event_type TEXT NOT NULL,
            description TEXT,
            ip_address TEXT,
            details TEXT
        )
    """)
    
    conn.commit()
    
    conn.close()
   

    print("✅ Audit database initialized.")