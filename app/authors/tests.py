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
        self.user.save()

    def testCreateSuccess(self):
        data = {
            'name': 'userTest',
            'picture': 'https://picture.url'
        }
        response = self.client.post('/api/admin/authors/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data,
                         {
                             'id': 2,
                             'name': 'userTest',
                             'picture': 'https://picture.url'
                         }
                         )

    def testGetAllSuccess(self):
        response = self.client.get('/api/admin/authors/')
        self.assertEqual(response.status_code, 200)

    def testGetOneSuccess(self):
        response = self.client.get('/api/admin/authors/1')
        self.assertEqual(response.status_code, 200)

    def testPutSuccess(self):
        data = {
            'name': 'userTest',
            'picture': 'https://picture22.url'
        }
        response = self.client.put('/api/admin/authors/1', data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data,
                         {'id': 1,
                          'name': 'userTest',
                          'picture': 'https://picture22.url'
                          }
                         )

    def testPutFail(self):
        data = {
            'first_name': 'userTest',
            'picture': 'https://picture22.url'
        }
        response = self.client.put('/api/admin/authors/1', data)
        self.assertEqual(response.status_code, 400)

    def testDeleteSuccess(self):
        response = self.client.delete('/api/admin/authors/1')
        self.assertEqual(response.data, (1, {'authors.Authors': 1}))
        self.assertEqual(response.status_code, 200)
