# super_basic_multi_file.py
# Bonus Challenge: Encrypt or Decrypt Many Files
# Name: [Your Name]
# Date: [Date]

# this program can make a key, encrypt many files, or decrypt many files

from cryptography.fernet import Fernet

print("Welcome to my multi-file encryption program!")
print("1 = make a key")
print("2 = encrypt files")
print("3 = decrypt files")
choice = input("What do you want to do? ")

if choice == "1":
    # make a key
    key = Fernet.generate_key()
    file = open("key.key", "wb")
    file.write(key)
    file.close()
    print("Key made and saved in key.key file!")

elif choice == "2":
    # encrypt many files
    file = open("key.key", "rb")
    key = file.read()
    file.close()

    f = Fernet(key)

    print("Type the names of the files to encrypt (put a space between each one):")
    files = input("Files: ").split()  # turns input into a list of names

    for name in files:
        print("Encrypting", name, "...")
        file = open(name, "rb")
        data = file.read()
        file.close()

        encrypted = f.encrypt(data)

        new_name = name + ".encrypted"
        file = open(new_name, "wb")
        file.write(encrypted)
        file.close()

        print("Saved as", new_name)

    print("All files encrypted!")

elif choice == "3":
    # decrypt many files
    file = open("key.key", "rb")
    key = file.read()
    file.close()

    f = Fernet(key)

    print("Type the names of the files to decrypt (put a space between each one):")
    files = input("Files: ").split()

    for name in files:
        print("Decrypting", name, "...")
        file = open(name, "rb")
        data = file.read()
        file.close()

        decrypted = f.decrypt(data)

        new_name = name.replace(".encrypted", ".decrypted")
        file = open(new_name, "wb")
        file.write(decrypted)
        file.close()

        print("Saved as", new_name)

    print("All files decrypted!")

else:
    print("Sorry, I don’t understand that choice.")
