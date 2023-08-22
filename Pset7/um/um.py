import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    """Count occurances of "um" in a text"""
    matches = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(matches)


if __name__ == "__main__":
    main()