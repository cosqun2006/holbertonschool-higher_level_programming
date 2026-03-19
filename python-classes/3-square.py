#!/usr/bin/python3
"""Module that defines a Square class with area calculation."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes the square with validation.

        Args:
            size (int): The width/height of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Calculates and returns the current square's area.

        Returns:
            The area of the square (size * size).
        """
        return self.__size ** 2
