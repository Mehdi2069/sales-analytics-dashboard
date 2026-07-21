from datetime import datetime
from audit.database import get_connection

#---------------------
# LOG EVENT
# --------------------

def log_event(username, event_type, description = None, ip_address = None, details = None):
    """
    Stores an audit event in the Auditlog tabel.
    """

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
                   INSERT INTO AuditLog (
                   timestamp, 
                   username,
                   event_type,
                   description,
                   ip_address, 
                   details
                   )
                   VALUES (?, ?, ?, ?, ?, ?)
                   """, 
                   (
                       timestamp,
                       username,
                       event_type,
                       description,
                       ip_address,
                       details
                    ))
    conn.commit()
    conn.close()

    print("✅ Audit event recorded.")         
