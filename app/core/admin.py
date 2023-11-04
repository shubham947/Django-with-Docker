"""
Django admin customizations.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Future proofing, to support translations
from django.utils.translation import gettext_lazy as _

from core import models


class UserAdmin(BaseUserAdmin):
    """Define admin pages for users."""
    ordering = ['id']
    list_display = ['username', 'email', 'phone', 'name']

    # Adding multiple sections to Update/Add user page
    fieldsets = (
        (None, {'fields': ('username', 'email', 'phone', 'password')}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_partner',
                    'is_superuser'
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )

    # For updating view on Add user page
    add_fieldsets = [
        [
            None,
            {
                'classes': ['wide'],
                'fields': [
                    'username',
                    'email',
                    'phone',
                    'password1',
                    'password2',
                    'is_active',
                    'is_staff',
                    'is_partner',
                    'is_superuser'
                ]
            }
        ]
    ]

    readonly_fields = ['username', 'last_login']


admin.site.register(models.User, UserAdmin)
