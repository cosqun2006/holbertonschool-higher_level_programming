#!/usr/bin/python3
"""
This module provides a function that prints a name.
"""


def say_my_name(first_name, last_name=""):
    """
        Prints 'My name is <first name> <last name>'.

        Args:
            first_name: The first name (string).
            last_name: The last name (string, defaults to "").

        Raises:
            TypeError: If first_name or last_name are not strings.
        """
    if isinstance(first_name, str):
        raise TypeError("first name must be a string.")
    if isinstance(last_name, str):
        raise TypeError("last name must be a string.")
    print("My name is {} {}".format(first_name, last_name))
