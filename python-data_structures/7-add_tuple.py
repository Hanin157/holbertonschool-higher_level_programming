#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure both tuples are at least of length 2
    a1, a2 = tuple_a + (0, 0)
    b1, b2 = tuple_b + (0, 0)

    # Return the sum of the first and second elements
    return (a1 + b1, a2 + b2)
