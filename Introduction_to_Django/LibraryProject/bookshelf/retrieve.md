## Commands to retrieve and display all attributes of the book
```python
# Import Book model
>>> from bookshelf.models import Book
# Create new instance of book
>>> Book.objects.all()
# Result:
<QuerySet [<Book: Book object (1)>]>
```