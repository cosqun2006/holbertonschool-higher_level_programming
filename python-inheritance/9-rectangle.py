#!/usr/bin/python3
"""BaseGeometry-dən miras alan Rectangle modulu"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Düzbucaqlı sinfi, BaseGeometry-dən miras alır"""

    def __init__(self, width, height):
        """Düzbucaqlını en və hündürlüklə inisializasiya edir.

        Args:
            width (int): Düzbucaqlının eni.
            height (int): Düzbucaqlının hündürlüyü.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """jhgytfrdytrfgyhljkjhgdf"""
        return self.__width * self.__height

    def __str__(self):
        """lkjhgfdsgkjhdfs"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
