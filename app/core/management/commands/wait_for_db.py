"""
Django command to wait for the database to be available
"""
from core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for database."""
    
    def handle(self, *args, **options):
        pass