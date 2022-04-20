from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('categories-lister/', views.CategoriesLister.as_view(), name='CategoriesLister'),
    path('categories-lister/<int:pk>', views.CategoriesDetails.as_view(), name='CategoriesDetails'),
    path('nationalities-lister/', views.NationalitiesLister.as_view(), name='NationalitiesLister'),
    path('nationalities-lister/<int:pk>', views.NationalitiesDetails.as_view(), name='NationalitiesDetails'),
    path('authors-lister/', views.AuthorsLister.as_view(), name='AuthorsLister'),
    path('authors-lister/<int:pk>', views.AuthorsDetails.as_view(), name='AuthorsDetails'),
    path('books-lister/', views.BooksLister.as_view(), name='AuthorsLister'),
    path('books-lister/<int:pk>', views.BooksDetails.as_view(), name='AuthorsDetails'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
