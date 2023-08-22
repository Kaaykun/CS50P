from datetime import date, timedelta
import inflect
import operator
import sys
import re

p = inflect.engine()

def main():
    print(minutes_old(input("Date of Birth: ")).capitalize())


def minutes_old(input_date):
    """Calculate minutes since birthday"""
    # Create a variable with todays date in ISO format
    today = date.today()
    bday = check_date(input_date)
    # Overload minus operator and calculate delta of time
    td = operator.__sub__(today, bday)
    # Convert to minutes
    td_minutes = round(timedelta.total_seconds(td) / 60)
    # Transform from number into words
    words = p.number_to_words(td_minutes, andword="")
    return f"{words} minutes"


def check_date(input_date):
    """Validate input and convert to date in ISO format (YYYY-MM-DD)"""
    if matches := re.search(r"^(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})$", input_date):
        year, month, day = int(matches.group("year")), int(matches.group("month")), int(matches.group("day"))
        try:
            # Check for year in range(0001, 9999), month in range(01, 12), day in range(01-31)
            # Checks for correct amount of days per month, including February of leap years
            if date(year, month, day):
                return date.fromisoformat(input_date)
            raise ValueError
        except ValueError:
            sys.exit("Invalid date")
    sys.exit("Invalid date")


if __name__ == "__main__":
    main()