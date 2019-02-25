from datetime import datetime
from django.test import TestCase
from django.shortcuts import resolve_url as r

from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from store.products.models import Product
from store.products.serializers import ProductSerializer


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
        response = self.client.get(r('products:product-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_products(self):
        """Get /products/ all products must be returned"""
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        response = self.client.get(r('products:product-list'), format='json')
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
            r('products:product-list'), data_to_create, format='json')
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

        self.valid_pk = 1
        self.invalid_pk = 99
        self.client = APIClient()

    def test_valid_retrieve_product(self):
        """Get /products/1/ must return status 200"""
        response = self.client.get(
            r('products:product-detail', pk=self.valid_pk), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_retrieve_product(self):
        """Must return error 404 on retrieve invalid id."""
        response = self.client.get(
            r('products:product-detail', pk=self.invalid_pk), format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_retrieve_product(self):
        """Ensure we can retrieve a product object by id."""
        serializer = ProductSerializer(self.product, many=False)
        response = self.client.get(
            r('products:product-detail', pk=self.valid_pk), format='json')
        self.assertEqual(response.data, serializer.data)


class ProductApiUpdateTest(APITestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name='Running Shoes',
            description='Soft and light running shoes.',
            price=100,)

        self.valid_pk = 1
        self.invalid_pk = 99
        self.client = APIClient()

    def test_valid_update_product(self):
        """Put /products/1/ must return status 200"""
        data_to_update = ProductSerializer(self.product, many=False).data
        response = self.client.put(
            r('products:product-detail', pk=self.valid_pk), data_to_update, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_product(self):
        """Must return error 404 on update invalid id."""
        data_to_update = ProductSerializer(self.product, many=False).data
        response = self.client.put(
            r('products:product-detail', pk=self.invalid_pk), data_to_update, format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_product(self):
        """Ensure we can update a product object by id."""
        data_to_update = ProductSerializer(self.product, many=False).data
        data_to_update['description'] = 'Bandana very stylish'

        response = self.client.put(
            r('products:product-detail', pk=self.valid_pk), data_to_update, format='json')

        self.assertEqual(response.data, data_to_update)


class ProductApiDeleteTest(APITestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name='Running Shoes',
            description='Soft and light running shoes.',
            price=100,)

        self.valid_pk = 1
        self.invalid_pk = 99
        self.client = APIClient()

    def test_valid_delete_product(self):
        """Ensure we can delete a product object by id."""
        response = self.client.delete(
            r('products:product-detail', pk=self.valid_pk), format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_product(self):
        """Must return error 404 on delete invalid id."""
        response = self.client.delete(
            r('products:product-detail', pk=self.invalid_pk), format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
