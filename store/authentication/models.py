from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from store.authentication.managers import ProfileManager


class Profile(AbstractBaseUser):

    username = models.CharField(
        'user name', max_length=50, blank=True, unique=True)
    name = models.CharField('name', max_length=50, blank=True)
    email = models.EmailField('email address', unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    objects = ProfileManager()

    USERNAME_FIELD = 'username'

    class Meta:
        db_table = 'profile'

    def __str__(self):
        return str(self.username).title()
