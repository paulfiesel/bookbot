def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_dict = get_dict_list(chars_dict)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    for i in sorted_dict[:26]:
        print(f"The '{i[0]}' character was found {i[1]} times")
    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered.isalpha():
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars


def get_dict_list(chars_dict):
    dict_list = list(chars_dict.items())
    dict_list.sort(key=lambda item: item[1], reverse=True)
    return dict_list


main()
