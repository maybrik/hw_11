from books.models import Author, Publisher, Book, Store

from django.core.management.base import BaseCommand

from faker import Faker

from random import randint, random, randrange

import datetime

# from django.utils import timezone


fake = Faker()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('amount', type=int, default=10, choices=range(1, 200),
                            help='Enter how many data you want to create')


    def handle(self, *args, **options):
        amount = options['amount']


        # for author
        author = []
        for _ in range(amount):
            author.append(Author(name=fake.name(), age=randint(15, 103)))
        Author.objects.bulk_create(author)


        # for publisher
        publisher = []
        for _ in range(amount):
            publisher.append(Publisher(name=fake.company()))
        Publisher.objects.bulk_create(publisher)

        #pubdate block

        start_date = datetime.date(1800, 1, 1)
        end_date = datetime.date(2020, 1, 1)
        time_between = end_date - start_date
        days_between = time_between.days
        random_number_of_days = randrange(days_between)
        pdate = start_date + datetime.timedelta(days=random_number_of_days)


        #ThroughModel = Store.books.through
        #bs = Book.objects.all()
        #store_object = Store()


        #ThroughModel2 = Book.authors.through
        #aus = Author.objects.all()
        #book_object = Book()


        #for book
        book = []
        for _ in range(amount):
            book.append(Book(name=fake.sentence(nb_words=3), pages=randint(1, 10000), price=randint(100, 1000),
                             rating=randint(1, 5), pubdate=pdate,
                             publisher_id=randint(1, amount)))
        Book.objects.bulk_create(book) #, ThroughModel2(author_id=aus[randrange(1, amount)].pk))


        # for store
        store = []
        for _ in range(amount):
            store.append(Store(name=fake.company()))
        Store.objects.bulk_create(store) #, ThroughModel(book_id=bs[randrange(1, amount)].pk))
