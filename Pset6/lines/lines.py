import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    print(count_lines())


def count_lines():
    counter = 0
    try:
        with open(sys.argv[1]) as file:
            for line in file:
                if line.isspace() or line.strip().startswith("#"):
                    pass
                else:
                    counter += 1
        return counter
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()