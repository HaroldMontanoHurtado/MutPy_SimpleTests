from unittest import TestCase
from calculator import mul

class TestCalculator(TestCase):
    
    def test_mul(self):
        self.assertEqual(mul(2, 2), 4)
