# simple_password_encrypt.py
# Bonus Challenge: Use password instead of key file
# Name: [Your Name]
# Date: [Date]

# This program encrypts and decrypts files using a password
# It uses PBKDF2 to make a key from your password (so no key file is needed)

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import base64

# make key from password
def make_key(password):
    salt = b"mysalt123"  # simple fixed salt for learning (in real life, use random salt)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key

# encrypt a file
def encrypt_file(filename, password):
    key = make_key(password)
    f = Fernet(key)

    with open(filename, "rb") as file:
        data = file.read()

    encrypted = f.encrypt(data)

    new_name = filename + ".encrypted"
    with open(new_name, "wb") as file:
        file.write(encrypted)

    print("✅ File encrypted and saved as:", new_name)

# decrypt a file
def decrypt_file(filename, password):
    key = make_key(password)
    f = Fernet(key)

    with open(filename, "rb") as file:
        data = file.read()

    try:
        decrypted = f.decrypt(data)
    except:
        print("❌ Wrong password or bad file!")
        return

    new_name = filename.replace(".encrypted", ".decrypted")
    with open(new_name, "wb") as file:
        file.write(decrypted)

    print("✅ File decrypted and saved as:", new_name)

# ---- MAIN PROGRAM ----
print("Simple Password Encryption Program")
print("----------------------------------")

choice = input("Do you want to (E)ncrypt or (D)ecrypt a file? ").lower()
filename = input("Enter file name (example: myfile.txt): ")
password = input("Enter your password: ")

if choice == "e":
    encrypt_file(filename, password)
elif choice == "d":
    decrypt_file(filename, password)
else:
    print("Invalid choice! Please type E or D.")
