#!/usr/bin/python3
"""
Adds two integers.
Arguments:
a (int or float): The first number to be added.
b (int or float, optional): The second number to be added. Defaults to 98.
Returns:
int: The sum of the two numbers, casted to an integer.
Raises:
TypeError: If a or b are not integers or floats.
"""

def add_integer(a, b=98):
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)

