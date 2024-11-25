
def read_book(book_path):
    with open(book_path) as book:
        book_text = book.read()
        return book_text

def count_words(text):
    word_tokens = text.split()
    return len(word_tokens)

def main():
    book_text = read_book("books/frankenstein.txt")
    word_count = count_words(book_text)
    print(word_count)

main()