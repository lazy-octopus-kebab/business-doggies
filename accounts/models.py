from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser

from phonenumber_field.modelfields import PhoneNumberField
from guardian.mixins import GuardianUserMixin

from .managers import UserManager, ClientManager, SitterManager


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
    REQUIRED_FIELDS = ['phone_number',]

    def get_absolute_url(self):
        """Get absolute url of User profile"""
        return reverse('accounts:profile', kwargs={'pk': self.pk})

    def __str__(self):
        return self.email


class ClientMore(models.Model):
    """
    Define a model for User model to provide additional Client-related fields
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="clientmore",
    )


class SitterMore(models.Model):
    """
    Define a model for User model to provide additional Sitter-related fields
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="sittermore",
    )

    description = models.TextField(null=True)


class Client(User):
    """Proxy User model to implement Client-related functionality"""
    objects = ClientManager()

    def save(self, *args, **kwargs):
        if not self.id:
            self.is_client = True
        return super().save(*args, **kwargs)

    class Meta:
        proxy = True


class Sitter(User):
    """Proxy User model to implement Sitter-related functionality"""
    objects = SitterManager()

    def clean(self):
        super().clean()
        if not self.is_client:
            raise ValidationError("Sitter must have is_sitter=True.")

    def save(self, *args, **kwargs):
        if not self.id:
            self.is_sitter = True
        return super().save(*args, **kwargs)

    class Meta:
        proxy = True
