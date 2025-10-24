# first_python_script.py
# My first Python script for cybersecurity class

print("1) Read and display names")
print("2) Add a new name")
print("3) Exit")

choice = input("Enter your choice: ")

if choice == "1":
    file = open("names.txt", "r")
    print("\n--- Names in the file ---")
    for line in file:
        print(line.strip())
    file.close()

elif choice == "2":
    new_name = input("Enter the new name to add: ")
    file = open("names.txt", "a")
    file.write(new_name + "\n")
    file.close()
    print("Name added!")

elif choice == "3":
    print("Exiting program. Goodbye!")

else:
    print("Invalid choice.")
