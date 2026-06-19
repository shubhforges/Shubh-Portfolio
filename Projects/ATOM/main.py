from engine import run
from utils.helpers import boot

def main():
    boot()
    print("ATOM Ready")

    while True:
        cmd = input("You: ").lower()

        if cmd in ["exit", "quit"]:
            print("Shutting down ATOM...")
            break

        print("ATOM:", run(cmd))

if __name__ == "__main__":
    main()
