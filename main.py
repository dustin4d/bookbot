import sys
from stats import word_count
from stats import char_count
from stats import sort_char_counts

def main():

    total_args = len(sys.argv)
    if total_args < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else: 
        filename = sys.argv[1]
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filename}")
        print("----------- Word Count ----------")
        print(word_count(get_book_text(filename)))
        print("--------- Character Count -------")
        print(sort_char_counts(char_count(get_book_text(filename))))

def get_book_text(file):
    with open(file) as f:
        book_text = f.read()

    return book_text

main()