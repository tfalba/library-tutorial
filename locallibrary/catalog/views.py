from django.shortcuts import render
  
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.

from catalog.models import Book, Author, BookInstance, Genre, Project, ProjectImage

@login_required
def index(request):
  """View function for home page of site."""

  # Generate counts of some of the main objects
  num_books = Book.objects.all().count()
  num_instances = BookInstance.objects.all().count()

  # Available books (status = 'a')
  num_instances_available = BookInstance.objects.filter(status__exact='a').count()

  # The 'all()' is implied by default.
  num_authors = Author.objects.count()

  # Number of visits to this view, as counted in the session variable.

  num_visits = request.session.get('num_visits', 1)
  request.session['num_visits'] = num_visits + 1

  words = Book.word
  all_titles = []
  for book in Book.objects.all():
    all_titles.append(book.word)
  all_titles = ' / '.join(all_titles)

  all_words = []
  # for book in Book.objects.all():
  #   for copy in BookInstance.objects.all():
  #     all_words.append(copy.word)
  # all_words = ' / '.join(all_words)

  for copy in BookInstance.objects.filter(status__exact='a'):
    all_words.append(copy.word)
  for copy in BookInstance.objects.filter(status__exact='r'):
    all_words.append(copy.word)
  for copy in BookInstance.objects.filter(status__exact='o'):
    all_words.append(copy.word)

  all_words = ' / '.join(all_words)

  context = {
    'num_books': num_books,
    'num_instances': num_instances,
    'num_instances_available': num_instances_available,
    'num_authors': num_authors,
    'words': words,
    'all_titles': all_titles,
    'all_words': all_words,
    'num_visits': num_visits,
  }

  # Render the HTML template index.html with the data in the context variable
  return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
  model = Book
  #context_object_name = 'my_book_list'
  #queryset = Book.objects.all()
  #queryset = Book.objects.filter(title__icontains='the')[:5] # Get 5 books containing the title war
  #template_name = 'books/book_list.html'  # Specify your own template name/location
  template_name = 'books/book_list.html'

class MyView(LoginRequiredMixin, BookListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

class BookDetailView(generic.DetailView):
  model = Book
  template_name = 'book/book_detail.html'

class AuthorListView(generic.ListView):
  model = Author
  #context_object_name = 'my_author_list'
  template_name = 'author/author_list.html'

class AuthorDetailView(generic.DetailView):
  model = Author
  #context_object_name = 'my_author_detail'
  template_name = 'author/author_detail.html'

class ProjectListView(generic.ListView):
  model = Project
  template_name = 'projects/project_list.html'


class ProjectDetailView(generic.DetailView):
  model = Project
  template_name = 'project/project_detail.html'




