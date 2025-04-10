# https://github.com/mcballero/lab10-MC-MC.git
# Partner 1: Maria Caballero
# Partner 2: Matias Camaran

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    # Partner 2
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(0, 10), 10)
        with self.assertRaises(TypeError):
            add("78", "88")  # Will now raise

    def test_subtract(self):
        self.assertEqual(subtract(2, 3), -1)
        self.assertEqual(subtract(6, 4), 2)
        with self.assertRaises(TypeError):
            subtract("78", "88")

    # Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 10)

    # Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(123, 76), 9348)
        with self.assertRaises(TypeError):
            mul('95', '89')
        self.assertEqual(mul(-5, -97), 485)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(6, 8), 1.16055842, places=6)
        with self.assertRaises(TypeError):
            logarithm("6", 8)
        self.assertAlmostEqual(logarithm(9, 8), 0.94639463, places=6)

    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(5, 0)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 0)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(7.5, 2.5), 7.906, places=3)
        self.assertEqual(hypotenuse(3, 4), 5.0)
        with self.assertRaises(TypeError):
            hypotenuse('NUM', 12)

    def test_sqrt(self): # 3 assertions
        self.assertEqual(square_root(0), 0.0)
        self.assertEqual(square_root(4), 2)
        self.assertAlmostEqual(square_root(2), 1.4142136, places=6)
        with self.assertRaises(ValueError):
            square_root(-4)


if __name__ == "__main__":
    unittest.main()