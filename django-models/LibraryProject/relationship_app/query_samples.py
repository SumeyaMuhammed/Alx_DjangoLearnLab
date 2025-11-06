from .models import Author, Book, Library, Librarian

# Query all books by a specific author
books_by_author = Book.objects.filter(author = "Jemes Clear")

# List all books in a library
library = Library.objects.get(name=library_name)
books = library.books.all()

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library="library1")
