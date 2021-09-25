from django import forms

from .models import Book


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('name', 'pages', 'price', 'rating', 'authors', 'publisher', 'pubdate')
        name = forms.CharField(max_length=300)
        pages = forms.IntegerField()
        price = forms.DecimalField(max_digits=10, decimal_places=2)
        rating = forms.FloatField()
        authors = forms.ManyToManyField(Author)
        publisher = forms.ForeignKey(Publisher, on_delete=models.CASCADE)
        pubdate = forms.DateField()
