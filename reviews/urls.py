from django.urls import path

from .views import (
    ReviewList,
) 


app_name = 'reviews'
urlpatterns = [
    # ex: /reviews/1/
    path('<int:target_id>/', ReviewList.as_view(), name='reviews'),

    # ex: /reviews/1/rating
    path('<int:user_id>/rating/', ReviewList.as_view(), name='reviews_rating'),
]