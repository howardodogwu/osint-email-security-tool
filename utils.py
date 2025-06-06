import validators

def validate_email(email):
    """
    Validate the format of an email address.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email is valid, otherwise False.
    """
    return validators.email(email)
