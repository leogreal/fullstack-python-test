from datetime import datetime
from django.test import TestCase
from django.shortcuts import resolve_url as r

from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from store.core.models import Product
from store.core.serializers import ProductSerializer


class ProductModelTest(TestCase):

    def setUp(self):
        self.obj = Product(
            name='Running Shoes',
            description='Soft and light running shoes.',
            price=100,)
        self.obj.save()

    def test_create(self):
        self.assertTrue(Product.objects.exists())

    def test_creation_date(self):
        """Product must have an auto creation_date attr."""
        self.assertIsInstance(self.obj.creation_date, datetime)

    def test_str(self):
        self.assertEqual('Running Shoes', str(self.obj))


class ProductApiTest(APITestCase):

    def setUp(self):
        Product.objects.create(
            name='Running Shoes',
            description='Soft and light running shoes.',
            price=100,)
        Product.objects.create(
            name='Blouse',
            description='Cotton blouse',
            price=30,)

        self.client = APIClient()

    def test_get(self):
        """Get /products/ must return status 200"""
        response = self.client.get(r('core:product-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_products(self):
        """Test GET all products"""
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        response = self.client.get(r('core:product-list'), format='json')
        self.assertEqual(response.data, serializer.data)

    def test_create_product(self):
        """Ensure we can create a new product object."""
        url = r('core:product-list')
        data_to_create = {'name': 'Bandana',
                          'description': 'Printed Bandana',
                          'price': '18.55'}
        response = self.client.post(url, data_to_create, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        for key in data_to_create:
            self.assertEqual(data_to_create[key], response.data[key])

    def test_retrieve_product(self):
        """Ensure we can retrieve a product object by id."""
        pk = 1
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product, many=False)
        url = r('core:product-detail', pk=pk)
        response = self.client.get(url, format='json')
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_product(self):
        """Ensure we can update a product object by id."""
        pk = 1
        description = 'Bandana very stylish'

        url = r('core:product-detail', pk=pk)
        response = self.client.get(url, format='json')

        url = r('core:product-detail', pk=pk)
        data_to_update = response.data
        data_to_update['description'] = description

        response = self.client.put(url, data_to_update, format='json')
        self.assertEqual(response.data['description'], description)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
