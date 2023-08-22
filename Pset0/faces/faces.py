def main ():
    message = input("")
    print(converter(message))


def converter(message):
    # Separate message where there is a " " and return the words as a list
    words = message.split(" ")
    # Define dictionary containing the special characters that shall be converted to emojis
    emojis = {
        ":)" : "🙂",
        ":(" : "🙁"
    }
    # Define variable to store converted message
    output = ""
    # Iterate through all words in the message
    for word in words:
        # Return and emoji if the word (e.g. ":)" is found in the dictionary, otherwise return the word itself as default
        output += emojis.get(word, word) + " "
    return output

main()