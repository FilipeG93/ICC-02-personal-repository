#!/usr/bin/env python3
# This script is only for simulation — do not use it on real systems without explicit permission.
# The ransomware features will only change the wallpaper and show a popup message. No actual harm will be done.


from cryptography.fernet import Fernet
import os
import ctypes
import tkinter as tk
from tkinter import messagebox

# Global variable for test folder
user_name = os.path.expanduser("~")
ransom_path = f"{user_name}\\OneDrive\\Desktop\\lab8folder"  # Windows path

# ---------------------------
#  Encryption Key Functions
# ---------------------------

def write_key():
    """Generate a key and save it to key.key"""
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    """Load the key from key.key file"""
    with open("key.key", "rb") as key_file:
        return key_file.read()

def if_key():
    """Check if key exists, generate if not"""
    if not os.path.exists("key.key"):
        print("Key not found. Generating new key...")
        key = write_key()
    else:
        key = load_key()
    return Fernet(key)

# ---------------------------
#  Encryption / Decryption
# ---------------------------

def encrypt_message():
    fernet = if_key()
    message = input("Enter a message to encrypt: ").encode()
    encrypted = fernet.encrypt(message)
    print(f"Encrypted message:\n{encrypted.decode()}")

def decrypt_message():
    fernet = if_key()
    token = input("Enter the encrypted message: ").encode()
    try:
        decrypted = fernet.decrypt(token)
        print(f"Decrypted message:\n{decrypted.decode()}")
    except Exception:
        print("Decryption failed. Wrong key or invalid token.")

def encrypt_file():
    fernet = if_key()
    file_path = input("Enter file path to encrypt: ")
    if not os.path.exists(file_path):
        print("File not found.")
        return
    with open(file_path, "rb") as f:
        data = f.read()
    encrypted = fernet.encrypt(data)
    with open(file_path, "wb") as f:
        f.write(encrypted)
    print(f"File {file_path} encrypted successfully!")

def decrypt_file():
    fernet = if_key()
    file_path = input("Enter file path to decrypt: ")
    if not os.path.exists(file_path):
        print("File not found.")
        return
    with open(file_path, "rb") as f:
        data = f.read()
    try:
        decrypted = fernet.decrypt(data)
        with open(file_path, "wb") as f:
            f.write(decrypted)
        print(f"File {file_path} decrypted successfully!")
    except Exception:
        print("Decryption failed. File may not be encrypted with this key.")

# ---------------------------
#  Ransomware Simulation
# ---------------------------

def ransomware_simulation():
    """Simulate ransomware by changing wallpaper and showing popup"""
    # 1. Create a ransom note image (simple text file as fake wallpaper)
    note_path = os.path.join(ransom_path, "ransom_note.txt")
    os.makedirs(ransom_path, exist_ok=True)
    with open(note_path, "w") as note:
        note.write("YOUR FILES HAVE BEEN ENCRYPTED!\n\n"
                   "This is a cybersecurity training simulation.\n"
                   "No real data was harmed.\n\n"
                   "-- Ethical Hacking Lab --")

    # 2. Change Windows wallpaper to the note (optional simulation)
    # You can use a real image path instead of a text file if desired.
    try:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, note_path, 3)
        print("Wallpaper changed to ransom note.")
    except Exception:
        print("Wallpaper change failed (may not be Windows).")

    # 3. Show popup window with ransom message
    root = tk.Tk()
    root.withdraw()  # Hide main window
    messagebox.showwarning(
        "RANSOMWARE SIMULATION",
        "⚠️ Your files have been encrypted!\n\n"
        "Don't panic — this is a training simulation.\n"
        "Use your decryption option to restore data."
    )
    root.destroy()

# ---------------------------
#  User Menu
# ---------------------------

def ask_user():
    mode = input(
        "\nWhat would you like to do?\n"
        "1 - Encrypt a message\n"
        "2 - Decrypt a message\n"
        "3 - Encrypt a file\n"
        "4 - Decrypt a file\n"
        "5 - Simulate ransomware attack\n"
        "6 - Exit\n"
        "Enter a number: "
    )

    if mode == "1":
        encrypt_message()
    elif mode == "2":
        decrypt_message()
    elif mode == "3":
        encrypt_file()
    elif mode == "4":
        decrypt_file()
    elif mode == "5":
        ransomware_simulation()
    elif mode == "6":
        print("Goodbye!")
        exit()
    else:
        print("Invalid selection.")

# ---------------------------
#  Main Program Loop
# ---------------------------

if __name__ == "__main__":
    while True:
        ask_user()
