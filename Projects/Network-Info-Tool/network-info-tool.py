import socket
import os

def clear():
    os.system("cls")

def pause():
    input("\nPress Enter to return to menu...")

print("======================")
print("  NETWORK TOOL v1.5")
print("      By Shubh")
print("======================")

while True:
    print("\n--- MENU ---")
    print("1. Show Hostname")
    print("2. Show Local IP")
    print("3. DNS Lookup")
    print("4. Ping Website")
    print("5. Traceroute")
    print("6. Clear Screen")
    print("7. Exit")

    choice = input("\nEnter choice: ")

    # 1. Hostname
    if choice == "1":
        print("\n[HOSTNAME]")
        print(socket.gethostname())
        pause()

    # 2. Local IP
    elif choice == "2":
        print("\n[LOCAL IP]")
        print(socket.gethostbyname(socket.gethostname()))
        pause()

    # 3. DNS Lookup
    elif choice == "3":
        try:
            domain = input("Enter domain: ")
            print("\n[DNS RESULT]")
            print(socket.gethostbyname(domain))
        except:
            print("Invalid domain or no internet connection.")
        pause()

    # 4. Ping
    elif choice == "4":
        website = input("Website to ping: ")
        print("\n[PING RESULT]")
        os.system(f"ping {website}")
        pause()

    # 5. Traceroute
    elif choice == "5":
        trace = input("Enter website or IP: ")
        print("\n[TRACEROUTE]")
        os.system(f"tracert {trace}")
        pause()

    # 6. Clear Screen
    elif choice == "6":
        clear()

    # 7. Exit
    elif choice == "7":
        print("\nShutting down Network Tool...")
        break

    # Invalid input
    else:
        print("Invalid choice. Try again.")
        pause()
