#!/usr/bin/python3

"""
This module provides the password generator functionality.
"""

# Import secrets and string module
import secrets
import string

"""
TODO: Create password generator, customize length & complexity.
"""


# Define a function to generate a password of specified length
def generate_password(length):
    """
    Generate a password of the specified length.

    Args:
        length (int): The length of the password to generate.

    Returns:
        str: The generated password.

    Raises:
        ValueError: If length is less than or equal to 0.
    """
    if length <= 0:
        raise ValueError("Length must be greater than 0")
    # Get characters from Lower Case and Upper Case letters
    characters = string.ascii_letters + string.digits + string.punctuation

    # Initialize an empty list to store secret chosen characters
    secret_chars = []

    for i in range(length):
        # Choose a secret character from the 'characters'
        secret_char = secrets.choice(characters)
        # Append the chosen character to the list of secret characters
        secret_chars.append(secret_char)
    # Join the list of secret characters into a single string
    password = ''.join(secret_chars)
    return password
