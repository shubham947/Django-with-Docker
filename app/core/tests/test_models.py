"""
Tests for models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
# from django.core.exceptions import ValidationError


def create_user_with_email(email='user@example.com', password='Testpass123'):
    """Create a user with email and return"""
    return get_user_model().objects.create_user(
            email=email, password=password
        )


def create_user_with_phone(phone='+91-9876543210', password='Testpass123'):
    """Create a user with phone and return"""
    return get_user_model().objects.create_user(
            phone=phone, password=password
        )


class ModelTests(TestCase):
    """Test cases for models"""

    def test_create_user_with_email_successful(self):
        """Test creating a user with email successfully."""
        email = 'testuser@example.com'
        password = 'TestPass123'
        user = create_user_with_email(email, password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_with_phone_successful(self):
        """Test creating a user with phone successfully."""
        phone = '+91-8907654321'
        password = 'Testpass123'
        user = create_user_with_phone(phone, password)

        self.assertEqual(user.phone, phone)
        self.assertTrue(user.check_password(password))

    def test_create_user_email_lowercased(self):
        """Test create user with email lowercased."""
        sample_emails = [
            ['TEST@EXAMPLE.COM', 'test@example.com'],
            ['uSER@example.COM', 'user@example.com'],
            ['Test2@Example.Com', 'test2@example.com'],
            ['user1@EXAMPLE.com', 'user1@example.com'],
        ]

        for email, expected_email in sample_emails:
            user = create_user_with_email(email)
            self.assertEqual(user.email, expected_email)

    def test_create_user_without_email_and_phone_raises_error(self):
        """Test creating user without email and phone raises ValueError."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(password='testPass123')
