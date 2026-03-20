#!/usr/bin/python3
"""Düzbucaqlını (Rectangle) müəyyən edən modul."""


class Rectangle:
    """Düzbucaqlı fiqurunu təmsil edən klass."""

    def __init__(self, width=0, height=0):
        """Yeni bir Rectangle yaradır.

        Args:
            width (int): Düzbucaqlının eni.
            height (int): Düzbucaqlının hündürlüyü.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Eni (width) geri qaytarır."""
        return self.__width

    @width.setter
    def width(self, value):
        """Eni təyin edir və yoxlamalar aparır."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Hündürlüyü (height) geri qaytarır."""
        return self.__height

    @height.setter
    def height(self, value):
        """Hündürlüyü təyin edir və yoxlamalar aparır."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
