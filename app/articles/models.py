from django.db import models
from authors.models import Authors
# from authentication.models import Authentication


class Articles(models.Model):
    category = models.CharField(null=False, max_length=100)
    title = models.CharField(null=False, max_length=255)
    summary = models.CharField(null=False, max_length=255)
    firstParagraph = models.CharField(null=False, max_length=255)
    body = models.TextField(null=False)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE, null=False)
    created = models.DateTimeField(auto_now_add=True)
