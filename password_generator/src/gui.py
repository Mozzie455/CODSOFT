#!/usr/bin/python3

import tkinter as tk
from tkinter import messagebox
from src.generator import generate_password


def generate_password_callback():
    try:
        length = int(length_entry.get())
        password = generate_password(length)
        password_label.config(text=f"Generated Password: {password}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))


# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create a label for password length
length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=5)

# Create an entry field for password length
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=5)

# Create a button to generate the password
generate_button = tk.Button(
    root, text="Generate Password", command=generate_password_callback)
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

# Create a label to display the generated password
password_label = tk.Label(root, text="")
password_label.grid(row=2, column=0, columnspan=2, padx=10, pady=5)
