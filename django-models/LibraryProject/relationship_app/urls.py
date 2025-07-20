from django.urls import path
from .views import list_books, LibraryDetailView, add_book_view
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('books/', list_books, name='list_books'),  # FBV URL
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # CBV URL
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('admin-dashboard/', views.admin_view, name='admin_view'),
    path('librarian-dashboard/', views.librarian_view, name='librarian_view'),
    path('member-dashboard/', views.member_view, name='member_view'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:pk>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),
    path('books/', views.book_list, name='book_list'),  # You can add a list view if needed
    path('add-book/', add_book_view, name='add_book'),
]
