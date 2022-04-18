from django.contrib import admin

from Books.models import *

admin.site.register(Categorie)
admin.site.register(Nationalitie)
admin.site.register(Author)
admin.site.register(Book)

