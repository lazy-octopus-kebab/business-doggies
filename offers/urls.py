from django.urls import path

from .views import (
    OfferListView,
    OfferAnswersListView,
    MakeOfferView,
)
from .views import (
    accept_offer_view,
    decline_offer_view
)


app_name = 'offers'
urlpatterns = [
    # ex: /offers/
    path('', OfferListView.as_view(), name='offers'),

    # ex: /offers/answers
    path('answers/', OfferAnswersListView.as_view(), name='answers'),

    # ex: /offers/1/
    path('<int:sitter_id>/', MakeOfferView.as_view(), name='make'),

    # ex: /offers/1/accept/
    path('<int:sitter_id>/', accept_offer_view, name='accept'),

    # ex: /offers/1/decline/
    path('<int:sitter_id>/', decline_offer_view, name='decline'),
]
