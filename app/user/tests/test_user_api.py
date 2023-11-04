"""
Tests for user APIs.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse('user:create')


def create_user(**params):
    """Create and return new user."""
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    """Test cases for User API without authentication."""

    def setUp(self):
        self.client = APIClient()

    def test_create_user_with_email_success(self):
        """Test creating a user with email successfully."""
        payload = {
            'email': 'test@example.com',
            'password': 'Testpass@123',
            'name': 'Test User'
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(email=payload['email'])
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_create_user_with_phone_success(self):
        """Test creating a user with phone successfully."""
        phone_numbers = [
            '+91-9876543210',
            '+918976543210',
        ]
        for num in phone_numbers:
            payload = {
                'phone': num,
                'password': 'Testpass@123',
                'name': 'Test User'
            }
            res = self.client.post(CREATE_USER_URL, payload)

            self.assertEqual(res.status_code, status.HTTP_201_CREATED)
            user = get_user_model().objects.get(phone=payload['phone'])
            self.assertTrue(user.check_password(payload['password']))
            self.assertTrue(user.get_username(), payload['phone'])

    def test_create_user_with_phone_with_invalid_pattern_raises_error(self):
        """Test creating user with phone not matching pattern, raises error."""
        phone_numbers = [
            '+91-987654321',
            '+91 987654321',
            '+91 9876543210',
            '876543210',
            '+7986543210',
            '+91-798654321a',
        ]
        for num in phone_numbers:
            payload = {'phone': num, 'password': 'Testpass@123'}
            res = self.client.post(CREATE_USER_URL, payload)

            self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_with_duplicate_phone_exists_raises_error(self):
        """Test creating user with existing phone raises error."""
        payload = {'phone': '+91-987654321', 'password': 'Testpass@123'}
        create_user(**payload)

        phone_numbers = [
            '+91-987654321',
            '+91987654321'
        ]
        for num in phone_numbers:
            payload = {'phone': num, 'password': 'Testpass@123'}
            res = self.client.post(CREATE_USER_URL, payload)

            self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_with_invalid_password_raises_error(self):
        """Test creating user with invalid password raises error."""
        passwords = [
            'Tes1@',
            'test@123',
            'TEST@1',
            'Testpass1',
            '+91987654321',
        ]
        for pwd in passwords:
            payload = {'email': 'test@example.com', 'password': pwd}
            res = self.client.post(CREATE_USER_URL, payload)

            self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
