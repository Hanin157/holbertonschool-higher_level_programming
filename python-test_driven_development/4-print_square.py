#!/usr/bin/python3
"""Module that defines a function to print a square."""


def print_square(size):
    """Prints a square with the character #.

    Args:
        size (int): Size of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if type(size) is float:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
