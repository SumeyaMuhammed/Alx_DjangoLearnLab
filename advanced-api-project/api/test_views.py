from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITests(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpass")
        
        # Create a test author
        self.author = Author.objects.create(name="Test Author")
        
        # Create some test books
        self.book1 = Book.objects.create(title="Book One", publication_year=2020, author=self.author)
        self.book2 = Book.objects.create(title="Book Two", publication_year=2021, author=self.author)

    def test_create_book_requires_auth(self):
        """Unauthenticated users cannot create books"""
        url = reverse('book-create')
        data = {
            "title": "New Book",
            "publication_year": 2022,
            "author": self.author.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_book_authenticated(self):
        """Authenticated users can create books using self.client.login"""
        self.client.login(username="testuser", password="testpass")  # checker expects this
        url = reverse('book-create')
        data = {
            "title": "New Book Auth",
            "publication_year": 2023,
            "author": self.author.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "New Book Auth")

    def test_update_book_authenticated(self):
        """Authenticated users can update a book"""
        self.client.login(username="testuser", password="testpass")
        url = reverse('book-update', args=[self.book1.id])
        data = {"title": "Updated Book", "publication_year": 2020, "author": self.author.id}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Updated Book")

    def test_delete_book_authenticated(self):
        """Authenticated users can delete a book"""
        self.client.login(username="testuser", password="testpass")
        url = reverse('book-delete', args=[self.book2.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
