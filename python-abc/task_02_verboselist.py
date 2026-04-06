#!/usr/bin/env python3
"""This module defines a VerboseList class."""


class VerboseList(list):
    """A list that prints notifications on changes."""

    def append(self, item):
        """Add item and print message."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extend list and print message."""
        count = len(iterable)
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        """Remove item and print message."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pop item and print message."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
