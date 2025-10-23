# secure_file_basic.py
# Task 5.2: Secure File Encryption
# Name: [Your Name]
# Date: [Date]

# This program encrypts and decrypts files using a key

from cryptography.fernet import Fernet

print("=== Secure File Encryption ===")
print("1 = Make Key")
print("2 = Encrypt File")
print("3 = Decrypt File")
choice = input("Choose what to do (1/2/3): ")

# make a key
if choice == "1":
    key = Fernet.generate_key()
    with open("key.key", "wb") as file:
        file.write(key)
    print("Key made and saved as key.key")

# encrypt a file
elif choice == "2":
    with open("key.key", "rb") as file:
        key = file.read()

    f = Fernet(key)

    filename = input("Enter the name of the file to encrypt: ")

    with open(filename, "rb") as file:
        data = file.read()

    encrypted = f.encrypt(data)

    new_name = filename + ".encrypted"
    with open(new_name, "wb") as file:
        file.write(encrypted)

    print("File encrypted and saved as", new_name)

# decrypt a file
elif choice == "3":
    with open("key.key", "rb") as file:
        key = file.read()

    f = Fernet(key)

    filename = input("Enter the name of the file to decrypt: ")

    with open(filename, "rb") as file:
        data = file.read()

    decrypted = f.decrypt(data)

    new_name = filename.replace(".encrypted", ".decrypted")
    with open(new_name, "wb") as file:
        file.write(decrypted)

    print("File decrypted and saved as", new_name)

else:
    print("Invalid choice.")
