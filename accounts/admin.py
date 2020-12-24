from django.contrib import admin

from .models import User, Sitter


admin.site.register(User)
admin.site.register(Sitter)