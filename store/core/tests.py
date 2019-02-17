from datetime import datetime
from django.test import TestCase

from store.core.models import Product


class ProductModelTest(TestCase):

    def setUp(self):
        self.obj = Product(
            name='Shoes',
            description='Soft and light running shoes.',
            price=100,
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Product.objects.exists())

    def test_creation_date(self):
        """Product must have an auto creation_date attr."""
        self.assertIsInstance(self.obj.creation_date, datetime)

    def test_str(self):
        self.assertEqual('Shoes', str(self.obj))
