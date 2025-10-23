# super_basic_gui_encrypt.py
# Bonus Challenge: Simple GUI Encryption
# Name: [Your Name]
# Date: [Date]

# this program lets you make a key, encrypt a file, or decrypt a file using buttons

from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# make a window
window = tk.Tk()
window.title("Simple Encryption Program")
window.geometry("400x250")

# make a key
def make_key():
    key = Fernet.generate_key()
    file = open("key.key", "wb")
    file.write(key)
    file.close()
    messagebox.showinfo("Key", "Key made and saved as key.key!")

# encrypt one file
def encrypt_file():
    try:
        file = open("key.key", "rb")
        key = file.read()
        file.close()
    except:
        messagebox.showerror("Error", "No key found! Make one first.")
        return

    f = Fernet(key)

    filename = filedialog.askopenfilename(title="Choose a file to encrypt")
    if filename == "":
        return

    file = open(filename, "rb")
    data = file.read()
    file.close()

    encrypted = f.encrypt(data)

    new_name = filename + ".encrypted"
    file = open(new_name, "wb")
    file.write(encrypted)
    file.close()

    messagebox.showinfo("Done", "File encrypted and saved as:\n" + new_name)

# decrypt one file
def decrypt_file():
    try:
        file = open("key.key", "rb")
        key = file.read()
        file.close()
    except:
        messagebox.showerror("Error", "No key found! Make one first.")
        return

    f = Fernet(key)

    filename = filedialog.askopenfilename(title="Choose a file to decrypt")
    if filename == "":
        return

    file = open(filename, "rb")
    data = file.read()
    file.close()

    decrypted = f.decrypt(data)

    new_name = filename.replace(".encrypted", ".decrypted")
    file = open(new_name, "wb")
    file.write(decrypted)
    file.close()

    messagebox.showinfo("Done", "File decrypted and saved as:\n" + new_name)

# buttons
make_key_button = tk.Button(window, text="Make Key", command=make_key, width=20)
encrypt_button = tk.Button(window, text="Encrypt File", command=encrypt_file, width=20)
decrypt_button = tk.Button(window, text="Decrypt File", command=decrypt_file, width=20)
exit_button = tk.Button(window, text="Exit", command=window.quit, width=20)

# place buttons
make_key_button.pack(pady=10)
encrypt_button.pack(pady=10)
decrypt_button.pack(pady=10)
exit_button.pack(pady=10)

# run window
window.mainloop()
