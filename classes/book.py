# Book
class Book:
    def __init__(self, isbn, title, author, genre, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.genre = genre
        self.copies = copies
        self.available = False

    def check_availability(self):
        if self.copies > 0:
            print(f"The book \"{self.title}\" is available. There are {self.copies} copies left.")
            self.available = True
        else:
            print(f"Unfortunately, the book \"{self.title}\" is currently out of stock.")
            self.available = False

    def borrow_book(self):
        if self.copies > 0:
            self.copies -= 1
            print(f"You have successfully borrowed \"{self.title}\".")
            self.check_availability()
        else:
            print(f"Sorry, \"{self.title}\" is not available for borrowing.")

    def return_book(self):
        self.copies += 1
        print(f"You have successfully returned \"{self.title}\".")
        self.check_availability()

'''
    Book's attributes & methods:
        - Attributes: Title(String), ISBN(Number), Author(String), Genre(String), Copies(Number), Available(Boolean)
        - Method: Check Availability, Borrow book, Return book
'''