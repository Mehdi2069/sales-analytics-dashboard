import streamlit as st
from authentication.auth import authenticate

def login_screen():
    st.title('Sales Analytics Login')

    username = st.text_input('Username')
    password = st.text_input('Password', type='password')

    if st.button('Login'):
        user = authenticate(username, password)
        if user:
            st.success_state = True
            st.success_state['user'] = user
            st.rerun()
            
        else:
            st.error("Invalid username or password. Please try again.")
            

