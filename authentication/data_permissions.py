def filter_data_by_user(df, user):
    """
    Filter the DataFrame based on the logged-in user's permissions.

    Parameters:
    - df: The DataFrame to filter.
    - user: Logged-in user information as a dictionary, including 'role' and 'region'.

    Returns:
    - A filtered DataFrame based on the user's permissions.
    """
    role = user["role"]
    region = user["region"]
    
    if user["role"] == "Admin":
        return df  # Admins can see all data
    else:
        return df[df["Region"] == user["region"]]  # Non-admins see only their region
    
