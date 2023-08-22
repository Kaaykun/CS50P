import sys
from tabulate import tabulate

def main():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        file = open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File does not exist")

    table = []

    for line in file:
        pizza, small, large = line.rstrip().split(",")
        menu = {"pizza": pizza, "small": small, "large":large}
        table.append(menu)

    print(tabulate(table, headers="firstrow", tablefmt="grid"))


if __name__ == "__main__":
    main()