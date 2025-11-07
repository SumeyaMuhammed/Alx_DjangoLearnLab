## Commands to retrieve and display all attributes of the book
```python
# Import Book model
>>> from bookshelf.models import Book
# Create new instance of book
>>> Book.objects.get(title = '1984')
# Result:
<Book: Book object (1)>
```