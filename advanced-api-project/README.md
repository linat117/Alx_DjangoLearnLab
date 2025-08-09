## API endpoints (advanced_api_project / api app)

Base path: `/api/`

- GET  /api/books/               -> list books (anyone)
- GET  /api/books/?publication_year=<year>&author=<id|name> -> filtered list
- GET  /api/books/<pk>/          -> retrieve single book (anyone)
- POST /api/books/create/        -> create a book (authenticated)
- PUT  /api/books/<pk>/update/   -> update a book (authenticated)
- DELETE /api/books/<pk>/delete/ -> delete a book (authenticated)

Notes:
- The BookSerializer validates that `publication_year` cannot be in the future.
- To perform write operations, create a user (e.g. `python manage.py createsuperuser`) and use BasicAuth/SessionAuth or configure token auth.
