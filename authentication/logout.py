import streamlit as st
from audit.logger import log_event


def logout():
    """Log out the user and reset session state."""
    
    user =st.session_state.get("user")

    if user:
        log_event(
            username = user['username'],
            event_type="LOGOUT",
            description="User logged out"
        )
    
    st.session_state.authenticated = False
    st.session_state.user = None

    st.rerun()  # Rerun the app to reflect the logout state
    