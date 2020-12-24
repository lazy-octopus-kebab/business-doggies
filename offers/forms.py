from django import forms

from .models import Offer


class MakeOfferForm(forms.ModelForm):

    class Meta:
        model = Offer
        fields = ['offer_datetime', 'client_address', 'payment_method', 'comment']
        labels = {
            'offer_datetime': "Date and Time",
            'client_address': "Your address",
            'payment_method': "Payment Method",
        }
        widgets = {
            'client_address': forms.TextInput(attrs={'placeholder': "Your address"}),
            'offer_datetime': forms.DateTimeField(),
            'comment': forms.TextInput(attrs={'placeholder': "Comment"}),
        }
    