def main():
    # Ask for user input and convert it to a float
    time_str = input("What time is it? ")
    time = convert(time_str)

    # Check the time and print the corresponding message
    if 7.00 <= time <= 8.00:
        print("breakfast time")
    elif 12.00 <= time <= 13.00:
        print("lunch time")
    elif 18.00 <= time <= 19.00:
        print("dinner time")


def convert(time_str):
    # Is called if input is in 12h-"am/pm"-Format
    if "am" in time_str or "pm" in time_str:
        # Converts the time string to a float
        hours, minutes = map(float, time_str[:-2].split(":"))
        period = time_str[-2:]

        # Check for "pm" and add 12 hours, unless its noon,
        # to convert from 12h to 24h-Format
        if period == "pm" and hours != 12:
            hours += 12
        # Check if it is midnight (12am), and if it is,
        # set hours to 0 to convert from 12h to 24h-Format
        elif period == "am" and hours == 12:
            hours = 0

        return hours + minutes / 60

    # Is called when input is in 24h-format ("hh:mm")
    else:
        # Converts the time string to a float
        hours, minutes = map(float, time_str.split(":"))
        return hours + minutes / 60

if __name__ == "__main__":
    main()