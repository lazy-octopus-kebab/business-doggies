from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_client = models.BooleanField(default=False)
    is_sitter = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class Sitter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(null=True)
