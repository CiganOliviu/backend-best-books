from abc import ABC

from rest_framework import serializers

from Books.models import Categorie, Nationalitie, Author, Book


class CategoriesSerializer(serializers.Serializer, ABC):
    class Meta:
        model = Categorie
        fields = '__all__'


class NationalitiesSerializer(serializers.Serializer, ABC):
    class Meta:
        model = Nationalitie
        fields = '__all__'


class AuthorsSerializer(serializers.Serializer, ABC):
    nationality = NationalitiesSerializer(read_only=True)

    class Meta:
        model = Author
        fields = '__all__'


class BooksSerializer(serializers.Serializer, ABC):
    author = AuthorsSerializer(read_only=True)
    category = CategoriesSerializer(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'
