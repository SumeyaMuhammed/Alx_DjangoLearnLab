from rest_framework import serializers
from .models import Book, Author

class BookSerializer(serializers.ModelSerializer):
  # Serializes Book model fields and validates publication_year.
  class Meta:
    model = Book
    fields = ['title', 'author', 'publication_date']

class AuthorSerializer(serializers.ModelSerializer):
  # Serializes Author model with nested list of books.
  books = BookSerializer(many=True, read_only=True)
  class Meta:
    model = Author
    fields = ['name']