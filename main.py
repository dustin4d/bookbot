from stats import word_count

def get_book_text(file):
    with open("books/frankenstein.txt") as f:
        book_text = f.read()

    return book_text

def main():
    print(word_count(get_book_text("./books/frankenstein.txt")))


main()
