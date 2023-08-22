import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):

    if matches := re.search(r"^(\d[0-2]?)(?::([0-5][0-9]))? (AM|PM) to (\d[0-2]?)(?::([0-5][0-9]))? (AM|PM)$", s):
        hour_1, hour_2 = int(matches.group(1)), int(matches.group(4))
        if matches.group(2) != None:
            minute_1 = int(matches.group(2))
        else:
            minute_1 = 0
        if matches.group(5) != None:
            minute_2 = int(matches.group(5))
        else:
            minute_2 = 0
        period_1, period_2 = matches.group(3), matches.group(6)

        if period_1 == "AM" and hour_1 == 12:
            hour_1 = 0
        elif period_1 == "PM" and hour_1 != 12:
            hour_1 = hour_1 + 12

        if period_2 == "AM" and hour_2 == 12:
            hour_2 = 0
        elif period_2 == "PM" and hour_2 != 12:
            hour_2 = hour_2 + 12

        return f"{hour_1:02d}:{minute_1:02d} to {hour_2:02d}:{minute_2:02d}"

    else:
        raise ValueError



if __name__ == "__main__":
    main()