import streamlit as st
from send_email import send_email
import pandas as pd

df = pd.read_csv("topics.csv")
with st.form(key="mail_form"):
    user_mail = st.text_input("Your Email Address")
    user_topic = st.selectbox("Choose a topic", df["topic"])
    text = st.text_area("Text")
    message = f"""\
SUBJECT: New email from {user_mail}

From: {user_mail}
Topic: {user_topic}
{text}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email was sent successfully and has been received by our team")
