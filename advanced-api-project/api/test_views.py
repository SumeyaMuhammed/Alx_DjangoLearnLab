from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Author, Book
from rest_framework import status

class BookAPITests(APITestCase):

    def setUp(self):
        self.author = Author.objects.create(name="Test Author")
        self.book = Book.objects.create(
            title="Sample",
            publication_year=2020,
            author=self.author
        )

    def test_list_books(self):
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book_requires_auth(self):
        data = {
            "title": "New Book",
            "publication_year": 2024,
            "author": self.author.id
        }
        response = self.client.post("/api/books/create/", data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
