from rest_framework import serializers

from .models import Review, ReviewRating


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = [
            'author',
            'text',
            'pub_date',
        ]
