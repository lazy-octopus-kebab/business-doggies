from django.forms import ModelForm
from .models import Offer

class MakeOfferForm(ModelForm):
    class Meta:
        model = Offer
        fields = ('offer_datetime', 'client_address', 'payment_method')
        labels = {
            'offer_datetime': "Date and Time", 
            'client_address': "Your address", 
            'payment_method': "Payment Method",
        }
    