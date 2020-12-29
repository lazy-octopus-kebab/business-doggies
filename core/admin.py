from django.contrib import admin
from django.contrib.auth.models import Group

from allauth.account.models import EmailAddress, EmailConfirmation
from allauth.account import app_settings as allauth_settings


admin.site.unregister(Group)
admin.site.unregister(EmailAddress)
if not allauth_settings.EMAIL_CONFIRMATION_HMAC:
    admin.site.unregister(EmailConfirmation)
