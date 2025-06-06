import streamlit as st
import os
from dotenv import load_dotenv
from email_api import check_email_breach
from utils import validate_email

load_dotenv()

st.markdown(
    """
    <h1 style='color:#FF4B4B; font-family:monospace;'>🔍 SecureMail Inspector</h1>
    <p style='font-size:18px;'>Check if your email has been exposed in public data breaches.<br>
    <span style='color:#888;'>Powered by Odogwu Howard</span></p>
    """,
    unsafe_allow_html=True
)

email = st.text_input("🔑 Enter your email address:")

custom_btn = """
    <style>
    div.stButton > button:first-child {
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        height: 3em;
        width: 12em;
        margin: 0.5em 0;
    }
    </style>
"""
st.markdown(custom_btn, unsafe_allow_html=True)

if st.button("Scan for Breaches 🚨"):
    if not validate_email(email):
        st.error("❌ Please enter a valid email address.")
    else:
        api_key = os.getenv("EMAIL_API_KEY")
        if not api_key:
            st.error("API key not found. Please set the EMAIL_API_KEY environment variable.")
        else:
            st.info(f"Scanning breaches for **{email}** ...")
            result = check_email_breach(api_key, email)
            if isinstance(result, list) and result:
                st.success(f"🎯 Results for {email}:")
                for breach in result:
                    # Show the actual breach object for debugging
                    # st.json(breach)
                    # Replace 'Name', 'Date', 'Info' with your actual keys!
                    st.markdown(
                        f"""
                        <div style='background:#222;padding:1em 1.5em;margin:1em 0;border-radius:10px;'>
                        <h3 style='color:#FF4B4B;margin-bottom:0.2em;'>{breach.get('Name', 'No Name')}</h3>
                        <p style='margin:0.2em 0 0.5em 0;color:#aaa;'>🗓️ {breach.get('Date', 'Unknown Date')}</p>
                        <p style='color:#fff;'>{breach.get('Info', 'No details available.')}</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                st.info("🔒 **Tip:** Change your passwords and enable Multi-Factor Authentication (MFA)!")
            elif result is None or (isinstance(result, list) and not result):
                st.success(f"✅ Good news! No breaches found for {email}.")
            else:
                st.error(f"⚠️ An error occurred: {result}")

st.markdown(
    "<hr><center><span style='color:#888;'>Made with ❤️ by Odogwu Howard</span></center>",
    unsafe_allow_html=True
)