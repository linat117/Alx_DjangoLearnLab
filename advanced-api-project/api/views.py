# api/views.py
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

"""
Views for Book model using Django REST Framework generic views.

We provide:
- BookListView   -> GET /api/books/                (read-only list)
- BookDetailView -> GET /api/books/<pk>/           (read-only detail)
- BookCreateView -> POST /api/books/create/        (authenticated)
- BookUpdateView -> PUT/PATCH /api/books/<pk>/update/ (authenticated)
- BookDeleteView -> DELETE /api/books/<pk>/delete/ (authenticated)

Permissions:
- List & Detail: accessible by anyone (read-only).
- Create / Update / Delete: restricted to authenticated users.

Additional behaviour:
- BookListView supports simple query param filtering for
  `publication_year` and `author` (author id or partial name).
- Create/Update leverage serializer validation (publication_year not in future).
  perform_create and perform_update are provided hooks for further customization.
"""

class BookListView(generics.ListAPIView):
    """
    List all books.
    Supports optional query parameters:
      - publication_year (exact int)
      - author (either numeric author id OR partial author name)
    Example:
      /api/books/?publication_year=1949
      /api/books/?author=Orwell
      /api/books/?author=1
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # read-only for everyone

    def get_queryset(self):
        queryset = super().get_queryset()
        qp = self.request.query_params

        # filter by publication_year if provided and valid int
        year = qp.get('publication_year')
        if year:
            try:
                year_int = int(year)
                queryset = queryset.filter(publication_year=year_int)
            except ValueError:
                # ignore invalid year filter
                pass

        # filter by author id or name
        author = qp.get('author')
        if author:
            if author.isdigit():
                queryset = queryset.filter(author__id=int(author))
            else:
                queryset = queryset.filter(author__name__icontains=author)

        return queryset


class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieve a single Book by PK.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookCreateView(generics.CreateAPIView):
    """
    Create a new Book instance.

    Requires authentication (users must be logged in). The BookSerializer
    will validate fields (including publication_year not in the future).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Hook for extra logic before saving. Currently just saves as-is.
        # Example: you could attach current user or audit info here.
        serializer.save()


class BookUpdateView(generics.UpdateAPIView):
    """
    Update an existing Book (PUT/PATCH). Requires authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        # Hook for logic before update. Validation is run by serializer.
        serializer.save()


class BookDeleteView(generics.DestroyAPIView):
    """
    Delete a Book by PK. Requires authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
