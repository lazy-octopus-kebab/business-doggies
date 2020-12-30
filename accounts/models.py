from django.db import models
from django.urls import reverse
from django.contrib.auth.models import (
    AbstractUser,
    BaseUserManager,
    Group
)

from phonenumber_field.modelfields import PhoneNumberField
from guardian.mixins import GuardianUserMixin


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, phone_number, password, **extra_fields):
        """Create and save a User with the given email and password."""
        email = self.normalize_email(email)
        user = self.model(email=email, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        if extra_fields.get('is_client'):
            group = Group.objects.get(name='Clients')
            user.groups.add(group)
            client = Client.objects.create(user=user)
            client.save()
        
        elif extra_fields.get('is_sitter'):
            user.save()
            group = Group.objects.get(name='Sitters')
            user.groups.add(group)
            sitter = Sitter.objects.create(user=user)
            sitter.save()

        return user

    def create_user(self, email, phone_number, password, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_client', False)
        extra_fields.setdefault('is_sitter', False)

        if not email:
            raise ValueError('The Email must be set')

        if not phone_number:
            raise ValueError('The Phone number must be set')

        if extra_fields.get('is_client') == extra_fields.get('is_sitter'):
            raise ValueError('User must have is_client=True or is_sitter=True')

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


class User(GuardianUserMixin, AbstractUser):
    """Define a model User"""

    objects = UserManager()

    username = None

    email = models.EmailField("Email", unique=True)
    phone_number = PhoneNumberField("Phone number", unique=True)

    image = models.ImageField("Profile image", upload_to='users/', null=True, blank=True)

    is_client = models.BooleanField(
        "Client status",
        default=False,
        help_text="Designates that this user is a Client.",
    )
    is_sitter = models.BooleanField(
        "Sitter status",
        default=False,
        help_text="Designates that this user is a Sitter.",
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    def get_absolute_url(self):
        """Get absolute url of User profile"""
        return reverse('accounts:profile', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.email


class Client(models.Model):
    """
    Define a model for User model to provide additional Client-related fields
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return self.user.email


class Sitter(models.Model):
    """
    Define a model for User model to provide additional Sitter-related fields
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    description = models.TextField(null=True)

    def __str__(self):
        return self.user.email
