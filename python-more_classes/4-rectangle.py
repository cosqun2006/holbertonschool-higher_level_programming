#!/usr/bin/python3
"""Düzbucaqlının repr təmsilini müəyyən edən modul."""


class Rectangle:
    """Düzbucaqlı fiqurunu təmsil edən klass."""

    def __init__(self, width=0, height=0):
        """Yeni bir Rectangle yaradır."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Eni geri qaytarır."""
        return self.__width

    @width.setter
    def width(self, value):
        """Eni təyin edir və yoxlayır."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Hündürlüyü geri qaytarır."""
        return self.__height

    @height.setter
    def height(self, value):
        """Hündürlüyü təyin edir və yoxlayır."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Sahəni qaytarır."""
        return self.__width * self.__height

    def perimeter(self):
        """Perimetri qaytarır."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Düzbucaqlını '#' simvollarından ibarət string kimi qaytarır."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rect_str = []
        for i in range(self.__height):
            rect_str.append("#" * self.__width)

        return "\n".join(rect_str)

    def __repr__(self):
        """Obyektin kod şəklində təmsilini qaytarır."""
        return "Rectangle({}, {})".format(self.__width, self.__height)
