def is_valid_date_1(input_date):
    """Returns True if the input_date is in the format Month DD, YYYY and is a valid date, and False otherwise"""
    try:
        # Condition check for year anno Domini, months per year and days per month
        month, day, year = map(int, input_date.split("/"))
        if 1 <= month <= 12 and 1 <= day <= 31 and year > 0:
            return True
        else:
            return False
    except ValueError:
        return False

def is_valid_date_2(input_date, months):
    """Prompts the user for a valid date and returns the year, month, and day in YYYY-MM-DD format"""
    try:
        month, day, year = input_date.split()
        # First index in a list is "0", adding 1 prevents error (e.g. January = 0 + 1)
        month = int(months.index(month) + 1)
        # "[:-1]" because the "," needs to be removed
        day = int(day[:-1])
        year = int(year)
        # Condition check for year anno Domini, months per year and days per month
        if 1 <= month <= 12 and 1 <= day <= 31 and year > 0:
            return True
        else:
            return False
    except ValueError:
        return False

def get_valid_date(months):
    """Prompts the user for a valid date and returns the year, month, and day in YYYY-MM-DD format"""
    while True:
            input_date = input("Date: ")
            # First possible user input (e.g. 6/21/1996)
            if "/" in input_date and is_valid_date_1(input_date) == True:
                month, day, year = map(int, input_date.split("/"))
                break

            # Second possible user input (e.g. June 21, 1996)
            elif "/" not in input_date and is_valid_date_2(input_date, months) == True:
                month, day, year = input_date.split()
                # First index in a list is "0", adding 1 prevents error (e.g. January = 0 + 1)
                month = int(months.index(month) + 1)
                # "[:-1]" because the "," needs to be removed
                day = int(day[:-1])
                year = int(year)
                break

    return f"{year:04d}-{month:02d}-{day:02d}"

def main():
    """Main function to execute the program"""
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

    output_date = get_valid_date(months)
    print(output_date)


if __name__ == '__main__':
    main()