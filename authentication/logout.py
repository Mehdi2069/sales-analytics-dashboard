import streamlit as st

def logout():
    """Log out the user and reset session state."""
    st.session_state.authenticated = False
    st.session_state.user = None

    st.rerun()  # Rerun the app to reflect the logout state
    