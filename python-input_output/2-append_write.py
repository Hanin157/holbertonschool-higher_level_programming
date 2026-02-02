#!/usr/bin/python3
"""Module for appending text to a file."""


def append_write(filename="", text=""):
    """Append a string to a file and return number of characters added."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
