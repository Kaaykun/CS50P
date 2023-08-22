import inflect

def main():
    p = inflect.engine()
    people = []

    while True:
        try:
            name = input("Name: ").title().strip()
            people.append(name)

        except EOFError:
            print()
            print("Adieu, adieu, to", p.join(people))
            break

if __name__ == '__main__':
    main()