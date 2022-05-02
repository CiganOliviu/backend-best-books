from django.contrib import admin

from Books.models import *


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'field')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'virtually_owned', 'physically_owned')


admin.site.register(Categorie)
admin.site.register(Nationalitie)
admin.site.register(Field)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
