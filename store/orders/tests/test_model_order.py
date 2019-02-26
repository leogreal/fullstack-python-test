from django.test import TestCase

from store.products.models import Product
from store.orders.models import Profile
from store.orders.models import Order, OrderItem


class OrderModelTest(TestCase):

    def setUp(self):
        self.user = Profile.objects.create_user(
            username='leonardo',
            password='secret',
            name='Leonardo Gregório',
            email='leogreal@gmail.com')

        self.product = Product(
            name='Running Shoes',
            description='Soft and light running shoes.',
            price=100,)
        self.product.save()

        self.order = Order(user=self.user)
        self.order.save()

        self.order_item = OrderItem(order=self.order,
                                    product=self.product,
                                    current_price=self.product.price,
                                    quantity=1)
        self.order_item.save()

    def test_create_order(self):
        """Ensure we can create a new Order"""
        self.assertTrue(Order.objects.exists())

    def test_create_item(self):
        """Ensure we can create a OrderItem"""
        self.assertTrue(OrderItem.objects.exists())
