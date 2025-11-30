from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
  # Serializes Book model fields and validates publication_year.

  def validate_publication_year(self, value):
    if value > datetime.now().year:
      raise serializers.ValidationError("Publication year cannot be in the future.")
    return value
  class Meta:
    model = Book
    fields = ['title', 'author', 'publication_date']

class AuthorSerializer(serializers.ModelSerializer):
  # Serializes Author model with nested list of books.
  books = BookSerializer(many=True, read_only=True)
  class Meta:
    model = Author
    fields = ['name']