def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    # Check if first two chracters are alphabetic
    if not plate[:2].isalpha():
        return False

    # Check platelength
    if len(plate) < 2 or len(plate) > 6:
        return False

    # Function faulty - Should check for alphabet between digits
    # Currently only checking for last character digit
    digits_encountered = False
    for c in plate:
        if c.isdigit():
            digits_encountered = True
        elif digits_encountered and c.isalpha():
            return False

    # Check if the first number is not "0"
    for c in range(len(plate) - 1):
        if plate[c].isalpha() and plate[c + 1] == "0":
            return False

    # Check if punctuation is used
    if any(c in " ,.;:!?" for c in plate):
        return False

    return True

if __name__ == '__main__':
    main()