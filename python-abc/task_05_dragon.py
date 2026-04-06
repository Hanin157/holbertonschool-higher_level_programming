#!/usr/bin/env python3
"""This module demonstrates mixins with a Dragon class."""


class SwimMixin:
    """Mixin to add swimming capability."""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin to add flying capability."""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class combining swim and fly abilities."""

    def roar(self):
        print("The dragon roars!")
