# Objective: Solidify understanding of basic OOP concepts in Python by implementing a system that tracks books in a library, focusing on classes, object instantiation, and method invocation.
# Check ./main-3.py for usage

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        # add a private attribute _is_checked_out initialized to False
        self._is_checked_out = False
    
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
class Library:
    #  a private list _books to store instances of Book.
    def __init__(self):
        self._books = []
    
    # method to add a book to the library    
    def add_book(self, book):
        self._books.append(book)

    # method to remove a book from the library
    def remove_book(self, book):
        self._books.remove(book)

    # method to find a book by its title
    def find_book(self, title):
        for book in self._books:
            if book.title == title:
                return book
        return None

    # method to list all books in the library
    def list_books(self):
        return self._books

    # method to check out a book (set _is_checked_out to True)
    def check_out_book(self, title):
        book = self.find_book(title)
        if book and not book._is_checked_out:
            book._is_checked_out = True
            return True
        return False
    
    # method to return a book (set _is_checked_out to False)
    def return_book(self, title):
        book = self.find_book(title)
        if book and book._is_checked_out:
            book._is_checked_out = False
            return True
        return False
    
    # method to list all available books (not checked out)
    def list_available_books(self):
        for book in self._books:
            if not book._is_checked_out:
                print(book)