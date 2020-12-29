from django import forms
from django.contrib.auth.models import Group

from allauth.account.forms import SignupForm, LoginForm
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

from phonenumber_field.formfields import PhoneNumberField

from .models import Client, Sitter


class UserSignUpForm(SignupForm):
    USER_CLIENT = 0
    USER_SITTER = 1
    USER_CHOICES = (
        (USER_CLIENT, "Client"),
        (USER_SITTER, "Sitter"),
    )

    phone_number = PhoneNumberField(
        widget=forms.TextInput(attrs={'placeholder': "Phone number"}),
        required=True,
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': "First name"})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': "First name"})
    )

    user_type = forms.TypedChoiceField(
        choices=USER_CHOICES,
        coerce=int,
        widget=forms.HiddenInput(),
        required=True,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={'placeholder': "Password"}
        )
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'placeholder': "Confirm password"}
        )

    def signup(self, request, user):
        user.phone_number = self.cleaned_data['phone_number']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if self.cleaned_data['user_type'] == self.USER_CLIENT:
            user.is_client = True
            user.save()
            group = Group.objects.get(name='Clients')
            user.groups.add(group)
            client = Client.objects.create(user=user)
            client.save()
        elif self.cleaned_data['user_type'] == self.USER_SITTER:
            user.is_sitter = True
            user.save()
            group = Group.objects.get(name='Sitters')
            user.groups.add(group)
            sitter = Sitter.objects.create(user=user)
            sitter.save()

    def save(self, request):
        adapter = get_adapter(request)
        user = adapter.new_user(request)
        adapter.save_user(request, user, self, commit=False)
        self.signup(request, user)
        setup_user_email(request, user, [])
        return user


class UserLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

        login_widget = forms.TextInput(
            attrs={
                'placeholder': "E-mail or Phone number",
                'autocomplete': "email",
            }
        )
        login_field = forms.CharField(
            label="Login", widget=login_widget
        )

        self.fields['login'] = login_field
        
    def user_credentials(self):
        """
        Provides the credentials required to authenticate the user for
        login.
        """
        credentials = {}
        login = self.cleaned_data["login"]
        if self._is_login_email(login):
            credentials["email"] = login
        credentials["phone_number"] = login
        credentials["password"] = self.cleaned_data["password"]
        return credentials

