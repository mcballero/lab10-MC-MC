# https://github.com/mcballero/lab10-MC-MC.git
# Partner 1: Maria Caballero
# Partner 2: Matias Camaran

import math


"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

# New functions above add
def square_root(a):
    if a < 0:
        raise ValueError("Cannot get the square root of a negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

# Basic operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return b / a  # raises ZeroDivisionError if a == 0

def logarithm(a, b):
    return math.log(b, a)  # raises ValueError if invalid

def exp(a, b):
    return a ** b



