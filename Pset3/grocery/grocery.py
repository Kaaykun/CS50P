def main():

    grocery = {}


    while True:
        try:
            item = input("").upper()

            if item in grocery:
                grocery[item] += 1
            else:
                # Alternative command: d.setdefault(key, 1) -> grocery.setdefault(item, 1)
                grocery.update({item: 1})

        # control-d is a common way of ending input to a program - EOFError catches this cancelling and reacts accordingly
        except EOFError:
            # Print an empty line for readability
            print()
            # Sort the dictionary by its keys and loop over each sorted key
            for key in sorted(grocery.keys()):
                # Print each dict entry "VALUE KEY"
                print(f"{grocery[key]} {key}")
            break

if __name__ == '__main__':
    main()