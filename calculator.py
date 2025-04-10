import math
# First example
def add(a, b):
    try:
        return (a+b)
    except TypeError as e:
        return (str(e))
def sub(a,b):
    try:
        return (a - b)
    except TypeError as e:
        return (str(e))
def mul(a,b):
    try:
        return (a * b)
    except TypeError as e:
        return (str(e))
def div(a,b):
    try:
        return (b/a)
    except ZeroDivisionError as e:
        return (str(e))

def log(a,b):
    try:
        return math.log(a,b)
    except ValueError as e:
        return (str(e))

def exp(a,b):
    try:
        return (a ** b)
    except TypeError as e:
        return (str(e))




