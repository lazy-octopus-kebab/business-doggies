from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from allauth.account.models import EmailAddress

from .models import User, SitterMore, ClientMore


class ReadOnlyInline(admin.StackedInline):
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class EmailAddressInline(ReadOnlyInline):
    model = EmailAddress
    fields = ('email', 'verified',)

    readonly_fields = ('email', 'verified')


class ClientInline(ReadOnlyInline):
    model = ClientMore


class SitterInline(ReadOnlyInline):
    model = SitterMore
    fields = ('description',)


class UserAdmin(DefaultUserAdmin):
    inlines = (EmailAddressInline,)
    client_inlines = (ClientInline,)
    sitter_inlines = (SitterInline,)

    list_display = (
        'email',
        'phone_number',
        'first_name',
        'last_name',
        'is_client',
        'is_sitter',
        'is_superuser',
        'id',
    )
    list_filter = ('is_client', 'is_sitter')
    ordering = ('email',)

    readonly_fields = (
        'date_joined',
        'is_client',
        'is_sitter',
        'last_login',
        'is_superuser',
    )

    fieldsets = (
        (None, {
            'fields': ('email', 'phone_number', 'password')
        }),
        ('Personal info', {
            'fields': ['first_name', 'last_name', 'image']
        }),
        ('Status', {
            'fields': (
                'is_active',
                'is_client',
                'is_sitter',
                'is_superuser',
            )
        }),
        ('Important dates', {
            'fields': (
                'last_login',
                'date_joined',
            )
        }),
    )
    
    search_fields = ['email', 'first_name', 'last_name', 'phone_number']

    def has_add_permission(self, request):
        return False

    def get_inlines(self, request, obj=None):
        if obj.is_client:
            return self.inlines + self.client_inlines
        elif obj.is_sitter:
            return self.inlines + self.sitter_inlines
        return self.inlines


admin.site.register(User, UserAdmin)
