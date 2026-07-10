import sqlite3
from pathlib import Path
import pandas as pd
import streamlit as st
from authentication.password_utils import hash_password


BASE_DIR = Path(__file__).resolve().parents[1]
DB_PATH = BASE_DIR / "authentication" / "users.db"

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
    hashed_password = hash_password(password)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Check if the username already exists
    cursor.execute("SELECT username FROM users WHERE username = ?", (username,))
   
    existing_user = cursor.fetchone()

    if existing_user:
        st.error("❌ Username already exists!")
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
      
    st.rerun()


       

       