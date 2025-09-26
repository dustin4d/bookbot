def get_book_text(file):
    with open("books/frankenstein.txt") as f:
        contents_as_string = f.read()

    return contents_as_string

def main():
    print(get_book_text("./books/frankenstein.txt"))


main()
