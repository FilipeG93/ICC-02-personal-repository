# first_python_script.py
# My first Python script for cybersecurity class
# This script reads and writes names to a file

# keep running until user chooses to exit
while True:
    print("---- MENU ----")
    print("1) Read and display names")
    print("2) Add a new name")
    print("3) Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            file = open("names.txt", "r")
            print("\n--- Names in the file ---")
            for line in file:
                print(line.strip())
            file.close()
            print("--------------------------\n")
        except:
            print("Error: could not read the file. Maybe it doesn't exist?\n")

    elif choice == "2":
        new_name = input("Enter the new name to add: ")
        try:
            file = open("names.txt", "a")
            file.write(new_name + "\n")
            file.close()
            print("Name added!\n")
        except:
            print("Error: could not write to the file.\n")

    elif choice == "3":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice, please try again.\n")
