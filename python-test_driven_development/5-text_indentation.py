#!/usr/bin/python3
"""Module that defines text indentation function."""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): input text

    Raises:
        TypeError: if text is not a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    i = 0
    n = len(text)
    at_line_start = True

    while i < n:
        ch = text[i]

        # Skip spaces at the beginning of a printed line
        if at_line_start and ch == " ":
            i += 1
            continue

        # Handle separators
        if ch in ".?:":
            print(ch)
            print()
            at_line_start = True
            i += 1
            # Skip spaces after separator
            while i < n and text[i] == " ":
                i += 1
            continue

        # Avoid trailing spaces at end of a printed line (before .?: or end)
        if ch == " ":
            j = i
            while j < n and text[j] == " ":
                j += 1
            if j == n or text[j] in ".?:":
                i += 1
                continue

        print(ch, end="")
        at_line_start = False
        i += 1
