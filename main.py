
def read_book(book_path):
    with open(book_path) as book:
        book_text = book.read()
        print(book_text)

def main():
    read_book("books/frankenstein.txt")

main()