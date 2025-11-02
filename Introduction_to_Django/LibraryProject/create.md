## Basic Command to create an instance

```python
# Import Book model
>>> from bookshelf.models import Book
# Create new instance of book
>>> book = Book(title = '1984', author = 'George Orwell', published_date = 1949)
>>> book.save()
# Expected output: A new Book object is successfully created and saved to the database.
```
