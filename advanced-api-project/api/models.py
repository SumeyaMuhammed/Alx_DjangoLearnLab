from django.db import models

class Author(models.Model):
  # Represents a book author.
  name = models.CharField(max_length=150)

class Book(models.Model):
  #Represents a book written by an author.
  title = models.CharField(max_length=150)
  publication_year = models.IntegerField()
  Author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author')