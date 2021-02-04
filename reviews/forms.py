from django.forms import ModelForm, CharField, Textarea, ChoiceField

from .models import Review, ReviewRating
from .serializers import ReviewSerializer


class ReviewForm(ModelForm):
    text = CharField(
        widget=Textarea(attrs={'placeholder': "Write your review"}),
        help_text="Text of review",
    )

    class Meta:
        model = Review
        fields = ['text']


class ReviewRatingForm(ReviewForm):
    rating = ChoiceField(choices=ReviewRating.RATING_CHOICES)

    class Meta:
        model = ReviewRating
        fields = ['text', 'rating']
    