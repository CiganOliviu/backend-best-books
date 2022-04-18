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
