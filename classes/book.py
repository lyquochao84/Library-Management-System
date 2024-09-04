# Book
class Book:
    def __init__(self, isbn, title, author, genre, available):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available

    def check_availability(self):
        return self.available > 0
    