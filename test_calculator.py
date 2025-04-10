import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    # Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(123, 76), 9348)
        self.assertEqual(mul('95', '89'), "can't multiply sequence by non-int of type 'str'")
        self.assertEqual(mul(-5, -97), 485)

    def test_log_invalid_argument(self): # 1 assertion
        self.assertEqual(logarithm(0, 0), "Error: Neither input can be 0")


    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(7.5, 2.5), 7.905)
        self.assertEqual(hypotenuse(3, 4), 5.0)
        self.assertEqual(hypotenuse('NUM', 12), "Error: must be real number, not str")

    def test_sqrt(self): # 3 assertions
        self.assertEqual(square_root(0), 0.0)
        self.assertEqual(square_root(4), 2)
        self.assertAlmostEqual(square_root(2), 1.4142)

# Do not touch this
if __name__ == "__main__":
    unittest.main()