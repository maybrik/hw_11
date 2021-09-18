from django.shortcuts import render#, get_object_or_404

# from django.views import generic

from .models import Author, Book, Publisher, Store

from django.db.models import Avg, Count


def home(request):
    return render(request, "base.html")

# не сработавшие варианты
#class BookAllView(generic.ListView):
#    model = Book
#    context = 'books_all'
#    template = 'books/book_list.html'
# def books(request):
  #   books_set = Book.objects.all()
   # return render(request, "books/book_list.html", context={"books": books_set})

def books(request):
    books_set = Book.objects.all()
    books_amount = Book.objects.annotate(num=Count('name'))
    return render(request, "books/book_list.html", context={"books": books_set, 'amount': books_amount})


def book_detail(request, pk2):
    pk = Book.objects.prefetch_related('authors').get(pk=pk2)
    return render(request, "books/book_detail.html", context={'pk': pk})


def authors_all(request):
    authors_set = Author.objects.all()
    return render(request, "books/authors_all.html", context={"authors": authors_set})

#def author_detail(request, pk2):
# и другие детали не реализованы
    # не разобралась с отсутствием вывода, в т.ч. и с генерейт дитейл.вью

def publishers(request):
    publishers_all = Publisher.objects.all()
    return render(request, "books/publishers_list.html", context={"publishers": publishers_all})


def stores(request):
    stores_all = Store.objects.all()
    return render(request, "books/stores_list.html", context={"stores": stores_all})
