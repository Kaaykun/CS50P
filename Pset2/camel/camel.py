def main():
    camel_case = input("camelCase: ")
    snake_case = convert_to_snake_case(camel_case)
    print("snake_case:", snake_case)

def convert_to_snake_case(camel_case):
    # Create empty string variable for concatenation
    snake_case = ""
    # For each character in the user input
    for c in camel_case:
        # Check if its uppercase
        if c.isupper():
            # Concatenate _ + current character
            snake_case += "_" + c.lower()
        # If its not upper case
        else:
            # Concatenate current character
            snake_case += c
    return snake_case

if __name__ == '__main__':
    main()
