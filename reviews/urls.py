from django.urls import path
from .views import (
    ReviewListView, 
    ReviewCreateView,
    ReviewDeleteView,
    ReviewRatingListView,
    ReviewRatingCreateView,
    ReviewRatingDeleteView
) 

app_name = 'reviews'
urlpatterns = [
    path('profile/', ReviewListView.as_view(), name = "review-list"),
    path('profile/<int:pk>/delete/', ReviewDeleteView.as_view(), name = "review-delete"),
    path('profile/newreview/', ReviewCreateView.as_view(), name = "review-create"),

    path('profile/', ReviewRatingListView.as_view(), name = "reviewrate-list"),
    path('profile/<int:pk>/delete/', ReviewRatingDeleteView.as_view(), name = "reviewrate-delete"),
    path('profile/newreview/', ReviewRatingCreateView.as_view(), name = "reviewrate-create"),
]