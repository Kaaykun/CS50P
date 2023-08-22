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
    # Converts the time string (format "hh:mm") to a float
    hours, minutes = map(float, time_str.split(":"))
    return hours + minutes / 60

if __name__ == "__main__":
    main()