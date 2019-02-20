from django.contrib.auth.models import BaseUserManager


class ProfileManager(BaseUserManager):
    def create_user(self, username, password):
        user = self.model(username, password)
        return user

    def create_superuser(self, username, password):
        user = self.model(username, password)
        return user
