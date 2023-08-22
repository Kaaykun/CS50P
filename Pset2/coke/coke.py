def main():

    coins = [5, 10, 25]
    amount_due = 50

    while amount_due > 0:
        print("Amount Due:", amount_due)

        while True:
            amount_insert = int(input("Insert Coin: "))
            if amount_insert in coins:
                break
            else:
                print("Amount Due:", amount_due)

        amount_due -= amount_insert

    print("Change Owed:", abs(amount_due))


if __name__ == '__main__':
    main()