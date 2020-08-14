import json

from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse

class UserCreateTests(APITestCase):
    def test_create_user_with_valid_credentials(self):
        url = reverse('authentication:create')
        data = {
            'username': 'kicia',
            'email': 'kicia@miau.com',
            'password': 'miauMIAU123'
        }

        response = self.client.post(url, data, 'json')
        body = json.loads(response.getvalue())

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(body['username'], 'kicia')

    def test_create_user_with_invalid_email(self):
        url = reverse('authentication:create')
        data = {
            'username': 'kicia',
            'email': 'kiciamiaucom',
            'password': 'miauMIAU123'
        }

        response = self.client.post(url, data, 'json')
        # body = json.loads(response.getvalue())

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # self.assertEqual(body['username'], 'kicia')

    def test_create_user_with_invalid_password(self):
        url = reverse('authentication:create')
        data = {
            'username': 'kicia',
            'email': 'kicia@miau.com',
            'password': '12345'
        }

        response = self.client.post(url, data, 'json')
        # body = json.loads(response.getvalue())

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # self.assertEqual(body['username'], 'kicia')
    
    def test_create_user_with_too_short_username(self):
        url = reverse('authentication:create')
        data = {
            'username': 'k',
            'email': 'kicia@miau.com',
            'password': 'miauMIAU123'
        }

        response = self.client.post(url, data, 'json')
        # body = json.loads(response.getvalue())

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
