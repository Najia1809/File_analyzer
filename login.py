import streamlit as st
import json

def login():
    st.subheader("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        with open("users.json", "r") as file:
            users = json.load(file)
            if username in users and users[username] == password:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.success("Login successful!")
            else:
                st.error("Invalid username or password.")

    # Link to Signup Page
    if st.button("Don't have an account? Signup"):
        st.session_state.page = "signup"

        

