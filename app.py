import streamlit as st
import os
from dotenv import load_dotenv
from email_api import check_email_breach
from utils import validate_email

load_dotenv()

st.title("OSINT Email Security Tool")

email = st.text_input("Enter an email address to check:")

if st.button("Check Breaches"):
    if not validate_email(email):
        st.error("Invalid email format. Please enter a valid email.")
    else:
        api_key = os.getenv("EMAIL_API_KEY")
        if not api_key:
            st.error("API key not found. Please set the EMAIL_API_KEY environment variable.")
        else:
            st.info(f"Checking breaches for {email}...")
            result = check_email_breach(api_key, email)
            if isinstance(result, list):
                st.warning(f"The email address {email} was found in the following breaches:")
                for breach in result:
                    st.write(f"**{breach.get('Title', 'Unknown')} ({breach.get('BreachDate', 'N/A')})**")
                    st.write(f"Domain: {breach.get('Domain', 'Unknown')}")
                    st.write(breach.get('Description', 'No description available.'))
                    st.write(breach)
                st.info("Recommendations: Change your passwords and enable MFA!")
            elif result is None:
                st.success(f"Good news! The email address {email} was not found in any known breaches.")
            else:
                st.error(f"An error occurred: {result}")