from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from Books.models import Categorie, Nationalitie, Author, Book, Field
from Books.serializers import CategoriesSerializer, NationalitiesSerializer, AuthorsSerializer, BooksSerializer, \
    FieldsSerializer


class CategoriesLister(APIView):
    @staticmethod
    def get(request):
        data_objects = Categorie.objects.all()
        serializer = CategoriesSerializer(data_objects, many=True)

        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = CategoriesSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoriesDetails(APIView):
    @staticmethod
    def get_post(pk):
        try:
            return Categorie.objects.get(pk=pk)
        except Categorie.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        post = self.get_post(pk)
        serializer = CategoriesSerializer(post)

        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_post(pk)
        serializer = CategoriesSerializer(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.get_post(pk)
        post.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class NationalitiesLister(APIView):
    @staticmethod
    def get(request):
        data_objects = Nationalitie.objects.all()
        serializer = NationalitiesSerializer(data_objects, many=True)

        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = NationalitiesSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NationalitiesDetails(APIView):
    @staticmethod
    def get_post(pk):
        try:
            return Nationalitie.objects.get(pk=pk)
        except Nationalitie.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        post = self.get_post(pk)
        serializer = NationalitiesSerializer(post)

        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_post(pk)
        serializer = NationalitiesSerializer(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.get_post(pk)
        post.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class FieldsLister(APIView):
    @staticmethod
    def get(request):
        data_objects = Field.objects.all()
        serializer = FieldsSerializer(data_objects, many=True)

        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = FieldsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FieldsDetails(APIView):
    @staticmethod
    def get_post(pk):
        try:
            return Field.objects.get(pk=pk)
        except Field.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        post = self.get_post(pk)
        serializer = FieldsSerializer(post)

        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_post(pk)
        serializer = FieldsSerializer(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.get_post(pk)
        post.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class AuthorsLister(APIView):
    @staticmethod
    def get(request):
        data_objects = Author.objects.all()
        serializer = AuthorsSerializer(data_objects, many=True)

        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = AuthorsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorsDetails(APIView):
    @staticmethod
    def get_post(pk):
        try:
            return Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        post = self.get_post(pk)
        serializer = AuthorsSerializer(post)

        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_post(pk)
        serializer = AuthorsSerializer(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.get_post(pk)
        post.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class BooksLister(APIView):
    @staticmethod
    def get(request):
        data_objects = Book.objects.all()
        serializer = BooksSerializer(data_objects, many=True)

        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = BooksSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BooksDetails(APIView):
    @staticmethod
    def get_post(pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        post = self.get_post(pk)
        serializer = BooksSerializer(post)

        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_post(pk)
        serializer = BooksSerializer(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.get_post(pk)
        post.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
