import sys
from stats import get_num_words, get_character_count, get_sorted_list

def get_book_text(file):
    with open(file) as f:
        return f.read()

def print_report(booktext):
    word_count = get_num_words(booktext)
    sorted_list = get_sorted_list(get_character_count(booktext))
 
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for entry in sorted_list:
        print (f"{entry['char']}: {entry['num']}")
    print("============= END ===============")

def main():
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    booktext = get_book_text(sys.argv[1])
    print_report(booktext)

main()