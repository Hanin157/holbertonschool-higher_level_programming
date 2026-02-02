#!/usr/bin/python3
"""
Defines a function that returns Pascal's triangle of size n.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle.

    If n <= 0, returns an empty list.
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1]
        if i > 0:
            prev = triangle[i - 1]
            for j in range(1, i):
                row.append(prev[j - 1] + prev[j])
            row.append(1)
        triangle.append(row)

    return triangle
