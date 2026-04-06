#!/usr/bin/python3
"""This module defines a function to check inheritance only."""


def inherits_from(obj, a_class):
    """Return True if obj is instance of subclass of a_class."""
    return isinstance(obj, a_class) and type(obj) is not a_class
