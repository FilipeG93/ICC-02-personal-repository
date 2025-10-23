# simple_gui_encrypt_multi.py
# Bonus Challenge: GUI Encryption App with Multi-File Support
# Name: [Your Name]
# Date: [Date]

# This program lets you make a key, encrypt one file or many files, and decrypt them
# It is very simple and uses Tkinter for the buttons and messages

from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# make the window
window = tk.Tk()
window.title("My Encryption App")
window.geometry("450x380")
window.config(bg="#e6f2ff")  # light blue background

# title
title_label = tk.Label(window, text="🔒 Simple File Encryption 🔒", 
                       font=("Arial", 16, "bold"), bg="#e6f2ff", fg="#003366")
title_label.pack(pady=20)

# status label
status_label = tk.Label(window, text="Ready", font=("Arial", 10), bg="#e6f2ff")
status_label.pack(side="bottom", pady=10)

# make a key
def make_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as file:
        file.write(key)
    messagebox.showinfo("Key", "Key made and saved as key.key!")
    status_label.config(text="Key created ✔️")

# load the key (returns Fernet object)
def load_fernet():
    try:
        with open("key.key", "rb") as file:
            key = file.read()
        return Fernet(key)
    except:
        messagebox.showerror("Error", "No key found! Please make one first.")
        return None

# encrypt a single file
def encrypt_one():
    f = load_fernet()
    if f is None:
        return

    filename = filedialog.askopenfilename(title="Choose a file to encrypt")
    if filename == "":
        return

    with open(filename, "rb") as file:
        data = file.read()

    encrypted = f.encrypt(data)
    new_name = filename + ".encrypted"

    with open(new_name, "wb") as file:
        file.write(encrypted)

    messagebox.showinfo("Done", f"File encrypted and saved as:\n{new_name}")
    status_label.config(text="One file encrypted ✔️")

# decrypt a single file
def decrypt_one():
    f = load_fernet()
    if f is None:
        return

    filename = filedialog.askopenfilename(title="Choose a file to decrypt")
    if filename == "":
        return

    with open(filename, "rb") as file:
        data = file.read()

    decrypted = f.decrypt(data)
    new_name = filename.replace(".encrypted", ".decrypted")

    with open(new_name, "wb") as file:
        file.write(decrypted)

    messagebox.showinfo("Done", f"File decrypted and saved as:\n{new_name}")
    status_label.config(text="One file decrypted ✔️")

# encrypt multiple files
def encrypt_many():
    f = load_fernet()
    if f is None:
        return

    filenames = filedialog.askopenfilenames(title="Choose files to encrypt")
    if not filenames:
        return

    for name in filenames:
        with open(name, "rb") as file:
            data = file.read()
        encrypted = f.encrypt(data)
        new_name = name + ".encrypted"
        with open(new_name, "wb") as file:
            file.write(encrypted)

    messagebox.showinfo("Done", f"{len(filenames)} files encrypted successfully!")
    status_label.config(text=f"{len(filenames)} files encrypted ✔️")

# decrypt multiple files
def decrypt_many():
    f = load_fernet()
    if f is None:
        return

    filenames = filedialog.askopenfilenames(title="Choose files to decrypt")
    if not filenames:
        return

    for name in filenames:
        with open(name, "rb") as file:
            data = file.read()
        decrypted = f.decrypt(data)
        new_name = name.replace(".encrypted", ".decrypted")
        with open(new_name, "wb") as file:
            file.write(decrypted)

    messagebox.showinfo("Done", f"{len(filenames)} files decrypted successfully!")
    status_label.config(text=f"{len(filenames)} files decrypted ✔️")

# button style
button_style = {"font": ("Arial", 12), "width": 25, "height": 1}

# buttons
make_key_btn = tk.Button(window, text="🔑 Make Key", command=make_key, bg="#99ccff", **button_style)
encrypt_one_btn = tk.Button(window, text="🔐 Encrypt One File", command=encrypt_one, bg="#66cc99", **button_style)
encrypt_many_btn = tk.Button(window, text="🗂️ Encrypt Many Files", command=encrypt_many, bg="#66cc99", **button_style)
decrypt_one_btn = tk.Button(window, text="📂 Decrypt One File", command=decrypt_one, bg="#ffcc66", **button_style)
decrypt_many_btn = tk.Button(window, text="📁 Decrypt Many Files", command=decrypt_many, bg="#ffcc66", **button_style)
exit_btn = tk.Button(window, text="❌ Exit", command=window.quit, bg="#ff9999", **button_style)

# place buttons
make_key_btn.pack(pady=5)
encrypt_one_btn.pack(pady=5)
encrypt_many_btn.pack(pady=5)
decrypt_one_btn.pack(pady=5)
decrypt_many_btn.pack(pady=5)
exit_btn.pack(pady=5)

# run window
window.mainloop()
