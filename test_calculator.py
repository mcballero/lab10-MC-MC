# https://github.com/mcballero/lab10-MC-MC.git
# Partner 1: Maria Caballero
# Partner 2: Matias Camaran

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    # Partner 2
    def test_add(self):
        self.assertEqual(add(2,3),5)
        self.assertEqual(add(0,10),10)
        self.assertEqual(add("78","88"), "Error: Cannot add string")


    def test_subtract(self):
        self.assertEqual(subtract(2, 3), -1)
        self.assertEqual(subtract(6, 4), 2)
        self.assertEqual(subtract("78", "88"), "Error: unsupported operand type(s) for -: 'str' and 'str'")


    # Partner 2
    def test_divide_by_zero(self): # 1 assertion
        self.assertEqual(div(0,10), 'division by zero')
        self.assertEqual(div("a", 10), "unsupported operand type(s) for /: 'int' and 'str'")

    # Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(123, 76), 9348)
        self.assertEqual(mul('95', '89'), "can't multiply sequence by non-int of type 'str'")
        self.assertEqual(mul(-5, -97), 485)

    def test_logarithm(self):
        self.assertEqual(logarithm(6,8),1.1605584217036247)
        self.assertEqual(logarithm("6",8), "Error: must be real number, not str")
        self.assertEqual(logarithm(9,8), 0.946394630357186)

    def test_log_invalid_argument(self): # 1 assertion
        self.assertEqual(logarithm(5, 0), "Error: Neither input can be 0")

    def test_log_invalid_base(self): # 1 assertion
        self.assertEqual(logarithm(0, 0), "Error: Neither input can be 0")
    

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(7.5, 2.5), 7.906, places=3)
        self.assertEqual(hypotenuse(3, 4), 5.0)
        self.assertEqual(hypotenuse('NUM', 12), "Error: must be real number, not str")

    def test_sqrt(self): # 3 assertions
        self.assertEqual(square_root(0), 0.0)
        self.assertEqual(square_root(4), 2)
        self.assertAlmostEqual(square_root(2), 1.4142136, places=6)

# Do not touch this
if __name__ == "__main__":
    unittest.main()