from string import ascii_lowercase

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    num_chars = count_char(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    for char in num_chars:
        print(f"The '{char}' character was found {num_chars[char]} times")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    print(words)
    return len(words)

def count_char(text):
    alphabet = ascii_lowercase
    char_dict = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if not char in alphabet:
            continue
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    sorted_char_dict = dict(sorted(char_dict.items()))
    return sorted_char_dict


main()