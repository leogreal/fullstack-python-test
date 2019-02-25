from django.db import models

from store.authentication.models import Profile


class Order(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'order'

    def __str__(self):
        return str(self.id)
