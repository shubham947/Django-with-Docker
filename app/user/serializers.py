"""
Serializers for User API view
"""
from django.contrib.auth import get_user_model
# from django.utils.translation import gettext as _

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model"""

    class Meta:
        model = get_user_model()
        fields = ['email', 'phone', 'password', 'name']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 6}}

    def create(self, validated_data):
        """Create and return user with encrypted password."""
        return get_user_model().objects.create_user(**validated_data)
