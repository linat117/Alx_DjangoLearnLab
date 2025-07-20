import os
import django
import sys

# Add the base directory (the one containing LibraryProject/) to sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import *

# 1. Query all books by a specific author
author_name = "Chinua Achebe"
author = Author.objects.get(name=author_name)
books = Book.objects.filter(author=author)
print(f"Books by {author.name}:")
for book in books:
    print("-", book.title)

# 2. List all books in a library
library = Library.objects.get(name="Central Library")
print(f"\nBooks in {library.name}:")
for book in library.books.all():
    print("-", book.title)

# 3. Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print(f"\nLibrarian for {library.name}: {librarian.name}")
