from os import name
import sqlite3
from pathlib import Path
import pandas as pd
import streamlit as st
from authentication.password_utils import hash_password


from config.paths import DB_PATH

@st.cache_data

def load_users():
    '''Load users from the SQLite database.'''

    conn = sqlite3.connect(DB_PATH)

    query = """ SELECT \
    id, \
    username,\
    role,\
    region, \
    active \
    FROM users \
    ORDER BY username """

    users = pd.read_sql_query(query, conn)
    conn.close()
    return users

def create_user(username, password, role, region, active):
    '''Create a new user in the SQLite database.'''
   
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Check if the username already exists
    cursor.execute("SELECT username FROM users WHERE username = ?", (username,))
   
    existing_user = cursor.fetchone()

    if existing_user:
        conn.close()
        return False    
    # Hash the password
    hashed_password = hash_password(password)

    # Insert the new user into the database
    cursor.execute("""
        INSERT INTO users (username, password, role, region, active)
        VALUES (?, ?, ?, ?, ?)
    """, (username, hashed_password, role, region, int(active)))

    conn.commit()
    conn.close()

    return True

def load_user_details(username):
    '''Load user details from the SQLite database.'''
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, username, role, region, active
        FROM users
        WHERE username = ?
    """, (username,))

    user_details = cursor.fetchone()
    conn.close()

    if user_details is None:
        return None
    return {
        "id": user_details[0],
        "username": user_details[1],
        "role": user_details[2],
        "region": user_details[3],
        "active": bool(user_details[4])
    }

def update_user(user_id, role, region, active):
    '''Update an existing user in the SQLite database.'''
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE users
        SET role = ?, region = ?, active = ?
        WHERE id = ?
    """, (role, region, int(active), user_id))

    conn.commit()
    conn.close()

def reset_user_password(username, new_password):
    ''' Reset a user's password by an administrator. 
    The users will be foced to change the password at next login. '''

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Check if user exists
    cursor.execute(
                """ 
                   SELECT username 
                   FROM users 
                   WHERE username =?
                    """, 
                    (username,))
    
    user = cursor.fetchone()

    if user is None:
        conn.close()
        return False, "User not found."
    
    # Hash the new password
    new_password_hash = hash_password(new_password)

    # Update password and force change on next login    

    cursor.execute(
        """ 
        UPDATE users
        SET password = ?,
            force_password_change = 1
        WHERE username = ?
        """,
        (new_password_hash, username)
    )
    conn.commit()
    conn.close()
    return True, "Password reset successfully." 

    

def delete_user(user_id):
    '''Delete a user from the SQLite database.'''
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))

    conn.commit()
    conn.close()


def user_management_page():
    '''Display the User Management page.'''

    st.header("👥 User Management")

    st.subheader("Current System Users")

    users = load_users()

    st.dataframe(users, use_container_width=True)

    st.markdown("---")
    st.subheader("➕ Create New User")

    # Create a form for creating a new user

    with st.form("create_user_form"):
        username = st.text_input("Username")

        password = st.text_input("Password", type="password")
        
        role = st.selectbox("Role", ["Admin", "Manager", "Analyst", "Viewer"])

        region = st.selectbox("Region", ["All", "Europe", "North America", "Asia", "South America"])

        active = st.checkbox("Active", value=True)

        submit= st.form_submit_button("Create User")
    if submit:
        success = create_user(username, password, role, region, active)

        if success:
            st.cache_data.clear()  # Clear the cache to reload users
            st.success("✅ User created successfully!")
            st.rerun()
        else:
            st.error("❌ Username already exists. Please choose a different username.")
      
    st.markdown("---")
    st.subheader("✏️ Edit User")
   
    users = load_users()
    
    selected_username = st.selectbox("Select User to Edit", users["username"]) 
    user = load_user_details(selected_username)
    user_id = user["id"]  # Get the user ID for updating

    roles = ['Admin', 'Manager', 'Analyst', 'Viewer']

    regions = ['All', 'Europe', 'North America', 'Asia', 'South America']

    edit_role = st.selectbox("Role", roles, index=roles.index(user["role"]))

    edit_region = st.selectbox("Region", regions, index=regions.index(user["region"]))

    edit_active = st.checkbox("Active", value=user["active"])

    update_button = st.button("Update User")

    if update_button:
        update_user(user_id, edit_role, edit_region, edit_active)
        st.cache_data.clear()  # Clear the cache to reload users
        st.success("✅ User updated successfully!")
        st.rerun()  # Rerun the app to reflect the updated user details

#-------------------------------------------------------------------------
    # Reset User Passwor by Admin users 

    st.markdown("---")
    st.subheader("🔑 Reset User Password")

    temporary_password = st.text_input("Teporary Password", type="password")

    if st.button("Reset Password"):
        success, message = reset_user_password(selected_username, temporary_password)
        if success:
            st.success(message)

        else:
            st.error(message)

# -----------------------------------------------------------------------

    st.markdown("---")
    st.subheader("🗑️ Delete User")

    if st.button("🗑️ Delete User"):
        if selected_username == st.session_state.user["username"]:
            st.error("❌ You cannot delete your own account.")

        elif user["role"] == 'Admin':
            st.error("❌ You cannot delete an Admin user.")
        else:
            delete_user(user_id)
            st.cache_data.clear()  # Clear the cache to reload users
            st.success("✅ User deleted successfully!")
            st.rerun()  # Rerun the app to reflect the updated user list

 
   


       

       