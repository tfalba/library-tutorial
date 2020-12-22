from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('books/', views.BookListView.as_view(), name='books'),
  path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
  path('author/', views.AuthorListView.as_view(), name='author'),
  path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
  path('projects/', views.ProjectListView.as_view(), name='projects'),
  path('project/<int:pk>', views.ProjectDetailView.as_view(), name='project-detail'),
  path('resume/', views.index, name='resume'),
  ]
# path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
