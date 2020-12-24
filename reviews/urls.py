from django.urls import path
from .views import (
    ReviewCreateView,
    ReviewRatingCreateView
) 

app_name = 'reviews'
urlpatterns = [
    # ex: /reviews/create/1/
    path('create/<int:pk>/', ReviewCreateView.as_view(), name='create'),

    # ex: /reviews/createrating/1
    path('createrating/<int:pk>/', ReviewRatingCreateView.as_view(), name='createrating'),
]