#!/usr/bin/python3
"""
This module provides a function that adds two integers.
The function is named add_integer.
"""


def add_integer(a, b=98):
    """
    Adds 2 integers.

    Args:
        a: The first number, must be an int or float.
        b: The second number, must be an int or float. Defaults to 98.

    Returns:
        The sum of a and b as an integer.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
