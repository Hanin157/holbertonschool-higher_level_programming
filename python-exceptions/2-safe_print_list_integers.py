#!/usr/bin/python3
import sys

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
        except IndexError:
            print("Traceback (most recent call last):", file=sys.stderr)
            print("IndexError: list index out of range", file=sys.stderr)
            break
    print()
    return count
