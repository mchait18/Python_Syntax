def print_upper_words(words, must_start_with):
    """This function prints all words in Upper Case on separate lines."""
    for word in words:
        for char in must_start_with:
            if (word.startswith(char)):
                print(word.upper())
                break


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                  must_start_with={"h", "g"})
