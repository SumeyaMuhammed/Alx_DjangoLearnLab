## Delete Instance 

```python
# Import Book model
>>> from bookshelf.models import Book
# delete instance
>>> book.delete()
(1, {'bookshelf.Book': 1})
>>> Book.objects.all()
<QuerySet []>
```