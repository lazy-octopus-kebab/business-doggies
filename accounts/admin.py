from django.contrib import admin

from .models import User, Sitter, Client


admin.site.register(User)
admin.site.register(Sitter)
admin.site.register(Client)
