from datetime import datetime
from django.test import TestCase
from django.shortcuts import resolve_url as r

from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from store.authentication.models import Profile


class ProfileModelTest(TestCase):

    def setUp(self):
        self.obj = Profile.objects.create_user(
            username='leonardo', password='secret', name='Leonardo Gregório', email='leogreal@gmail.com')

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

    def test_create_profile(self):
        """Ensure we can create a new profile object."""
        data_to_create = {'username': 'leonardo',
                          'name': 'Leonardo Gregório',
                          'email': 'leogreal@gmail.com',
                          'password': 'secret'}
        response = self.client.post(
            r('authentication:signup'), data_to_create, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class SigninApiGetTest(APITestCase):

    def setUp(self):
        self.obj = Profile.objects.create_user(
            username='leonardo', password='secret', name='Leonardo Gregório', email='leogreal@gmail.com')

        self.client = APIClient()

    def test_get(self):
        """Get /signin/ must return status 405"""
        response = self.client.get(
            r('authentication:signin'), format='json')
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_check_user(self):

        response = self.client.post(
            r('authentication:signin'),
            data=dict(username=self.obj.username, password="secret"),
            content_type="application/json")

        print('==>', self.obj.username, response)

        # self.assertTrue(self.client.login(
        #    username=self.profile.username, password=self.profile.password))

        # response = self.client.get(reverse('check_user'))
        # self.assertEqual(response.status_code, httplib.OK)
