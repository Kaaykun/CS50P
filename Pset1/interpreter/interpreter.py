def main():
    # Ask for user input
    expression = input("Expression: ")

    # Split the input into three parts: two numbers and an operator
    x, symbol, y = expression.split()

    # Calculate the solution
    solution = interpreter(float(x), symbol, float(y))

    # Print the solution
    print(f"{solution:.1f}")


def interpreter(n1, symbol, n2):
    # Perform the appropriate operation based on the symbol
    if symbol == "+":
        return n1 + n2
    elif symbol == "-":
        return n1 - n2
    elif symbol == "*":
        return n1 * n2
    else:
        return n1 / n2

main()