import streamlit as st

from authentication.login import login_screen
from app.sales_dashboard import main as dashboard_main

def initialize_session():
    '''Initialize session state variables. '''
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if 'username' not in st.session_state:
        st.session_state.username = None

def run_application():
    '''Run the main application. '''
    initialize_session()
    if st.session_state.authenticated:

        login_screen()

    else:
        dashboard_main()

if __name__ == "__main__":
    