from datetime import datetime
from django.test import TestCase
from django.shortcuts import resolve_url as r

from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from store.authentication.models import Profile


class ProfileModelTest(TestCase):

    def setUp(self):
        self.obj = Profile(
            username='leonardo',
            name='Leonardo Gregório',
            email='leogreal@gmail.com',
            password='secret',)
        self.obj.save()

    def test_create(self):
        """Ensure we can create a new profile"""
        self.assertTrue(Profile.objects.exists())

    def test_creation_date(self):
        """Profile must have an auto creation_date attr."""
        self.assertIsInstance(self.obj.creation_date, datetime)

    def test_str(self):
        self.assertEqual('Leonardo', str(self.obj))


class SignupApiGetTest(APITestCase):

    def setUp(self):
        self.client = APIClient()

    def test_get(self):
        """Get /signup/ must return status 405"""
        response = self.client.get(
            r('authentication:signup'), format='json')
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)
