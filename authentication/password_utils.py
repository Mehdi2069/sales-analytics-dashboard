import bcrypt
import re


def hash_password(password: str) -> str:
    """
    Hash a plain-text password using bcrypt.
    """
    return bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")


def verify_password(password: str, hashed: str) -> bool:
    """
    Verify a plain-text password against a stored bcrypt hash.
    """
    return bcrypt.checkpw(
        password.encode("utf-8"),
        hashed.encode("utf-8")
    )

def validate_password(password):
    # Validate password strength. 
    # Returns: (TRUE, "") if valid.
    # (False, error_message) if invalid. 

    if len(password) < 8:
        return False, "Password must be at least 8 characters."
    
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter."
    
    if not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter."

    if not re.search(r'\d', password):
        return False, "Password must contain at least one number." 
    
    return True, ""


