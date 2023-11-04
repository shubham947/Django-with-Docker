"""
Custom auth backends
"""
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model


User = get_user_model()


class EmailBackend(BaseBackend):
    """Auth backend to support login using Email."""

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None

    # Required for custom backends
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


class PhoneBackend(BaseBackend):
    """Auth backend to support login using Phone."""

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(phone=username)
        except User.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None

    # Required for custom backends
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
