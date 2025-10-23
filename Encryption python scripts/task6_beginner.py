# secure_message_simple.py
# Task 5.1: Secure Messaging System
# Name: [Your Name]
# Date: [Date]

# This program lets two people send secret messages using encryption

from cryptography.fernet import Fernet

# make a new key and save it
def make_key():
    key = Fernet.generate_key()          # make a random key
    with open("key.key", "wb") as file:  # save it in a file
        file.write(key)
    print("Key made and saved as key.key")

# read the key from the file
def get_key():
    with open("key.key", "rb") as file:
        key = file.read()
    return key

# encrypt a message
def encrypt_message():
    key = get_key()
    f = Fernet(key)

    msg = input("Type your message: ")
    msg_bytes = msg.encode()             # turn text into bytes
    encrypted = f.encrypt(msg_bytes)

    print("Encrypted message (send this):")
    print(encrypted.decode())

# decrypt a message
def decrypt_message():
    key = get_key()
    f = Fernet(key)

    encrypted = input("Paste the encrypted message: ").encode()
    decrypted = f.decrypt(encrypted)

    print("Decrypted message:")
    print(decrypted.decode())

# main program
print("=== Secure Messaging System ===")
print("1. Make key")
print("2. Encrypt message")
print("3. Decrypt message")

choice = input("Choose what to do (1/2/3): ")

if choice == "1":
    make_key()
elif choice == "2":
    encrypt_message()
elif choice == "3":
    decrypt_message()
else:
    print("Invalid choice.")
