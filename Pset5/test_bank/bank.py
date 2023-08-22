def main():
    greeting = input("Greeting: ")
    amount = value(greeting)
    print(f"${amount}")

def value(greeting):
    if greeting.lower().startswith("hello"):
        return 0
    elif greeting.lower().startswith("h", 0, 1):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()