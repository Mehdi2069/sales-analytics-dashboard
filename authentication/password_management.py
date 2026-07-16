import sqlite3

from config.paths import DB_PATH
from authentication.password_utils import (verify_password, hash_password, validate_password)

def change_my_password(username, current_password, new_password):
    """ Change a user's password after verifying the current password. """

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Get the current password hash
    cursor.execute(''' 
                   SELECT password 
                   FROM users
                   WHERE username = ?
                   ''', (username,)
    )

    row = cursor.fetchone()

    if row is None:
        conn.close()
        return False, "User not found."
    stored_password = row[0]

    # Verify current password 
    if not verify_password(current_password, stored_password):
        conn.close()
        return False, "Current password is incorrect."
    
    valid, message = validate_password(new_password)

    if not valid:
        conn.close()
        return False, message
    
    
    # Hash the new password 
    new_password_hash = hash_password(new_password)

    # Update the password
    cursor.execute(
        '''
        UPDATE users 
        SET password = ?,
            force_password_change = 0
        WHERE username = ?
        ''', (new_password_hash, username))
    
    conn.commit()
    conn.close()

    return True, "✅ Your password has been changed successfully."

    
    

