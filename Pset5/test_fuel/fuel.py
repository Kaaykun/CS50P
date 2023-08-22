def main():
    fuel = input("Fraction: ")
    percentage = convert(fuel)
    print(gauge(percentage))

def convert(fuel):
    while True:
        try:
            x, y = fuel.split("/")
            x, y, = int(x), int(y)
            fraction = x / y
            if fraction <= 1:
                return int(round(fraction * 100))
            else:
                fuel = input("Fraction: ")
                pass
            
        except (ValueError, ZeroDivisionError):
            raise

def gauge(n):
    if n >= 99:
        return f"F"
    elif n <= 1:
        return f"E"
    else:
        return f"{n}%"

if __name__ == '__main__':
    main()