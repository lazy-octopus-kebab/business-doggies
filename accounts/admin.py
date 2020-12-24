from django.contrib import admin

from .models import User, Sitter, Client


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone_number', 'first_name', 'last_name', 'id')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions', 'is_client',
                                       'is_sitter')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ['email', 'first_name', 'last_name', 'phone_number']


admin.site.register(User, UserAdmin)
admin.site.register(Sitter)
admin.site.register(Client)
