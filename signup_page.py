import streamlit as st
import json

def signup():
    st.subheader("Signup Page")
    username = st.text_input("Choose a username")
    password = st.text_input("Choose a password", type="password")

    if st.button("Create Account"):
        if username and password:
            with open("users.json", "r+") as file:
                users = json.load(file)
                if username in users:
                    st.error("Username already exists!")
                else:
                    users[username] = password
                    file.seek(0)
                    json.dump(users, file)
                    file.truncate()
                    st.success("Account created! You can now log in.")
                    st.session_state.page = "login"
        else:
            st.warning("Please fill in all fields.")

    # Back to login link
    if st.button("Already have an account? Login"):
        st.session_state.page = "login"




