from django.urls import path
from . import views

urlpatterns = [
    path('schemas-lister/', views.SchemasLister.as_view(), name='SchemasLister'),
    path('schemas-lister/<int:pk>', views.SchemasDetails.as_view(), name='SchemasDetails'),
]
