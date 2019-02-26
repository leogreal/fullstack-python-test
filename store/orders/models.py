from django.db import models

from store.authentication.models import Profile
from store.products.models import Product


class Order(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'order'

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    current_price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()

    class Meta:
        db_table = 'order_item'

    def __str__(self):
        return str(self.id)
