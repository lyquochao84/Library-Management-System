# User Class
class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
        self.borrowed_books = {}
        self.returned_books = {}

   