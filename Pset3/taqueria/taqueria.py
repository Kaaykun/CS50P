def main():

    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total_price = 0.00

    while True:
        try:
            item = input("Item: ").title()
            # Check if input matches any of the key values in the menu
            if item in menu:
                # Add price of the item in the menu to Total
                total_price += menu[item]
                # Print the current total, formatted to 2 decimal points
                print(f"Total: ${total_price:.2f}",)
            else:
                pass
        # control-d is a common way of ending input to a program - EOFError catches this cancelling and reacts accordingly
        except EOFError:
            print()
            break

if __name__ == '__main__':
    main()