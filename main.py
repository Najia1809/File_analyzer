import streamlit as st
from login import login
from signup_page import signup

from analyzer import analyzer

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "page" not in st.session_state:
    st.session_state.page = "login"  # default page

st.title(" File Analyzer")

if not st.session_state.logged_in:
    if st.session_state.page == "login":
        login()
    elif st.session_state.page == "signup":
        signup()
else:
    analyzer()




    

