from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from Books.models import Categorie
from Books.serializers import CategoriesSerializer


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
        except:
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
