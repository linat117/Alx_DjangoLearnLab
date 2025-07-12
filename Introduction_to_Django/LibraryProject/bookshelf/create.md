

## 1. Create Operation


from bookshelf.models import Book

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
print(book)

## Expected output

1984 by George Orwell

