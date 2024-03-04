from unittest import TestCase, main
from calculator import mul

class TestCalculator(TestCase):
    
    def test_mul(self):
        self.assertEqual(mul(2, 2), 4)

if __name__ == '__main__':
    main()
