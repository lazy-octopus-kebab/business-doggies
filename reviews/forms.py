from django.forms import ModelForm

from .models import Review, ReviewRating


class ReviewForm(ModelForm):
    
    class Meta:
        model = Review
        fields = ['offer_datetime', 'client_address', 'payment_method']
        labels = {
            'offer_datetime': "Date and Time",
            'client_address': "Your address",
            'payment_method': "Payment Method",
        }
    