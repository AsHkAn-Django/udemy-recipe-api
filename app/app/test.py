"""
Sample tests
"""
from django.test import SimpleTestCase

from . import calc


class CalcTests(SimpleTestCase):
    """Test the calc module."""
    
    def test_add_number(self):
        """Test adding numbers together."""
        res = calc.add(5, 6)
        
        self.assertEqual(res, 11)
    
    def test_subtract_number(self):
        """Test subtracting nubmbers together."""
        res = calc.subtract(6, 5)
        self.assertEqual(res, 1)
        