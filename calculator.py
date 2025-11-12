import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b): 
    addition = a + b
    return addition

def sub(a, b):
    subtraction = a - b
    return subtraction

def mul (a, b):
    multiply = a * b
    return multiply

def div(a, b):
    division = b / a
    if a == 0:
        raise ZeroDivisionError
    return division

def log(a, b):
    logarithm = math.log(a, b)
    if b == 0:
        raise ValueError
    return logarithm

def exp(a, b):
    exponent = a ^^ b
    return exponent




