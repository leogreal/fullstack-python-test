from datetime import datetime
from django.shortcuts import resolve_url as r

from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from store.authentication.models import Profile


class SignupApiTest(APITestCase):

    def setUp(self):
        self.client = APIClient()

    def test_get(self):
        """Get /signup/ must return status 405"""
        response = self.client.get(
            r('authentication:signup'), format='json')
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_create_profile(self):
        """Ensure we can create a new profile object."""
        data_to_create = {'username': 'leonardo',
                          'name': 'Leonardo',
                          'full_display_name': 'Leonardo Gregório',
                          'email': 'leogreal@gmail.com',
                          'password': 'secret'}
        response = self.client.post(
            r('authentication:signup'), data_to_create, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
