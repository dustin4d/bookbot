def word_count(book_text):
    splitted = book_text.split()
    num_words = 0
    for word in splitted:
        num_words += 1

    return f"Found {num_words} total words"
