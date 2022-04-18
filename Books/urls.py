from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('categories-lister/', views.CategoriesLister.as_view(), name='CategoriesLister'),
    path('categories-lister/<int:pk>', views.CategoriesDetails.as_view(), name='CategoriesDetails')
]
urlpatterns = format_suffix_patterns(urlpatterns)