#!/usr/bin/python3
"""Module that defines a function to print a person's name."""


def say_my_name(first_name, last_name=""):
    """Prints: My name is <first_name> <last_name>.

    Args:
        first_name (str): First name.
        last_name (str): Last name.

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
