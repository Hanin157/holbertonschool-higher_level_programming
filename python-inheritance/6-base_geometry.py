#!/usr/bin/python3
"""This module defines BaseGeometry class with area method."""


class BaseGeometry:
    """Base class for geometry."""

    def area(self):
        """Raise exception since area is not implemented."""
        raise Exception("area() is not implemented")
