import requests

def check_email_breach(api_key, email):
    """
    Check if an email address appears in any data breaches using the HaveIBeenPwned API.

    Args:
        api_key (str): The HaveIBeenPwned API key.
        email (str): The email address to check.

    Returns:
        list or None: List of breaches (if found) or None if the email hasn't been breached.
    """
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {
        "hibp-api-key": api_key,
        "user-agent": "OSINT-Email-Security-Tool"
    }
    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()  # Return the list of breaches
        elif response.status_code == 404:
            return None  # No breaches found
        else:
            return f"Error: {response.status_code} - {response.reason}"
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
