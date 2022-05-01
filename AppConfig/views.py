from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from AppConfig.models import Schema
from AppConfig.serializers import SchemasSerializer


def index(request):
    return redirect('admin/')


class SchemasLister(APIView):
    @staticmethod
    def get(request):
        data_objects = Schema.objects.all()
        serializer = SchemasSerializer(data_objects, many=True)

        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = SchemasSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SchemasDetails(APIView):
    @staticmethod
    def get_post(pk):
        try:
            return Schema.objects.get(pk=pk)
        except Schema.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        post = self.get_post(pk)
        serializer = SchemasSerializer(post)

        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_post(pk)
        serializer = SchemasSerializer(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.get_post(pk)
        post.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
