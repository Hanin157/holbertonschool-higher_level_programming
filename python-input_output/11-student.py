#!/usr/bin/python3
"""Defines a Student class with JSON serialization/deserialization."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return dictionary representation of the Student.
        If attrs is a list of strings, only those attributes are returned.
        """
        if isinstance(attrs, list):
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance from a dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
