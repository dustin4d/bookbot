book_text = None
book_words = []

def get_book_text(file):
    with open("books/frankenstein.txt") as f:
        book_text = f.read()

    return book_text

# TODO fix this function
# it currently splits the text down by character
# it SHOULD split based on WORD
def word_count(book_text):
    num_words = 0
    splitted_text = book_text.split(' ')
    for word in book_text:
        book_words.append(word)
        num_words += 1
    print(book_words)

    return f"Found {num_words} total words"



def main():
#    This prints the whole book
#    print(get_book_text("./books/frankenstein.txt"))

    # this prints the word count
    print(word_count(get_book_text("./books/frankenstein.txt")))


main()
