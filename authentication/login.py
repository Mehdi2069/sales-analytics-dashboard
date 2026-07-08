import streamlit as st
from authentication.auth import authenticate


def login_screen():
    """
    Display the login screen and authenticate users.
    """

    st.title("🔐 Sales Analytics Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        user = authenticate(username, password)

        if user:

            st.session_state.authenticated = True
            st.session_state.user = user

            st.success(f"Welcome, {user['username']}!")

            st.rerun()

        else:

            st.error("Invalid username or password.")

            