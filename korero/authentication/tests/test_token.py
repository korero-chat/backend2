import json

from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse


TOKEN_URL = reverse('token')
USER_DATA = {
    'username': 'kicia',
    'password': 'miauMIAU123',
    'email': 'kicia@miau.com'
}

class TokenTests(APITestCase):
    def setUp(self):
        self.client.post(reverse('authentication:create'), USER_DATA)

    def test_obtaining_token(self):
        response = self.client.post(TOKEN_URL, USER_DATA, 'json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_obtaining_token_with_invalid_data(self):
        # use an empty dict for data
        response = self.client.post(TOKEN_URL, {}, 'json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('token', response.data)

    def test_using_a_token_to_retrieve_user_data(self):
        token = self.client.post(TOKEN_URL, USER_DATA, 'json').data['token']
        
        token_client = APIClient()
        token_client.credentials(HTTP_AUTHORIZATION=f'Token {token}')

        response = token_client.get(reverse('authentication:retrieve', args=[1]))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'kicia')
        self.assertNotIn('password', response.data)
