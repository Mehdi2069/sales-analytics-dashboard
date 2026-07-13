import sqlite3

from authentication.password_utils import verify_password

from config.paths import DB_PATH

def authenticate(username, password):
    """
    Authenticate a user against the SQLite database.
    """

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT username,
               password,
               role,
               region,
               active
        FROM users
        WHERE username = ?
        """,
        (username,)
    )

    user = cursor.fetchone()

    conn.close()

    if user is None:
        return None

    # Check if account is active
    if user[4] != 1:
        return None

    stored_password = user[1]

    if verify_password(password, stored_password):

        return {
            "username": user[0],
            "role": user[2],
            "region": user[3],
            "active": bool(user[4])
        }

    return None
