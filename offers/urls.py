from django.urls import path

from .views import (
    OfferSentListView,
    OfferRecvListView,
    MakeOfferView,
)


app_name = 'offers'
urlpatterns = [
    # ex: /offers/ (sent)
    path('', OfferSentListView.as_view(), name='list'),

    # ex: /offers/ (recv)
    path('', OfferRecvListView.as_view(), name='list'),

    # ex: /offers/1/
    path('<int:pk>/', MakeOfferView.as_view(), name='make'),
]
