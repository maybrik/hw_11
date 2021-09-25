from django.shortcuts import render#, get_object_or_404

from django.views import generic

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Author, Book, Publisher, Store

from django.db.models import Avg, Count

from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    return render(request, "base.html")

# without listview
# def books(request):
  #  books_set = Book.objects.all()
  #  books_amount = Book.objects.annotate(num=Count('name'))
  # return render(request, "books/book_list.html", context={"books": books_set, 'amount': books_amount})


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


""" hw14 """


def confirmation(request):
    return render(request, 'books/confirmation.html')
# add link for b_create/upd/del


class BookListView(ListView):
    model = Book
    context = 'books_all'
    template = 'books/book_list.html'
    paginate_by = 10

    def books(request):
        books_set = Book.objects.all()
        return render(request, "books/book_list.html", context={"books": books_set})


class BookCreateView(CreateView, LoginRequiredMixin):
    model = Book
    fields = ['name', 'pages', 'price', 'rating', 'authors', 'publisher', 'pubdate']
    template = 'books/book_create.html'

    def success(self):
        return render('confirmation.html')

class BookUpdateView(UpdateView, LoginRequiredMixin):
    model = Book
    fields = ['name', 'pages', 'price', 'rating', 'authors', 'publisher', 'pubdate']
    template = 'books/book_update.html'

    def success(self):
        return render('confirmation.html')


class BookDeleteView(DeleteView, LoginRequiredMixin):
    model = Book
    template = 'books/book_delete.html'

    def success(self):
        return render('confirmation.html')
