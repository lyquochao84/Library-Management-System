import unittest
from unittest.mock import patch
from classes.library import Library
from classes.book import Book

class Test_Library(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book = Book(isbn="12345", title="The Great Gatsby", author="F. Scott Fitzgerald", genre="Fiction", available=3)
        self.library.add_book(self.book)

    def test_add_book(self):
        # assertIn(): Verify that the key (ISBN) is present in the dictionary (self.library.books)
        # assertEqual(): Verifies that the value associated with the key (book's title) matches the expect value
        self.assertIn(self.book.isbn, self.library.books)
        self.assertEqual(self.library.books[self.book.isbn].title, "The Great Gatsby")

    def test_remove_book(self):
        self.library.remove_book(self.book.isbn)
        # Check if the book has been removed from the library's collection
        self.assertNotIn(self.book.isbn, self.library.books)
   
    def test_remove_nonexistent_book(self):
        # Attempt to remove a book that doesn't exist in the library
        self.library.remove_book("nonexistent_isbn")
        # No assertion needed, just ensure no exception is raised

if __name__ == '__main__':
    unittest.main()