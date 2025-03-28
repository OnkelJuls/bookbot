import sys
from stats import count_words, count_characters, count_list


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    unique_chars = count_characters(book_text)
    report_list = count_list(unique_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in report_list:
        if item["char"].isalpha():  # This ensures only alphabetical characters are included
            print(f"{item['char']}: {item['count']}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
