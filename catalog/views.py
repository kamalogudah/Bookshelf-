# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre


# Create your views here.


def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  # The 'all()' is implied by default.
    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors,
            'num_visits':num_visits}, # num_visits appended
    )

from django.views import generic
class BookListView(generic.ListView):
    model = Book
    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super(BookListView, self).get_context_data(**kwargs)
    #     # Get the blog from id and add it to the context
    #     context['some_data'] = 'This is just some data'
    #     return context
    # context_object_name = 'my_book_list'   # your own name for the list as a template variable
    # # def get_queryset(self):
    # #     return Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    # queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    # template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location

    paginate_by = 10

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author 
        # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super(BookListView, self).get_context_data(**kwargs)
    #     # Get the blog from id and add it to the context
    #     context['some_data'] = 'This is just some data'
    #     return context
    # context_object_name = 'my_book_list'   # your own name for the list as a template variable
    # # def get_queryset(self):
    # #     return Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    # queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    # template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location

    paginate_by = 10


class AuthorDetailView(generic.DetailView):
    model = Author