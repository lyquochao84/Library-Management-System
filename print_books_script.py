from classes.library import Library
from classes.book import Book

def main():
    # Create a Library instance
    library = Library()

    # Add some books to the library
    book1 = Book(isbn="12345", title="The Great Gatsby", author="F. Scott Fitzgerald", genre="Fiction", available=3)
    book2 = Book(isbn="67890", title="To Kill a Mockingbird", author="Harper Lee", genre="Fiction", available=2)

    library.add_book(book1)
    library.add_book(book2)

    # Print out all books
    print("Books in the Library:")
    for isbn, book in library.books.items():
        print(f"ISBN: {book.isbn}, Title: {book.title}, Author: {book.author}, Genre: {book.genre}, Available: {book.available}")

if __name__ == "__main__":
    main()
