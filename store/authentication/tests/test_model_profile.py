from datetime import datetime
from django.test import TestCase

from store.authentication.models import Profile


class ProfileModelTest(TestCase):

    def setUp(self):
        self.obj = Profile.objects.create_user(
            username='leonardo',
            password='secret',
            name='Leonardo',
            full_display_name='Leonardo Gregório',
            email='leogreal@gmail.com')

    def test_create(self):
        """Ensure we can create a new profile"""
        self.assertTrue(Profile.objects.exists())

    def test_creation_date(self):
        """Profile must have an auto creation_date attr."""
        self.assertIsInstance(self.obj.creation_date, datetime)

    def test_str(self):
        self.assertEqual('Leonardo', str(self.obj))
