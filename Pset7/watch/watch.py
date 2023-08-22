import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    """Parse the input string"""
    if matches := re.search(r"^.+((?:http|https)://(?:www\.)?youtube\.com/embed/(\w+)).+$", s, re.IGNORECASE):
        return f"https://youtu.be/{matches.group(2)}"
    else:
        return None


if __name__ == "__main__":
    main()