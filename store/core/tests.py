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
        """Ensure we can create a new product"""
        self.assertTrue(Product.objects.exists())

    def test_creation_date(self):
        """Product must have an auto creation_date attr."""
        self.assertIsInstance(self.obj.creation_date, datetime)

    def test_str(self):
        self.assertEqual('Running Shoes', str(self.obj))


class ProductApiGetTest(APITestCase):

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
        """Get /products/ all products must be returned"""
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        response = self.client.get(r('core:product-list'), format='json')
        self.assertEqual(response.data, serializer.data)


class ProductApiCreateTest(APITestCase):

    def setUp(self):
        self.client = APIClient()

    def test_create_product(self):
        """Ensure we can create a new product object."""
        data_to_create = {'name': 'Bandana',
                          'description': 'Printed Bandana',
                          'price': '18.55'}
        response = self.client.post(
            r('core:product-list'), data_to_create, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        for key in data_to_create:
            self.assertEqual(data_to_create[key], response.data[key])


class ProductApiRetrieveTest(APITestCase):

    def setUp(self):
        self.pk = 1
        self.product = Product.objects.create(
            name='Running Shoes',
            description='Soft and light running shoes.',
            price=100,)

        self.client = APIClient()

    def test_get(self):
        """Get /products/1/ must return status 200"""
        response = self.client.get(
            r('core:product-detail', pk=self.pk), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_product(self):
        """Ensure we can retrieve a product object by id."""
        serializer = ProductSerializer(self.product, many=False)
        response = self.client.get(
            r('core:product-detail', pk=self.pk), format='json')
        self.assertEqual(response.data, serializer.data)


class ProductApiUpdateTest(APITestCase):

    def setUp(self):
        self.pk = 1
        self.product = Product.objects.create(
            name='Running Shoes',
            description='Soft and light running shoes.',
            price=100,)

        self.client = APIClient()

    def test_put(self):
        """Put /products/1/ must return status 200"""
        data_to_update = ProductSerializer(self.product, many=False).data
        response = self.client.put(
            r('core:product-detail', pk=self.pk), data_to_update, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_product(self):
        """Ensure we can update a product object by id."""
        data_to_update = ProductSerializer(self.product, many=False).data
        data_to_update['description'] = 'Bandana very stylish'

        response = self.client.put(
            r('core:product-detail', pk=self.pk), data_to_update, format='json')

        self.assertEqual(response.data, data_to_update)


class ProductApiDeleteTest(APITestCase):
    def setUp(self):
        self.pk = 1
        self.product = Product.objects.create(
            name='Running Shoes',
            description='Soft and light running shoes.',
            price=100,)

        self.client = APIClient()

    def test_delete_product(self):
        """Ensure we can delete a product object by id."""
        response = self.client.delete(
            r('core:product-detail', pk=self.pk), format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
