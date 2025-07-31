from django.urls import path, include
from .views import BookList
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
    path('login/', obtain_auth_token, name='api_token_auth'),  # for login
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
]
