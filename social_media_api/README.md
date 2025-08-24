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
