import os
from dotenv import load_dotenv
from email_api import check_email_breach
from utils import validate_email

load_dotenv()  # Load environment variables from .env

def main():
    """
    Entry point for the OSINT Email Security Tool.
    """
    # Get API key from environment variable
    api_key = os.getenv("EMAIL_API_KEY")
    if not api_key:
        print("API key not found. Please set the EMAIL_API_KEY environment variable.")
        return

    # Get email input from the user
    email = input("Enter an email address to check: ")

    # Validate email format
    if not validate_email(email):
        print("Invalid email format. Please enter a valid email.")
        return

    # Check for breaches
    print(f"Checking breaches for {email}...")
    result = check_email_breach(api_key, email)

    # Process and print results
    if isinstance(result, list):
        print(f"\nThe email address {email} was found in the following breaches:")
        for breach in result:
            print(f"- {breach['Title']} ({breach['BreachDate']})")
            print(f"  Details: {breach['Description']}\n")
        print("Recommendations: Change your passwords and enable MFA!")
    elif result is None:
        print(f"\nGood news! The email address {email} was not found in any known breaches.")
    else:
        print(f"\nAn error occurred: {result}")

if __name__ == "__main__":
    main()
