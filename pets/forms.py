from django.forms import ModelForm

from .models import Pet


class PetForm(ModelForm):
    
    class Meta:
        model = Pet
        fields = ('name', 'description', 'image')
        labels = {
            'name': "Name",
            'description': "Description",
            'image': "Image",
        }