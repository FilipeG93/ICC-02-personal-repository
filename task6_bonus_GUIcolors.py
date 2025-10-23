# simple_gui_encrypt_pretty.py
# Bonus Challenge: Simple and Pretty GUI Encryption App
# Name: [Your Name]
# Date: [Date]

# This program lets you make a key, encrypt files, or decrypt files
# It uses simple buttons and colors to look nice and friendly :)

from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# make the window
window = tk.Tk()
window.title("My Encryption App")
window.geometry("420x320")
window.config(bg="#e6f2ff")  # light blue background

# title label
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

# encrypt file
def encrypt_file():
    try:
        with open("key.key", "rb") as file:
            key = file.read()
    except:
        messagebox.showerror("Error", "No key found! Please make one first.")
        return

    f = Fernet(key)
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
    status_label.config(text="File encrypted ✔️")

# decrypt file
def decrypt_file():
    try:
        with open("key.key", "rb") as file:
            key = file.read()
    except:
        messagebox.showerror("Error", "No key found! Please make one first.")
        return

    f = Fernet(key)
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
    status_label.config(text="File decrypted ✔️")

# buttons (with colors)
button_style = {"font": ("Arial", 12), "width": 20, "height": 1}

make_key_btn = tk.Button(window, text="🔑 Make Key", command=make_key, bg="#99ccff", **button_style)
encrypt_btn = tk.Button(window, text="🔐 Encrypt File", command=encrypt_file, bg="#66cc99", **button_style)
decrypt_btn = tk.Button(window, text="📂 Decrypt File", command=decrypt_file, bg="#ffcc66", **button_style)
exit_btn = tk.Button(window, text="❌ Exit", command=window.quit, bg="#ff9999", **button_style)

# place buttons
make_key_btn.pack(pady=5)
encrypt_btn.pack(pady=5)
decrypt_btn.pack(pady=5)
exit_btn.pack(pady=5)

# run window
window.mainloop()
