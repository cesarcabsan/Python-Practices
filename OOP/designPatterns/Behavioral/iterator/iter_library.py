## The Iterator pattern is a design pattern that provides a way to access the elements of an aggregate object (such as a list or collection) 
## sequentially without exposing its underlying representation.

# Iterator class responsible for iterating over the books in the library
class LibraryIterator:
    def __init__(self, books):
        self.books = books   # The collection (books) to iterate over
        self.position = 0    # Keeps track of the current position in the collection

    # Method to check if there are more items to iterate over
    def has_next(self):
        return self.position < len(self.books)   # Returns True if there are more books to visit

    # Method to return the next book in the iteration
    def next(self):
        # Returns the current book if there is a next item, otherwise None
        book = self.books[self.position] if self.has_next() else None
        self.position += 1    # Move to the next position
        return book


# Aggregate class (BookLibrary) that holds the collection and provides the iterator
class BookLibrary:
    def __init__(self):
        self.books = []  # Initializes an empty list of books

    # Method to add a book to the library
    def add_book(self, book):
        self.books.append(book)   # Adds a book to the collection

    # Method to create and return an iterator for the book collection
    def create_iterator(self):
        return LibraryIterator(self.books)  # Returns an iterator that iterates over the books


# Client code (using the iterator pattern)
library = BookLibrary()   # Creating a library instance
library.add_book("The Great Gatsby")  # Adding books to the library
library.add_book("1984")
library.add_book("To Kill a Mockingbird")

# Creating an iterator for the library
iterator = library.create_iterator()

print("Library Catalog:")
# Iterating over the books using the iterator
while iterator.has_next():
    print(iterator.next())  # Printing each book while the iterator has more items
