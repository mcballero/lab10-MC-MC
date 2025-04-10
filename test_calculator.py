import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(add(2,3),5)
        self.assertEqual(add(0,10),10)
        self.assertRaises(add("78","88"), "Error: Cannot add string")




    def test_subtract(self):
        self.assertEqual(subtract(2, 3), -1)
        self.assertEqual(subtract(6, 4), 2)
        self.assertRaises(subtract("78", "88"), "Error: unsupported operand type(s) for -: 'str' and 'str'")

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        self.assertRaises(div(0,10), ZeroDivisionError)
        self.assertRaises(div("a", 10), TypeError)


    def test_logarithm(self):
        self.assertEqual(logarithm(6,8),1.1605584217036247)
        self.assertEqual(logarithm("6",8), "Error: must be real number, not str")
        self.assertEqual(logarithm(9,8), 0.946394630357186)


     def test_log_invalid_base(self): # 1 assertion
         self.assertEqual(logarithm(0, 8), "Error: Neither input can be 0")
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()