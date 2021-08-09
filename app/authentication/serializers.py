from rest_framework.serializers import ModelSerializer
from .models import Authentication


class AuthenticationSerializer(ModelSerializer):
    class Meta:
        model = Authentication
        fields = ['email']
