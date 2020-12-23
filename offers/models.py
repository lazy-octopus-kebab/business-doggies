from django.db import models
from django.conf import settings
from django.utils import timezone


class Offer(models.Model):

    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_sent",
        related_query_name="%(app_label)s_%(class)ss",
    )

    sitter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_recv",
        related_query_name="%(app_label)s_%(class)ss",
    )

    created_datetime = models.DateTimeField(
        auto_now_add=True,
        help_text="Time and date of creation",
    )

    offer_datetime = models.DateTimeField(
        help_text="Time and date when sitter is needed",
    )
    client_address = models.CharField(
        max_length=255,
        help_text="Client address",
    )

    PAYMENT_METHOD_CASH = 0
    PAYMENT_METHOD_CARD = 1
    PAYMENT_METHOD_CHOICES = [
        (PAYMENT_METHOD_CASH, "Cash"),
        (PAYMENT_METHOD_CARD, "Card"),
    ]
    payment_method = models.PositiveSmallIntegerField(
        choices=PAYMENT_METHOD_CHOICES,
        default=PAYMENT_METHOD_CASH,
        help_text="Payment method",
    )

    STATUS_DECLINED = 0
    STATUS_PENDING = 1
    STATUS_ACCEPTED = 2
    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_ACCEPTED, "Accepted"),
        (STATUS_DECLINED, "Declined"),
    )
    status = models.PositiveSmallIntegerField(
        choices=STATUS_CHOICES,
        default=STATUS_PENDING,
        help_text="Status of the offer",
    )

    def __str__(self):
        return "{} - {}".format(self.client, self.sitter)

    def is_finished(self):
        now = timezone.now()
        return now > self.offer_datetime