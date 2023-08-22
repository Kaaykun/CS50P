def main():
    greeting = input("Greeting: ").strip().lower()

    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h", 0, 1):
        print("$20")
    else:
        print("$100")

main()