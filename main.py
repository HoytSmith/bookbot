
def read_book(book_path):
    with open(book_path) as book:
        book_text = book.read()
        return book_text

def count_words(text):
    word_tokens = text.split()
    return len(word_tokens)

def count_characters(text):
    character_data = {}
    for c in text.lower():
        if c.isalpha():
            if c in character_data:
                character_data[c] += 1
            else:
                character_data[c] = 1
    return character_data

def reorder_character_data(character_data):
    reordered_data = {}
    while len(character_data) > 0:
        highest_character = ''
        highest_value = 0
        for c in character_data:
            if character_data[c] > highest_value:
                highest_character = c
                highest_value = character_data[c]
        else:
            reordered_data[highest_character] = highest_value
            character_data.pop(highest_character)
    return reordered_data

def nice_print(file, word_count, character_data):
    print("--- Begin report of "+file+" ---")
    print(str(word_count)+" words found in the document")
    print("\n")
    for c in character_data:
        print("The '"+c+"' character was found "+str(character_data[c])+" times")

def main():
    book_file = "books/frankenstein.txt"
    book_text = read_book(book_file)
    word_count = count_words(book_text)
    character_count = count_characters(book_text)
    ordered_character_data = reorder_character_data(character_count)
    nice_print(book_file, word_count, ordered_character_data)

main()