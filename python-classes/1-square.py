#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """Represents a square."""

    def __init__(self, size):
        """Initializes the square with a private size attribute.

        Args:
            size: The length of a side of the square.
        """
        self.__size = size
