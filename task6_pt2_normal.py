# secure_file.py
# Task 5.1: Secure File Encryption
# Author: [Your Name]

from cryptography.fernet import Fernet
import os

# === KEY MANAGEMENT ===
def write_key():
    """Generate and save a new Fernet key"""
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    print("[+] Key generated and saved to key.key")

def load_key():
    """Load the existing Fernet key"""
    return open("key.key", "rb").read()

# === FILE ENCRYPTION ===
def encrypt_file(filename):
    """Encrypt the specified file and save it as filename.encrypted"""
    key = load_key()
    f = Fernet(key)

    with open(filename, "rb") as file:
        original_data = file.read()

    encrypted_data = f.encrypt(original_data)

    encrypted_filename = filename + ".encrypted"
    with open(encrypted_filename, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

    print(f"[+] File '{filename}' encrypted and saved as '{encrypted_filename}'")

# === FILE DECRYPTION ===
def decrypt_file(encrypted_filename):
    """Decrypt an encrypted file and save it as filename.decrypted"""
    key = load_key()
    f = Fernet(key)

    with open(encrypted_filename, "rb") as enc_file:
        encrypted_data = enc_file.read()

    decrypted_data = f.decrypt(encrypted_data)

    decrypted_filename = encrypted_filename.replace(".encrypted", ".decrypted")
    with open(decrypted_filename, "wb") as dec_file:
        dec_file.write(decrypted_data)

    print(f"[+] File '{encrypted_filename}' decrypted and saved as '{decrypted_filename}'")

# === MAIN ===
if __name__ == "__main__":
    print("=== Secure File Encryption System ===")
    choice = input("Do you want to (G)enerate key, (E)ncrypt, or (D)ecrypt? ").lower()

    if choice == 'g':
        write_key()

    elif choice == 'e':
        filename = input("Enter the file name to encrypt (with extension): ")
        if os.path.exists(filename):
            encrypt_file(filename)
        else:
            print("[-] File not found.")

    elif choice == 'd':
        filename = input("Enter the encrypted file name (with extension): ")
        if os.path.exists(filename):
            decrypt_file(filename)
        else:
            print("[-] File not found.")

    else:
        print("Invalid option.")
