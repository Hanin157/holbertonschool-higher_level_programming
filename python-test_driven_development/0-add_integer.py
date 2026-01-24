#!/usr/bin/python3
"""
This module contains a function that adds two integers.
It takes two arguments, casts them to integers, and returns their sum.
"""

def add_integer(a, b=98):
    """
    Adds two integers.

    Arguments:
        a (int or float): The first number to be added.
        b (int or float, optional): The second number to be added. Defaults to 98.

    Returns:
        int: The sum of the two numbers, casted to an integer.

    Raises:
        TypeError: If a or b are not integers or floats.
        OverflowError: If the result of addition is too large.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    # Check for potential overflow (if the value is too large)
    if abs(a) > 10**308 or abs(b) > 10**308:
        raise OverflowError("Result of addition is too large")

    return int(a) + int(b)
