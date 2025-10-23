# secure_message.py
# Task 5.1: Secure Messaging System
# Author: [Your Name]

from cryptography.fernet import Fernet

# === 1. KEY GENERATION ===
def write_key():
    """Generates a new Fernet key and saves it to key.key"""
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    print("[+] Key generated and saved to key.key")

def load_key():
    """Loads the key from the current directory named `key.key`"""
    return open("key.key", "rb").read()

# === 2. MESSAGE ENCRYPTION ===
def encrypt_message(message):
    """Encrypts a plaintext message using the loaded Fernet key"""
    key = load_key()
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    print("[+] Message encrypted.")
    return encrypted_message

# === 3. MESSAGE DECRYPTION ===
def decrypt_message(encrypted_message):
    """Decrypts an encrypted message using the shared key"""
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    print("[+] Message decrypted.")
    return decrypted_message.decode()

# === MAIN FUNCTION ===
if __name__ == "__main__":
    print("=== Secure Messaging System ===")
    choice = input("Do you want to (G)enerate key, (E)ncrypt, or (D)ecrypt? ").lower()

    if choice == 'g':
        write_key()

    elif choice == 'e':
        msg = input("Enter your message: ")
        encrypted = encrypt_message(msg)
        print("Encrypted message (send this):")
        print(encrypted.decode())

    elif choice == 'd':
        encrypted_input = input("Paste the encrypted message: ").encode()
        decrypted = decrypt_message(encrypted_input)
        print("Decrypted message:")
        print(decrypted)

    else:
        print("Invalid option.")
