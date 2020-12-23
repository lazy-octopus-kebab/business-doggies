from django.forms import ModelForm
from django.forms import DateTimeField

from .models import Offer


class MakeOfferForm(ModelForm):
    offer_datetime = DateTimeField()

    class Meta:
        model = Offer
        fields = ['offer_datetime', 'client_address', 'payment_method']
        labels = {
            'offer_datetime': "Date and Time",
            'client_address': "Your address",
            'payment_method': "Payment Method",
        }
    