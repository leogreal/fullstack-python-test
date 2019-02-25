from django.test import TestCase

from store.orders.models import Profile
from store.orders.models import Order


class OrderModelTest(TestCase):

    def setUp(self):
        self.user = Profile.objects.create_user(
            username='leonardo',
            password='secret',
            name='Leonardo Gregório',
            email='leogreal@gmail.com')

        self.obj = Order(user=self.user)
        self.obj.save()

    def test_create(self):
        """Ensure we can create a new Order"""
        self.assertTrue(Order.objects.exists())
