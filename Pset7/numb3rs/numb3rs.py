import re

def main():
    # Expected input "#.#.#.#", where # between 0 and 255, inclusive
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    """Validate the input string"""
    # Limit input "#.#.#.#", where # between between 1 and 3 decimal digits separated by "."
    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        numbers = ip.split(".")
        for number in numbers:
            if int(number) < 0 or int(number) > 255:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()