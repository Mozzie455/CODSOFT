#!/usr/bin/python3

"""
This module tests the password generator functionality
"""
# Import pytest ,string  and generator module
import pytest
import string
from src.generator import generate_password


# Test different password lengths
@pytest.fixture(params=[6, 8, 10])
def password_length(request):
    """
    Fixture to provide different password lengths for testing
    """
    return request.param


@pytest.fixture
def valid_characters():
    """
    Fixture to provide valid characters for password generation
    """
    return string.ascii_letters + string.digits + string.punctuation


def test_generate_password_length(password_length):
    """
    Test if the generated password has the correct length.
    """
    password = generate_password(password_length)
    assert len(password) == password_length


def test_generate_password_valid_characters(password_length, valid_characters):
    """
    Test all characters in the generated password belongs to set of valid characters.
    """
    password = generate_password(password_length)
    for char in password:
        assert char in valid_characters


def test_generate_password_raises_value_error_for_negative_length():
    """
    Test if the function raises a ValueError when given a negative length.
    """
    with pytest.raises(ValueError):
        generate_password(-1)


def test_generate_password_raises_value_error_for_non_positive_length():
    """
    Test for ValueError when given a non-positive length.
    """
    with pytest.raises(ValueError):
        generate_password(0)
    with pytest.raises(ValueError):
        generate_password(-1)


def test_generate_password_raises_type_error_for_non_integer_length():
    """
    Test for TypeError when given a non-interger length.
    """
    with pytest.raises(TypeError):
        generate_password("length")


@pytest.mark.parametrize("length", [0, 1, 2,])
def test_generate_password_length_minimum(length):
    """
    Test the edge cases for minimum lengths.
    """
    password = generate_password(length)
    assert len(password) == length
