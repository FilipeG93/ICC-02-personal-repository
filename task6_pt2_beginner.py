# secure_file_simple.py
# Task 5.2: Secure File Encryption
# Name: [Your Name]
# Date: [Date]

# This program encrypts and decrypts files using Fernet encryption

from cryptography.fernet import Fernet

# make a new key and save it
def make_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as file:
        file.write(key)
    print("Key made and saved as key.key")

# read the key from the file
def get_key():
    with open("key.key", "rb") as file:
        key = file.read()
    return key

# encrypt a file
def encrypt_file():
    key = get_key()
    f = Fernet(key)

    filename = input("Enter file name to encrypt: ")

    # read the file
    with open(filename, "rb") as file:
        data = file.read()

    # encrypt it
    encrypted = f.encrypt(data)

    # save it as new file
    new_name = filename + ".encrypted"
    with open(new_name, "wb") as file:
        file.write(encrypted)

    print("File encrypted and saved as", new_name)

# decrypt a file
def decrypt_file():
    key = get_key()
    f = Fernet(key)

    filename = input("Enter file name to decrypt: ")

    # read the encrypted file
    with open(filename, "rb") as file:
        data = file.read()

    # decrypt it
    decrypted = f.decrypt(data)

    # save as new file
    new_name = filename.replace(".encrypted", ".decrypted")
    with open(new_name, "wb") as file:
        file.write(decrypted)

    print("File decrypted and saved as", new_name)

# main menu
print("=== Secure File Encryption ===")
print("1. Make key")
print("2. Encrypt file")
print("3. Decrypt file")

choice = input("Choose what to do (1/2/3): ")

if choice == "1":
    make_key()
elif choice == "2":
    encrypt_file()
elif choice == "3":
    decrypt_file()
else:
    print("Invalid choice.")
