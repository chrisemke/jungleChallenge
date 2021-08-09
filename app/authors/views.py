from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from .models import Authors
from .serializers import AuthorsSerializer


class AuthorsView(APIView):
    def post(self, request, format=None):
        author = AuthorsSerializer(data=request.data)
        if (author.is_valid()):
            author.save()
            return Response(author.data, status=status.HTTP_201_CREATED)

    def get(self, format=None):
        authors = Authors.objects.all()
        authors = AuthorsSerializer(authors, many=True)
        return Response(authors.data, status=status.HTTP_200_OK)

    def get(self, pk, format=None):
        try:
            authors = Authors.objects.get(pk=pk)
            authors = AuthorsSerializer(authors, many=True)
            return Response(authors.data, status=status.HTTP_200_OK)
        except Authors.DoesNotExist:
            raise NotFound(detail=['Error, author not found'])

    def put(self, pk, request, format=None):
        ...

    def delete(self, pk, request, format=None):
        ...
