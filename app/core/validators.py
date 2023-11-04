"""
Password & field validators
"""
import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class NumberValidator(object):
    """Validates presence of digits."""

    def validate(self, password, user=None):
        if not re.findall(r'\d', password):
            raise ValidationError(
                _('Password must contain at least 1 digit, 0-9.'),
                code='password_no_number'
            )

    def get_help_text(self):
        return _('Password must contain at least 1 digit, 0-9.')


class UppercaseValidator(object):
    """Validates the presence of Uppercase characters."""

    def validate(self, password, user=None):
        if not re.findall('[A-Z]', password):
            raise ValidationError(
                _('Password must contain at least 1 Uppercase character, A-Z'),
                code='password_no_uppercase'
            )

    def get_help_text(self):
        return _('Password must contain at least 1 Uppercase character, A-Z')


class LowercaseValidator(object):
    """Validates the presence of Lowercase characters."""

    def validate(self, password, user=None):
        if not re.findall('[a-z]', password):
            raise ValidationError(
                _('Password must contain at least 1 Lowercase character, a-z'),
                code='password_no_lowercase'
            )

    def get_help_text(self):
        return _('Password must contain at least 1 Lowercase character, a-z')


class SymbolValidator(object):
    """Validates the presence of Symbols."""
    def validate(self, password, user=None):
        if not re.findall(r'[()[\]{}|\`~!@#$%^&*_\-+=;:\'",<>./?]', password):
            raise ValidationError(
                _("The password must contain at least 1 symbol: " +
                  "()[]{}|\\`~!@#$%^&*_-+=;:'\",<>./?"),
                code='password_no_symbol',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 symbol: " +
            "()[]{}|\\`~!@#$%^&*_-+=;:'\",<>./?"
        )
