def main():
    original = input("Input: ")
    output = remove_vowels(original)
    print("Output:", output)

def remove_vowels(string):
    output = ""
    vowels = "aeiou"
    for c in string:
        if c.lower() not in vowels:
            output += c
    return output

if __name__ == '__main__':
    main()