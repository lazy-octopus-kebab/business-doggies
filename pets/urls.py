from django.urls import path

from .views import (
    PetCreateView
)

app_name = 'pets'
urlpatterns = [
    # ex: /pets/create/
    path('create/', PetCreateView.as_view(), name='create'),
]