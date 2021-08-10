from rest_framework.serializers import ModelSerializer
from .models import Authors


class AuthorsSerializer(ModelSerializer):
    class Meta:
        model = Authors
        exclude = ['created']
