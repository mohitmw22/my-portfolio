import streamlit as st

st.set_page_config(layout="wide")

st.title("Contact Us")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address:")
    message = st.text_area("Your message:")
    button = st.form_submit_button()

    if button:
        print("button pressed!")