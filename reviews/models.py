from django.db import models
from django.conf import settings


class Review(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_sent",
        related_query_name="%(app_label)s_%(class)ss",
    )

    target = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_recv",
        related_query_name="%(app_label)s_%(class)ss",
    )

    pub_date = models.DateTimeField(auto_now=True)
    text = models.TextField()

    class Meta:
        verbose_name = "Review about Client"
        verbose_name_plural = "Reviews about Clients"


class ReviewRating(Review):
    VERYBAD = 1
    BAD = 2
    OKAY = 3
    GOOD = 4
    EXCELLENT = 5
    RATING = (
        (VERYBAD, 'Very bad'),
        (BAD, 'Bad'),
        (OKAY, 'Okay'),
        (GOOD, 'Good'),
        (EXCELLENT, 'Excellent'),
    )
    rating = models.PositiveIntegerField(
        choices=RATING,
        default=EXCELLENT,
    )

    class Meta:
        verbose_name = "Review about Sitter"
        verbose_name_plural = "Reviews about Sitters"
