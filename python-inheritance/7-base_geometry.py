#!/usr/bin/python3
"""This module defines BaseGeometry with validation."""


class BaseGeometry:
    """Base class for geometry."""

    def area(self):
        """Raise exception since area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is an integer greater than 0."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
