## Basic CRUD Commands on the Book model

```python
# Import Book model
>>> from bookshelf.models import Book
# Create new instance of book
>>> book = Book(title = '1984', author = 'George Orwell', published_date = 1949)
>>> book.save()
# Expected output: A new Book object is successfully created and saved to the database.

# Retrieve the new instance of book
>>> Book.objects.all()
<QuerySet [<Book: Book object (1)>]>

# Update title
>>> book.title = 'Nineteen Eighty-Four'
>>> book.title
'Nineteen Eighty-Four'

# delete instance
>>> book.delete()
(1, {'bookshelf.Book': 1})
>>> Book.objects.all()
<QuerySet []>
```