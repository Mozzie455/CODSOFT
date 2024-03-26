#!/usr/bin/python3

import pytest
from tkinter import Tk, Entry, Button, Label
from tkinter import messagebox
from src.generator import generate_password


# Fixture to set up and tear down the Tkinter application
@pytest.fixture
def app():
    root = Tk()
    yield root
    root.destroy()


# Test case to verify password generation with valid length
def test_generate_password_valid_length(app):
    # Set up GUI elements
    length_entry = Entry(app)
    length_entry.grid(row=0, column=1)

    generate_button = Button(app, text="Generate Password",
                             command=lambda: generate_password_callback(length_entry))
    generate_button.grid(row=1, column=0, columnspan=2)

    password_label = Label(app, text="")
    password_label.grid(row=2, column=0, columnspan=2)

    # Set password length and invoke generation
    length_entry.insert(0, "8")
    generate_button.invoke()

    # Verify that password label displays a password of correct length
    password = password_label.cget("text")
    assert password != ""
    assert len(password) == 8


# Test case to verify handling of invalid password length
def test_generate_password_invalid_length(app):
    # Set up GUI elements
    length_entry = Entry(app)
    length_entry.grid(row=0, column=1)

    generate_button = Button(app, text="Generate Password",
                             command=lambda: generate_password_callback(length_entry))
    generate_button.grid(row=1, column=0, columnspan=2)

    password_label = Label(app, text="")
    password_label.grid(row=2, column=0, columnspan=2)

    # Set invalid password length and invoke generation
    length_entry.insert(0, "-1")
    generate_button.invoke()

    # Verify that password label remains empty
    password = password_label.cget("text")
    assert password == ""


# Function to handle password generation callback
def generate_password_callback(length_entry, password_label):
    try:
        length = int(length_entry.get())
        password = generate_password(length)
        password_label.config(text=f"Generated Password: {password}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
