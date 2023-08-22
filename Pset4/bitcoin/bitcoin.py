import json
import requests
import sys


def is_valid_argument(argument):
    if len(argument) < 2:
        print("Missing command-line argument")
        return False
    elif argument[1].isalpha():
        print("Command-line argument is not a number")
        return False
    else:
        return True


def main():
    """Main function to execute the program"""
    if is_valid_argument(sys.argv) == False:
        sys.exit(1)

    amount = float(sys.argv[1])

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response_json = response.json()
        bitcoin = response_json["bpi"]["USD"]["rate_float"]

    except requests.RequestException:
        print("An error occured while making the request")
        sys.exit(1)
    print(f"${(amount * bitcoin):,.4f}")


if __name__ == "__main__":
    main()
