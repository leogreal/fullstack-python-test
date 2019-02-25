from datetime import datetime
from django.test import TestCase

from store.products.models import Product


class ProductModelTest(TestCase):

    def setUp(self):
        self.obj = Product(
            name='Running Shoes',
            description='Soft and light running shoes.',
            price=100,)
        self.obj.save()

    def test_create(self):
        """Ensure we can create a new product"""
        self.assertTrue(Product.objects.exists())

    def test_creation_date(self):
        """Product must have an auto creation_date attr."""
        self.assertIsInstance(self.obj.creation_date, datetime)

    def test_str(self):
        self.assertEqual('Running Shoes', str(self.obj))
