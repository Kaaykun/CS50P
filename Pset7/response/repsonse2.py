from validator_collection import validators, errors
import sys


def main():
    email = input("What's your email? ")
    try:
        validators.email(email)
        print("Valid")
    except errors.EmptyValueError:
        sys.exit("Invalid")
    except errors.InvalidEmailError:
        sys.exit("Invalid")


if __name__ == "__main__":
    main()