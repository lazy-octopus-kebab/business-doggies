from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Offer(models.Model):
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='proposals',
    )
    sitter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='offers',
    )

    offer_datetime = models.DateTimeField(
        help_text="Time and date when sitter is needed",
    )
    client_address = models.CharField(
        max_length=255,
        help_text="Client address"
    )

    PAYMENT_METHOD_CASH = 'cash'
    PAYMENT_METHOD_CHOICES = [
        (PAYMENT_METHOD_CASH, "Cash"),
    ]
    payment_method = models.CharField(
        max_length=25,
        choices=PAYMENT_METHOD_CHOICES,
        help_text="Payment method",
    )
