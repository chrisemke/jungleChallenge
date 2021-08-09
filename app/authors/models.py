from django.db import models
# from authentication.models import Authentication


class Authors(models.Model):
    name = models.CharField(null=False, max_length=100)
    picture = models.CharField(null=True, max_length=255)  # TODO CharField to imageField
    created = models.DateTimeField(auto_now_add=True)
