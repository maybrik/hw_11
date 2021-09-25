from django.contrib import admin
from django.urls import path, include
from books import views

urlpatterns = [
    path('', views.home, name='home'),

   # path('books/', views.books, name='books')
    path('books/', views.BookListView.as_view, name='books'),
    path('books/<int:pk>', views.book_detail, name='book_detail'),
    path('books/create_book', views.BookCreateView.as_view(), name='book_create'),
    path('books/<int:pk>/delete', views.BookDeleteView.as_view(), name='book_delete'),
    path('books/<int:pk>/update', views.BookUpdateView.as_view(), name='book_update'),
    path('books/confirmation', views.confirmation(), name='confirmation'),

    path('authors/', views.authors_all, name='authors_all'),
   # path('authors/', views.authors, name='authors'),
]
