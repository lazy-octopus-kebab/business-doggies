from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.forms import CharField, Textarea
from django.db import transaction

from phonenumber_field.formfields import PhoneNumberField

from .models import User, Sitter, Client


class ClientSingUpForm(UserCreationForm):
    phone_number = PhoneNumberField()

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
    phone_number = PhoneNumberField()
    description = CharField(
        widget=Textarea,
        help_text="Information about you and your experience.",
    )

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'phone_number',
            'description',
        )

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
