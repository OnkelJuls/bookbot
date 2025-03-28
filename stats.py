from itertools import count
def count_words(text):
    words = text.split()
    return len(words)

def count_characters(words):
    lower_words = words.lower()
    unique = set(lower_words)
    char_count = {}
    for char in unique:
        char_count[char] = lower_words.count(char)
    return char_count

def count_list(yup):
    dictionary_list = []
    for key, value in yup.items():
        dictionary_list.append({"char": key, "count" : value})
    dictionary_list.sort(key=lambda item: item["count"], reverse=True)
    return dictionary_list
