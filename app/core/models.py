"""
Django models
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.phonenumber import PhoneNumber
from django.utils.translation import gettext as _


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, username=None, email=None, phone=None, password=None,
                    **extra_fields):
        """Create and return a new user."""
        if not email and not phone:
            raise ValueError(_('User must have either email or phone.'))
        if not password:
            raise ValueError(_('Password is required.'))

        if email:
            email = str(email).lower()

        # Normalizing phone
        if phone:
            phone = self.normalize_phone(phone)

        user = self.model(
            username=username,
            email=email,
            phone=phone,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password):
        """Create and return superuser."""
        user = self.create_user(
            username=username, email=username, password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

    def normalize_phone(self, phone):
        phone = PhoneNumber.from_string(phone)
        return str(phone)


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    username = models.CharField(max_length=255, unique=True, null=True)
    email = models.EmailField(
        max_length=255,
        unique=True, null=True, blank=True)
    phone = PhoneNumberField(unique=True, null=True, blank=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_partner = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def get_username(self):
        """Setting username (pk) based on email or phone."""
        return self.email if self.email else str(self.phone)
