from django.db import models
from django.conf import settings


class Pet(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_pet",
        related_query_name="%(app_label)s_%(class)ss",
    )

    name = models.CharField(max_length=150)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='pets/', null=True)

    def __str__(self):
        return '{} - {}'.format(self.owner.email, self.name)
