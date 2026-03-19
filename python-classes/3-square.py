#!/usr/bin/python3
"""Module that defines a Square class."""

class Square:
    """Square class."""
    def __init__(self, size=0):
        """Initialize the Square class."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = size
    def area(self):
        """Return the area of the square."""
        return self.size ** 2
