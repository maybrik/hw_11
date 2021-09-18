from django.contrib import admin

from .models import Author, Publisher, Book, Store


class AuthorInline(admin.TabularInline):
    model = Author


class BookInline(admin.TabularInline):
    model = Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
   # list_display = ('name', 'age')
    fields = ["name", "age"]
    list_filter = ["name"]


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    fields = ["name"]
    inlines = [BookInline]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
   # list_display = ('name', ('pages', 'price', 'rating'), 'authors', 'publisher', 'pubdate')
    list_filter = ["price", "rating"]
    date_hierarchy = "pubdate"
    filter_horizontal = ["authors"]


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    #list_display = ('name', 'books')
    list_filter = ["name"]
    filter_horizontal = ["books"]
