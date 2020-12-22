from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Review(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    pub_date = models.DateTimeField(auto_now=True)
    text = models.TextField()


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
    rating = models.IntegerField(
        choices=RATING,
        default=EXCELLENT,
    )
