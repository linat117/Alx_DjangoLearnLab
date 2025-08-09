# api/urls.py
from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    # List all books (GET)
    path('books/', BookListView.as_view(), name='book-list'),

    # Retrieve single book (GET)
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # Create a new book (POST) - requires authentication
    path('books/create/', BookCreateView.as_view(), name='book-create'),

    # Update a book (PUT / PATCH) - requires authentication
    path('books/update/', BookUpdateView.as_view(), name='book-update'),

    # Delete a book (DELETE) - requires authentication
    path('books/delete/', BookDeleteView.as_view(), name='book-delete'),
]
