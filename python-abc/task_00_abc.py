#!/usr/bin/env python3
"""This module defines an abstract Animal class and its subclasses."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Abstract method to return animal sound."""
        pass


class Dog(Animal):
    """Dog class that implements Animal."""

    def sound(self):
        """Return dog's sound."""
        return "Bark"


class Cat(Animal):
    """Cat class that implements Animal."""

    def sound(self):
        """Return cat's sound."""
        return "Meow"
