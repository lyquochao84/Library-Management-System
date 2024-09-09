from classes.book import Book

class TestBook:
    def __init__(self):
        # Create instances of the Book class
        self.book1 = Book("123-456", "The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 3)
        self.book2 = Book("789-101", "1984", "George Orwell", "Dystopian", 0)  

    def run_tests(self):
        # Test checking availability
        self.book1.check_availability()
        self.book2.check_availability()
        
        # Test borrowing books
        print("\nAttempting to borrow book1:")
        self.book1.borrow_book() 
        print("\nAttempting to borrow book2:")
        self.book2.borrow_book()  # Should indicate that the book is not available for borrowing

        # Test returning books
        print("\nReturning book1:")
        self.book1.return_book()  

        print("\nReturning book2:")
        self.book2.return_book()  

# Create an instance of TestBook and run tests
test = TestBook()
test.run_tests()
