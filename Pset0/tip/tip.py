def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Remove the leading "$"
    # Return the value as a float
    input = d.removeprefix("$")
    dollars = float(input)
    return dollars

def percent_to_float(p):
    # Remove the trailing "%"
    # Return the value as a percantage float
    input = p.removesuffix("%")
    percent = (float(input) / 100)
    return percent


main()