from rest_framework import serializers

from Books.models import Categorie, Nationalitie, Author, Book


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'


class NationalitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nationalitie
        fields = '__all__'


class AuthorsSerializer(serializers.ModelSerializer):
    nationality = NationalitiesSerializer(read_only=True)

    class Meta:
        model = Author
        fields = '__all__'


class BooksSerializer(serializers.ModelSerializer):
    author = AuthorsSerializer(read_only=True)
    category = CategoriesSerializer(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'
