ROLE_PERMISSIONS = {
    "Admin": [
        "dashboard",
        "reports",
        "customers",
        "settings",
        "user_management"
    ],
    "Manager": [
        "dashboard",
        "reports",
        "customers"
    ],
    "Analyst": [
        "dashboard",
        "reports"
    ],
    "Viewer": [
        "dashboard"
    ]
}


def has_permission(role, permission):
    """
    Check whether a role has a specific permission.
    """
    return permission in ROLE_PERMISSIONS.get(role, [])
