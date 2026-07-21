import streamlit as st
from authentication.auth import authenticate
from audit.logger import log_event

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

            log_event(username=user["username"], 
                      
                      event_type="LOGIN_SUCCESS", 
                      description="User logged in successfully")

            st.success(f"Welcome, {user['username']}!")

            st.rerun()

        else:

            log_event(
            username=username,
            event_type="LOGIN_FAILED",
            description="Failed login attempt"
            )
            st.error("Invalid username or password.")

            