# Objective: Solidify understanding of basic OOP concepts in Python by implementing a system that tracks books in a library, focusing on classes, object instantiation, and method invocation.
# Check ./main-3.py for usage

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        # Private attribute to track checkout status
        self._is_checked_out = False
    
    def __str__(self):
        return f"'{self.title}' by {self.author}"

    # Method to check out the book
    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    # Method to return the book
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False


class Library:
    def __init__(self):
        # Private list to store book instances
        self._books = []
    
    # Add a book to the library
    def add_book(self, book):
        self._books.append(book)

    # Remove a book from the library
    def remove_book(self, book):
        self._books.remove(book)

    # Find a book by its title
    def find_book(self, title):
        for book in self._books:
            if book.title == title:
                return book
        return None

    # Check out a book using the Book class method
    def check_out_book(self, title):
        book = self.find_book(title)
        if book:
            return book.check_out()
        return False
    
    # Return a book using the Book class method
    def return_book(self, title):
        book = self.find_book(title)
        if book:
            return book.return_book()
        return False

    # List all available books (not checked out)
    def list_available_books(self):
        for book in self._books:
            if not book._is_checked_out:
                print(book)