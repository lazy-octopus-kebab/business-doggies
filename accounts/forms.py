from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import Group
from django import forms
from django.db import transaction

from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget

from .models import User, Sitter, Client


class ClientSignUpForm(UserCreationForm):
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
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

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


class SitterSignUpForm(UserCreationForm):
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
            'email': forms.EmailInput(attrs={'placeholder': "Email"}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': "Password"})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': "Confirm password"})
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_sitter = True

        user.save()

        group = Group.objects.get(name='Sitters')
        user.groups.add(group)

        sitter = Sitter.objects.create(user=user)
        
        sitter.save()

        return user


class UserAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
