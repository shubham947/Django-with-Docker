"""
Test custom Django management commands.
"""
from unittest.mock import patch
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


@patch('core.management.commands.wait_for_db.connections')
class CommandTests(SimpleTestCase):
    """Test commands."""

    def test_wait_for_db_ready(self, patched_connections):
        """Test waiting for database if the database is ready."""
        patched_connections['default'].cursor.return_value = True

        call_command('wait_for_db')

        patched_connections['default'].cursor.assert_called_once()

    @patch('time.sleep', return_value=None)
    def test_wait_for_db_delay(self, patched_sleep, patched_connections):
        """Test waiting for delayed database connection."""
        patched_connections['default'].cursor.side_effect = \
            [OperationalError] * 4 + [True]

        call_command('wait_for_db')

        self.assertEqual(patched_connections['default'].cursor.call_count, 5)
