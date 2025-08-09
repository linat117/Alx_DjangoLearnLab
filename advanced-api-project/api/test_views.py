from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book

"""
Unit tests for the Book API endpoints.

Covers:
- CRUD operations
- Filtering, searching, ordering
- Permission and authentication checks
"""

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a user for authenticated operations
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create Authors
        self.author1 = Author.objects.create(name="J.R.R. Tolkien")
        self.author2 = Author.objects.create(name="George Orwell")

        # Create Books
        self.book1 = Book.objects.create(
            title="The Hobbit",
            publication_year=1937,
            author=self.author1
        )
        self.book2 = Book.objects.create(
            title="1984",
            publication_year=1949,
            author=self.author2
        )

        # URLs
        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')
        self.update_url = reverse('book-update', kwargs={'pk': self.book1.pk})
        self.delete_url = reverse('book-delete', kwargs={'pk': self.book1.pk})
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book1.pk})

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        data = {
            'title': 'Animal Farm',
            'publication_year': 1945,
            'author': self.author2.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        data = {
            'title': 'Animal Farm',
            'publication_year': 1945,
            'author': self.author2.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        data = {
            'title': 'The Hobbit: Revised',
            'publication_year': 1937,
            'author': self.author1.id
        }
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'The Hobbit: Revised')

    def test_delete_book_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_author(self):
        url = f"{self.list_url}?author__name=J.R.R.%20Tolkien"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'The Hobbit')

    def test_search_books(self):
        url = f"{self.list_url}?search=Tolkien"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books_by_publication_year_desc(self):
        url = f"{self.list_url}?ordering=-publication_year"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], '1984')
