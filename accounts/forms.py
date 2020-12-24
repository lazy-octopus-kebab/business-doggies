from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django import forms
from django.db import transaction

from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget

from .models import User, Sitter, Client


class ClientSingUpForm(UserCreationForm):
    phone_number = PhoneNumberField(
        widget=forms.TextInput(attrs={'placeholder': "Phone number"}),
    )

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'password1',
            'password2',
        )
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': "First name"}),
            'last_name': forms.TextInput(attrs={'placeholder': "Last name"}),
            'email': forms.TextInput(attrs={'placeholder': "Email"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': "Password"})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': "Confirm password"})

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_client = True

        user.save()

        group = Group.objects.get(name='Clients')
        user.groups.add(group)

        client = Client.objects.create(user=user)

        client.save()
    
        return user


class SitterSingUpForm(UserCreationForm):
    phone_number = PhoneNumberField(
        widget=forms.TextInput(attrs={'placeholder': "Phone number"}),
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': "A little about yourself and your experience"}),
        help_text="Information about you and your experience.",
    )

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'password1',
            'password2',
            'description',
        )
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': "First name"}),
            'last_name': forms.TextInput(attrs={'placeholder': "Last name"}),
            'email': forms.EmailInput(attrs={'placeholder': "Email"}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': "Password"})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': "Confirm password"})

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_sitter = True

        user.save()

        group = Group.objects.get(name='Sitters')
        user.groups.add(group)

        sitter = Sitter.objects.create(user=user)
        sitter.description = self.cleaned_data.get('description')
        
        sitter.save()

        return user
