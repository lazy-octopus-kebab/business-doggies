from django import forms

from .models import Pet


class PetForm(forms.ModelForm):
    image = forms.ImageField()
    
    class Meta:
        model = Pet
        fields = ('name', 'description', 'image')
        labels = {
            'name': "Name",
            'description': "Description",
            'image': "Image",
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': "Pet's name"}),
            'description': forms.TextInput(attrs={'placeholder': "A few words about your pet"}),
        }
