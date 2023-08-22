def main():
    fruits = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 60,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80
    }
    # Get user input in lowercase
    item = input("Input: ").lower()

    # Loop through fruits in dictionary
    for key in fruits:
        # Find the fruit requested in user input
        if key == item:
            print("Calories:", fruits[key])



if __name__ == '__main__':
    main()