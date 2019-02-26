from datetime import datetime

import requests
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import RequestsClient

from store.authentication.models import Profile


class SigninApiTest(APITestCase):

    def setUp(self):
        self.obj = Profile.objects.create_user(
            username='leonardo',
            password='secret',
            name='Leonardo',
            full_display_name='Leonardo Gregório',
            email='leogreal@gmail.com')

        self.client = RequestsClient()

    def test_get(self):
        """Get /signin/ must return status 405"""
        response = self.client.get('http://127.0.0.1:8000/signin/')
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_authenticate_user(self):
        """Ensure we can authenticate a user."""
        data_to_authenticate = {
            "username": "leonardo",
            "password": "secret"
        }

        response = self.client.post(
            'http://127.0.0.1:8000/signin/',
            data=data_to_authenticate)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
