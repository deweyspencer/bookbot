from stats import get_num_words, get_character_count, get_sorted_list

filename = "books/frankenstein.txt"

def get_book_text(file):
    with open(file) as f:
        return f.read()

def print_report(booktext):
    word_count = get_num_words(booktext)
    sorted_list = get_sorted_list(get_character_count(booktext))
 
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filename}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for entry in sorted_list:
        print (f"{entry['char']}: {entry['num']}")
    print("============= END ===============")

def main():
    booktext = get_book_text(filename)
    print_report(booktext)

main()