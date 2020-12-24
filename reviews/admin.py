from django.contrib import admin

from .models import ReviewRating, Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'target', 'pub_date')

    list_filters = ['pub_date']
    search_fields = ['text', 'author', 'target']


admin.site.register(Review, ReviewAdmin)
admin.site.register(ReviewRating, ReviewAdmin)
