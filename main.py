from stats import word_count
from stats import char_count
from stats import sort_char_counts

def get_book_text(file):
    with open("books/frankenstein.txt") as f:
        book_text = f.read()

    return book_text

def main():

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(word_count(get_book_text("./books/frankenstein.txt")))
    print("--------- Character Count -------")
    print(sort_char_counts(char_count(get_book_text("./books/frankenstein.txt"))))

main()
