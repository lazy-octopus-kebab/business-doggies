from django.urls import path
from .views import (
    ReviewCreateView
) 

app_name = 'reviews'
urlpatterns = [
    # ex: /reviews/create/1/
    path('create/<int:pk>/', ReviewCreateView.as_view(), name='create'),

    # ex: /reviews/createrating/1
    path('createrating/<int:pk>/', ReviewCreateView.as_view(), name='createrating'),
]