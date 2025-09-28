def word_count(book_text):
    splitted = book_text.split()
    num_words = 0
    for word in splitted:
        num_words += 1

    return f"Found {num_words} total words"

def char_count(book_text):
    print("### CHAR_COUNT DEBUG ###")
    char_obj = {}

    # add each unique value (lowercased) to the object
    for char in book_text:
        c = char.lower()
        if not c in char_obj:
            char_obj[c] = 0
        char_obj[c] += 1

    print("CHECKS")
    print(f"t: {char_obj['t']}")
    print(f"p: {char_obj['p']}")
    print(f"c: {char_obj['c']}")
    print("#########################")
    return char_obj
