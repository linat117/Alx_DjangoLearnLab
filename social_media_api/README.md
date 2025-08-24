# Social Media API – Project Setup & Authentication

## Overview
Starter project for a Social Media API using Django + Django REST Framework with Token Authentication and a custom user model (bio, profile_picture, followers).

## Tech
- Django
- Django REST Framework
- DRF Authtoken (TokenAuthentication)
- Pillow (image uploads)

## Quick Start
```bash
pip install django djangorestframework djangorestframework-authtoken Pillow
django-admin startproject social_media_api
cd social_media_api
python manage.py startapp accounts
# add settings and files as in docs
python manage.py makemigrations
python manage.py migrate
python manage.py runserver


Auth header (for create/update/delete):
Authorization: Token <TOKEN>

Create Post

POST /api/posts/
{
  "title": "First post",
  "content": "Hello world!"
}


List Posts (paginated, search, ordering)

GET /api/posts/?search=hello&ordering=-created_at&page=1


Update/Delete Post (owner only)

PATCH /api/posts/1/
DELETE /api/posts/1/


Create Comment

POST /api/comments/
{
  "post": 1,
  "content": "Nice post!"
}


List Comments for a Post

GET /api/comments/?post=1


Posts

GET /api/posts/ (list, paginated, ?search=..., ?ordering=created_at|-created_at|title)

POST /api/posts/ (auth) { "title": "...", "content": "..." }

GET /api/posts/{id}/

PATCH /api/posts/{id}/ (owner)

DELETE /api/posts/{id}/ (owner)

Comments

GET /api/comments/?post=<post_id> (list for a post)

POST /api/comments/ (auth) { "post": <id>, "content": "..." }

GET /api/comments/{id}/

PATCH /api/comments/{id}/ (owner)

DELETE /api/comments/{id}/ (owner)