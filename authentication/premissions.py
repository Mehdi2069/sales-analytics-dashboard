ROLE_PREMISSIONS = {
    "Admin": ["dashboard", "reports", "customers", "settings", "user_management"],
    "Manager": ["dashboard", "reports", "customers"],
    "Analyst": ["dashboard", "reports"],
    'Viewer': ["dashboard"]
}

def has_permission(role, permission):
    """
    Check if a given role has the specified permission.

    Args:
        role (str): The role of the user (e.g., "Admin", "Manager", "Analyst", "Viewer").
        permission (str): The permission to check (e.g., "dashboard", "reports").

    Returns:
        bool: True if the role has the permission, False otherwise.
    """
    return permission in ROLE_PREMISSIONS.get(role, [])
