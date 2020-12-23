from django.urls import path

from .views import (
    
)

app_name = 'offers'
urlpatterns = [
    # ex: /pets/create
    path('create/', OfferListView.as_view(), name='create'),
]
