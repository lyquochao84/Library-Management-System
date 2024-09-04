# Library
class Library:
    def __init__(self):
        self.books = {}
        self.users = {}
        self.track_books = {}

    def add_book(self, book):
        self.books[book.isbn] = book
        print(f"Added a new book name: {book.title} to the library")

    def remove_book(self, isbn):
        if isbn in self.books:
            del self.books[isbn]
            print(f"Removed book with ISBN {isbn}.")
        else:
            print(f"Book not found")
    

'''
    Library's system requirements:
        - Add book 
        - Remove book 
        - Search book 
        - Register for new person
'''