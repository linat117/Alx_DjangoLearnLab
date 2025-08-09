from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer

"""
Views for Book model using Django REST Framework generic views.

We provide:
- BookListView   -> GET /api/books/                      (read for all)
- BookDetailView -> GET /api/books/<pk>/                 (read for all)
- BookCreateView -> POST /api/books/create/              (authenticated only)
- BookUpdateView -> PUT/PATCH /api/books/update/<pk>/    (authenticated only)
- BookDeleteView -> DELETE /api/books/delete/<pk>/       (authenticated only)

Permissions:
- List & Detail: accessible by anyone (read-only).
- Create / Update / Delete: restricted to authenticated users.

Additional behaviour:
- BookListView supports optional filtering by publication_year or author name/ID.
"""

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # read for all

    def get_queryset(self):
        queryset = super().get_queryset()
        qp = self.request.query_params

        # Filter by publication_year if provided
        year = qp.get('publication_year')
        if year and year.isdigit():
            queryset = queryset.filter(publication_year=int(year))

        # Filter by author (id or name)
        author = qp.get('author')
        if author:
            if author.isdigit():
                queryset = queryset.filter(author__id=int(author))
            else:
                queryset = queryset.filter(author__name__icontains=author)

        return queryset


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()


class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
