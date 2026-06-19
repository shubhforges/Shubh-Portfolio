import random
import string

print("========================")
print(" PASSWORD GENERATOR ")
print("========================")

while True:
    length = int(input("\nEnter password length: "))

    print("\nChoose mode:")
    print("1. Letters only")
    print("2. Numbers only")
    print("3. Letters + Numbers + Symbols")

    mode = input("Enter choice (1/2/3): ")

    if mode == "1":
        characters = string.ascii_letters

    elif mode == "2":
        characters = string.digits

    elif mode == "3":
        characters = string.ascii_letters + string.digits + string.punctuation

    else:
        print("Invalid choice, defaulting to letters only.")
        characters = string.ascii_letters

    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("\nGenerated Password:")
    print(password)

    again = input("\nDo you want another password? (y/n): ")

    if again != "y":
        print("Goodbye!")
        break
