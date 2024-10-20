# Base class Book
class Book:
    def __init__(self, title, author):
        """Initialize common attributes for all books."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return a string representation of the book."""
        return f"Book: {self.title} by {self.author}"


# Derived class EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize EBook attributes, including calling the base class initializer."""
        super().__init__(title, author)  # Call the base class initializer
        self.file_size = file_size

    def __str__(self):
        """Return a string representation of the EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


# Derived class PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize PrintBook attributes, including calling the base class initializer."""
        super().__init__(title, author)  # Call the base class initializer
        self.page_count = page_count

    def __str__(self):
        """Return a string representation of the PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


# Library class demonstrating composition
class Library:
    def __init__(self):
        """Initialize the Library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add a book (of any type) to the library's collection."""
        self.books.append(book)

    def list_books(self):
        """Print details of all books in the library."""
        for book in self.books:
            print(book)
