from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from store.authentication.managers import ProfileManager


class Profile(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(
        'user name', max_length=50, blank=True, unique=True)
    name = models.CharField('name', max_length=50, blank=True)
    email = models.EmailField('email address', unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField('active', default=True)

    objects = ProfileManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'profile'

    def __str__(self):
        return str(self.username).title()
