import sqlite3
from authentication.password_utils import verify_password

def authenticate(username, password):

    conn = sqlite3.connect('authentication/users.db')
    cursor = conn.cursor()

    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    
    user = cursor.fetchone()

    conn.close()

    if not user:
        return None
    
    stored_password = user[1]

    if verify_password(password, stored_password):
        return {"username": user[0], "role": user[2], "region": user[3], "active": user[4]}
    
    return None