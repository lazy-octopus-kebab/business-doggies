from django.contrib import admin

from .models import User, Sitter, Client


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone_number', 'first_name', 'last_name', 'id')

    search_fields = ['email', 'first_name', 'last_name', 'phone_number']


admin.site.register(User, UserAdmin)
admin.site.register(Sitter)
admin.site.register(Client)
