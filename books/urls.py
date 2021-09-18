from django.contrib import admin
from django.urls import path, include
from books import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.books, name='books'),
    path('books/<int:pk>', views.book_detail, name='book_detail'),
    path('authors/', views.authors_all, name='authors_all'),
   # path('authors/', views.authors, name='authors'),
]
