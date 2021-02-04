from django.db.models import Manager
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, phone_number, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The Email must be set')
        if not phone_number:
            raise ValueError('The Phone number must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
Imagine that we already have a JSON API and a mock from our designer. The mock looks like this:
    def create_user(self, email, phone_number, password, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, phone_number, password, **extra_fields)

    def create_superuser(self, email, phone_number, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, phone_number, password, **extra_fields)


class ClientManager(Manager):
    """Custom manager for Client model"""

    def get_queryset(self, *args, **kwargs):
        """Get Clients"""
        return super().get_queryset(*args, **kwargs).filter(is_client=True)


class SitterManager(Manager):
    """Custom manager for Sitter model"""

    def get_queryset(self, *args, **kwargs):
        """Get Sitters"""
        return super().get_queryset(*args, **kwargs).filter(is_client=True)
