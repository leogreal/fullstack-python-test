from django.contrib.auth.models import BaseUserManager


class ProfileManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        """
        Creates and saves a User with the given username and password.
        """
        if not username:
            raise ValueError('The given username must be set')

        is_superuser = extra_fields.pop('is_superuser')

        user = self.model(username=username, **extra_fields)

        if is_superuser:
            user.is_superuser = is_superuser
            user.is_staff()

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(username, password, **extra_fields)
