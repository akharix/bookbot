def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    lowered_string = get_lowered_string(text)
    character_count = get_alphabet_character_count(lowered_string)
    sorted_character_count = get_sorted_character_count(character_count)
    print_report(sorted_character_count, num_words, book_path)

def print_report(sorted_character_count, num_words, book_path):
    print("--- Begin report of", book_path,"---")
    print(num_words, "words was found in the document")
    print("")
    for key, value in sorted_character_count.items():
        print(f"The '{key}' character was found {value} times")
    print("--- End report ---")

def get_sorted_character_count(character_count):
    sorted_list_character_count = sorted(character_count.items(), key=lambda item: item[1], reverse = True)
    return dict(sorted_list_character_count)

def get_alphabet_character_count(lowered_string):
    character_count = {}
    for character in lowered_string:
        if character.isalpha():
            if character in character_count:
                character_count[character] += 1
            else:
                character_count[character] = 1
    return character_count

def get_lowered_string(text):
    lowered_string = text.lower()
    return lowered_string

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
