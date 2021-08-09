from django.test import TestCase
from .models import Authentication
from rest_framework.test import APIClient


class TestAuthentication(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = Authentication.objects.create_user(
            'userTestGeneral',
            'testGeneral@test.com',
            'abc123@#'
        )

    def testCreateUserSuccess(self):
        data = {
            'username': 'userTest',
            'email': 'test@test.com',
            'password': 'abc123@#'
        }
        response = self.client.post('/api/sign-up/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, {'email': 'test@test.com'})

    def testLoginSuccess(self):
        data = {
            'username': 'userTestGeneral',
            'password': 'abc123@#'
        }
        response = self.client.post('/api/login/', data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'email': 'testGeneral@test.com'})
