import streamlit as st

from authentication.login import login_screen
from app.sales_dashboard import main as dashboard_main




def initialize_session():
    """Initialize Streamlit session variables."""

    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if "user" not in st.session_state:
        st.session_state.user = None


def run_application():
    """Run the application."""

    initialize_session()

    if not st.session_state.authenticated:

        login_screen()

    else:

        dashboard_main()


if __name__ == "__main__":
    run_application()
