def main():
    fuel = get_input()
    if fuel >= 99:
        print("F")
    elif fuel <= 1:
        print("E")
    else:
        print(f"{fuel}%")

def get_input():
    while True:
        try:
            # Get user input and split it into "x" and "y" at the location of "/"
            x, y = input("Fraction: ").split("/")
            x, y = int(x), int(y)
            if x <= y:
                # Calculate of fuel % in tank and return it as an int
                # Note that "/" operator always returns a "float", so "int" has to be delcared
                # Because the return value of "/" is a float, it has to be rounded before casting it to an int to remove rounding errors
                return int(round((x / y) * 100))
            else:
                pass
        except (ValueError, TypeError, ZeroDivisionError):
            pass

if __name__ == '__main__':
    main()