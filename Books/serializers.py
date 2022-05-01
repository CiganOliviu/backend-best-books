from rest_framework import serializers

from Books.models import Categorie, Nationalitie, Author, Book, Field


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'


class NationalitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nationalitie
        fields = '__all__'


class FieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'


class AuthorsSerializer(serializers.ModelSerializer):
    nationality = NationalitiesSerializer(read_only=True)
    field = FieldsSerializer(read_only=True)

    class Meta:
        model = Author
        fields = '__all__'


class BooksSerializer(serializers.ModelSerializer):
    authors = AuthorsSerializer(many=True)
    category = CategoriesSerializer(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'
