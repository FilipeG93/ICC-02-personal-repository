# secure_message_basic.py
# Task 5.1: Secure Messaging System
# Name: [Your Name]
# Date: [Date]

# This program lets you make a secret key, encrypt a message, or decrypt a message

from cryptography.fernet import Fernet

print("=== Secure Messaging System ===")
print("1 = Make Key")
print("2 = Encrypt Message")
print("3 = Decrypt Message")
choice = input("Choose what to do (1/2/3): ")

# make a key
if choice == "1":
    key = Fernet.generate_key()
    with open("key.key", "wb") as file:
        file.write(key)
    print("Key made and saved as key.key")

# encrypt a message
elif choice == "2":
    with open("key.key", "rb") as file:
        key = file.read()

    f = Fernet(key)
    message = input("Type your message: ")
    encrypted = f.encrypt(message.encode())
    print("Encrypted message:")
    print(encrypted.decode())

# decrypt a message
elif choice == "3":
    with open("key.key", "rb") as file:
        key = file.read()

    f = Fernet(key)
    encrypted_text = input("Paste encrypted message: ").encode()
    decrypted = f.decrypt(encrypted_text)
    print("Decrypted message:")
    print(decrypted.decode())

else:
    print("Invalid choice.")
