import random


def get_level():
    """Prompts the user for a positive integer between 1 and 3, inclusive"""
    while True:
        try:
            level = int(input("Level: "))
            if level not in (1, 2, 3):
                continue
            return level
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError


def main():
    """Main function to execute the program"""
    level = get_level()
    # Initiate variable to keep track of score
    score = 0
    # Initiate variable to keep track of questions asked
    question = 0

    while question < 10:
        # Initiate variable to keep track of attempts for right answer
        attempt = 0
        question += 1
        x = generate_integer(level)
        y = generate_integer(level)
        solution = x + y

        # Ask user for correct solution a maximum of 3 times
        while attempt < 3:
            try:
                user_solution = int(input(f"{x} + {y} = "))
                # Wrong answer is given
                if user_solution != solution:
                    print("EEE")
                    attempt += 1
                    pass
                # Correct answer is given
                else:
                    # Add a point to score
                    score += 1
                    break
            # Catch inputs that are not integers
            except ValueError:
                print("EEE")
                attempt += 1
                pass
        else:
            print(f"{x} + {y} = {solution}")

    print("Score:", score)


if __name__ == "__main__":
    main()
