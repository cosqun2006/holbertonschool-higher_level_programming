#!#!/usr/bin/python3
"""Düzbucaqlı təmsilini dəyişməyə imkan verən modul."""


class Rectangle:
    """
    Düzbucaqlı klassı.

    Attributes:
        number_of_instances (int): Aktiv obyektlərin sayı.
        print_symbol (any): Çap üçün istifadə olunan simvol.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Yeni Rectangle yaradır və sayğacı artırır."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Eni geri qaytarır."""
        return self.__width

    @width.setter
    def width(self, value):
        """Eni təyin edir."""
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
        """Hündürlüyü təyin edir."""
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
        """Düzbucaqlını print_symbol ilə string kimi qaytarır."""
        if self.__width == 0 or self.__height == 0:
            return ""

        # Hər sətri print_symbol-dan istifadə edərək qururuq
        line = str(self.print_symbol) * self.__width
        rect = [line for _ in range(self.__height)]
        return "\n".join(rect)

    def __repr__(self):
        """Obyektin yenidən yaradılması üçün string təmsilini qaytarır."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Obyekt silinəndə mesaj verir və sayğacı azaldır."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
