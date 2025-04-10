import math
# https://github.com/mcballero/lab10-MC-MC.git
# Partner 1: Maria Caballero
# Partner 2: Matias Camaran

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example

def square_root(a):
    try:
        if a < 0:
            raise ValueError("Cannot get the square root of a negative number")
        return math.sqrt(a)
    except ValueError as e:
        print(f"Error: {e}")
        return None


def hypotenuse(a, b):
    try:
        hypo = math.hypot(a, b)
        return hypo
    except TypeError as e:
        print(f"Error: {e}")
        return None

# calculator.py functions part 1

def add(a, b):
    try:
        result = a + b
        return result
    except TypeError as e:
        print(f"Error: {e}")
        return None

def sub(a, b):
    try:
        result = a - b
        return result
    except TypeError as e:
        print(f"Error: {e}")

def mul(a, b):
    try:
        result = a * b
        return result
    except TypeError as e:
        print(f"Error: {e}")


def div(a, b): # raise ZeroDivisionError if a == 0
    try:
        if a == 0:
            raise ZeroDivisionError("Can't Divide by zero!")
        else:
            result = a / b
            return result
        result = a * b
        return result
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")


def log(a, b):
    try:
        if b == 0 or a == 0:
          raise ValueError('Neither input can be 0')
        else:
            result = math.log(b, a)
            return result
    except ValueError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")


def exp(a, b):
    try:
        result = a ** b
        return result
    except TypeError as e:
        print(f"Error: {e}")






