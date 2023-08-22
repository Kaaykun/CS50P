import random


def get_level():
    """Prompts the user for a positive integer"""
    while True:
        try:
            level = int(input("Level: "))
            if level < 1:
                continue
            return level
        except ValueError:
            continue


def random_number(level):
    """Generates a random number between 1 and 'level' input"""
    return random.randint(1, level)


def check_guess(solution):
    """Repromts user until guess is correct and prints hints"""
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 1:
                continue

            if guess > solution:
                print("Too large!")
                continue
            elif guess < solution:
                print("Too small!")
                continue
            return "Just right!"

        except ValueError:
            continue


def main():
    """Main function to execute the program"""
    level = get_level()
    solution = random_number(level)
    print(check_guess(solution))


if __name__ == "__main__":
    main()
