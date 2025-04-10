# https://github.com/mcballero/lab10-MC-MC.git
# Partner 1: Maria Caballero
# Partner 2: Matias Camaran

import math


"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""


def square_root(a):
    if a < 0:
        raise ValueError("Cannot get the square root of a negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):  # must be called mul
    return a * b

def div(a, b):  # must be called div
    return b / a  # this exact order

def logarithm(a, b):
    return math.log(b, a)  # base a of b

def exp(a, b):  # must be called exp
    return a ** b