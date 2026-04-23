#!/usr/bin/python3
"""
This module prints a square with the character #.
"""


def print_square(size):
    """
    Prints a square with the character #.
    """

    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")

    if isinstance(size, float):
        if not size.is_integer():
            raise TypeError("size must be an integer")
        size = int(size)

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
