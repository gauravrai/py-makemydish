"""Example tests"""
from django.test import SimpleTestCase
from app import calc

class CalcTest(SimpleTestCase):
    """Test calc module"""

    def test_add_num(self):
        """Testing add function"""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)