import socket
import os
print("Network Info Tool v1.0")
print("Made by Shubh Chaudhary")
while True:
    print("\n=== Network Info Tool ===")
    print("1. Show Hostname")
    print("2. Show Local IP")
    print("3. Ping a Website")
    print("4. Trace Route")
    print("5. DNS Lookup")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Hostname:", socket.gethostname())

    elif choice == "2":
        print("Local IP:", socket.gethostbyname(socket.gethostname()))

    elif choice == "3":
        website = input("Website to ping: ")
        os.system(f"ping {website}")
        input("\nPress Enter to continue...")
        
    elif choice== "4":
        trace = input("Web or IP to trace:")
        os.system(f"tracert {trace}")
        input("\nPress Enter to continue...")

    elif choice == "5":
        domain = input("Enter domain: ")
        print("IP Address:", socket.gethostbyname(domain))
    

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid option!")
