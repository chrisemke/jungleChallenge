from django.test import TestCase
from .models import Authors
from rest_framework.test import APIClient


class TestAuthors(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = Authors(
            name='userTestGeneral',
            picture='https://pictureGeneral.url'
        )

    def testCreateAuthorsSuccess(self):
        data = {
            'name': 'userTest',
            'picture': 'https://picture.url'
        }
        response = self.client.post('/api/admin/authors/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data,
                         {
                             'id': 1,
                             'name': 'userTest',
                             'picture': 'https://picture.url'
                         }
                         )

    def testGetAuthorSuccess(self):
        response = self.client.get('/api/admin/authors/1')
        self.assertEqual(response.status_code, 200)
