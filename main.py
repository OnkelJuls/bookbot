# from collections import Counter
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    character_count = get_character_count(text)
    print(f"{word_count} words found in the document")
    print(character_count)

def get_character_count(text):
    lowered_text = text.lower()
    # return Counter(lowered_text)
    dict = {}
    for x in lowered_text:
        dict[x] = dict.get(x, 0) + 1
    return dict

def get_word_count(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()