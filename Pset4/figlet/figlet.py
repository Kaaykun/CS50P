import sys
import random
from pyfiglet import Figlet

"""
Command line input should be of len 0 or 2
If len == 0, random font will be chosen
If len == 2, then first input == "-f" or "--font" and seocond == "name of font"
"""

def main():
    figlet = Figlet()

    if len(sys.argv) > 3 or len(sys.argv) == 2:
        sys.exit("Invalid usage")
    elif len(sys.argv) == 3 and sys.argv[1] not in ("-f", "--font"):
        sys.exit("Invalid usage")
    elif len(sys.argv) == 3 and sys.argv[2] not in figlet.getFonts():
        sys.exit("Invalid usage")

    input_str = input("Input: ")

    if len(sys.argv) == 1:
        figlet.setFont(font=random.choice(figlet.getFonts()))
    else:
        figlet.setFont(font=sys.argv[2])

    print(figlet.renderText(input_str))


if __name__ == "__main__":
    main()