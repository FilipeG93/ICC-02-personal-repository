# simple_gui_encrypt_pbkdf2.py
# Bonus Challenge: GUI Encryption with Password Key (PBKDF2)
# Name: [Your Name]
# Date: [Date]

# This program encrypts and decrypts files using a password instead of a saved key.
# The password makes a key using PBKDF2HMAC.

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import base64
import os

# make the window
window = tk.Tk()
window.title("Password Encryption App")
window.geometry("450x350")
window.config(bg="#e6f2ff")

# title
title_label = tk.Label(window, text="🔐 Password-Based Encryption 🔐",
                       font=("Arial", 16, "bold"), bg="#e6f2ff", fg="#003366")
title_label.pack(pady=20)

# status
status_label = tk.Label(window, text="Ready", font=("Arial", 10), bg="#e6f2ff")
status_label.pack(side="bottom", pady=10)

# function to make a key from a password
def make_key_from_password(password):
    salt = b"mysalt123"  # In real life, this should be random and saved safely
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key

# encrypt one file
def encrypt_file():
    password = simpledialog.askstring("Password", "Enter your password:", show="*")
    if not password:
        return

    key = make_key_from_password(password)
    f = Fernet(key)

    filename = filedialog.askopenfilename(title="Choose a file to encrypt")
    if not filename:
        return

    with open(filename, "rb") as file:
        data = file.read()

    encrypted = f.encrypt(data)
    new_name = filename + ".encrypted"

    with open(new_name, "wb") as file:
        file.write(encrypted)

    messagebox.showinfo("Done", f"File encrypted as:\n{new_name}")
    status_label.config(text="File encrypted ✔️")

# decrypt one file
def decrypt_file():
    password = simpledialog.askstring("Password", "Enter your password:", show="*")
    if not password:
        return

    key = make_key_from_password(password)
    f = Fernet(key)

    filename = filedialog.askopenfilename(title="Choose a file to decrypt")
    if not filename:
        return

    with open(filename, "rb") as file:
        data = file.read()

    try:
        decrypted = f.decrypt(data)
    except:
        messagebox.showerror("Error", "Wrong password or corrupted file!")
        return

    new_name = filename.replace(".encrypted", ".decrypted")
    with open(new_name, "wb") as file:
        file.write(decrypted)

    messagebox.showinfo("Done", f"File decrypted as:\n{new_name}")
    status_label.config(text="File decrypted ✔️")

# buttons
button_style = {"font": ("Arial", 12), "width": 25, "height": 1}

encrypt_btn = tk.Button(window, text="🔐 Encrypt File", command=encrypt_file, bg="#66cc99", **button_style)
decrypt_btn = tk.Button(window, text="📂 Decrypt File", command=decrypt_file, bg="#ffcc66", **button_style)
exit_btn = tk.Button(window, text="❌ Exit", command=window.quit, bg="#ff9999", **button_style)

encrypt_btn.pack(pady=10)
decrypt_btn.pack(pady=10)
exit_btn.pack(pady=10)

# run window
window.mainloop()
