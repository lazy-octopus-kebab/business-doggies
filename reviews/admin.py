from django.contrib import admin

from .models import ReviewRating, Review


admin.site.register(Review)
admin.site.register(ReviewRating)
