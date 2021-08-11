from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework import status
from .models import Authors
from .serializers import AuthorsSerializer
from utils.validator import Validator


class AuthorsView(APIView):
    def post(self, request, format=None):
        author = AuthorsSerializer(data=request.data)
        if (author.is_valid()):
            Validator(author.validated_data)
            author.save()
            return Response(author.data, status=status.HTTP_201_CREATED)

    def get(self, request, pk=None, format=None):
        if (pk):
            try:
                author = Authors.objects.get(pk=pk)
                author = AuthorsSerializer(author)
                return Response(author.data, status=status.HTTP_200_OK)
            except Authors.DoesNotExist:
                raise NotFound(detail=['Error, author not found'])
        else:
            authors = Authors.objects.all()
            authors = AuthorsSerializer(authors, many=True)
            return Response(authors.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        try:
            author = Authors.objects.get(pk=pk)
            author = AuthorsSerializer(author, request.data)
            if (author.is_valid()):
                Validator(author.validated_data)
                author.save()
                return Response(author.data, status=status.HTTP_200_OK)
            else:
                raise ValidationError(detail=['Error, author not valid'])
        except Authors.DoesNotExist:
            raise NotFound(detail=['Error, author not found'])

    def delete(self, request, pk, format=None):
        try:
            author = Authors.objects.get(pk=pk)
            author = author.delete()
            if (author):
                return Response(author, status=status.HTTP_200_OK)
        except Authors.DoesNotExist:
            raise NotFound(detail=['Error, author not found'])
