# api/test_views.py
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
        self.book1 = Book.objects.create(
            title="Book One",
            publication_year=2020,
            author=self.author
        )
        self.book2 = Book.objects.create(
            title="Book Two",
            publication_year=2021,
            author=self.author
        )

    def test_list_books(self):
        """Anyone can list books (IsAuthenticatedOrReadOnly)"""
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['title'], "Book One")

    def test_retrieve_book(self):
        """Anyone can retrieve a single book"""
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Book One")

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
        """Authenticated users can create books"""
        self.client.force_authenticate(user=self.user)
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
        self.client.force_authenticate(user=self.user)
        url = reverse('book-update', args=[self.book1.id])
        data = {"title": "Updated Book", "publication_year": 2020, "author": self.author.id}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Updated Book")

    def test_delete_book_authenticated(self):
        """Authenticated users can delete a book"""
        self.client.force_authenticate(user=self.user)
        url = reverse('book-delete', args=[self.book2.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_filter_books_by_title(self):
        """Test filtering books by title"""
        url = reverse('book-list') + '?title=Book One'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Book One")

    def test_search_books(self):
        """Test search functionality"""
        url = reverse('book-list') + '?search=Two'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Book Two")

    def test_order_books_by_publication_year(self):
        """Test ordering by publication year"""
        url = reverse('book-list') + '?ordering=-publication_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2021)
