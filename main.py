# from collections import Counter
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    character_count = get_character_count(text)
    sorted_character_list = sort_characters(character_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the book")
    print()

    for item in sorted_character_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def sort_on(d):
    return d['num']

def sort_characters(character_count):
    list_of_dict = []
    for char in character_count:
        list_of_dict.append({"char": char, "num": character_count[char]})
    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict

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