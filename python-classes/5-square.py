#!/usr/bin/python3
"""Kvadratı müəyyən edən Square klassı."""


class Square:
    """Kvadrat fiqurunu təmsil edən klass."""

    def __init__(self, size=0):
        """Kvadratı 'size' parametri ilə başladır."""
        self.size = size

    @property
    def size(self):
        """Kvadratın ölçüsünü (size) geri qaytarır."""
        return self.__size

    @size.setter
    def size(self, value):
        """Kvadratın ölçüsünü təyin edir və yoxlamalar aparır."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Kvadratın sahəsini hesablayır və qaytarır."""
        return self.__size ** 2

    def my_print(self):
        """Kvadratı '#' simvolu ilə ekrana çap edir."""
        if self.__size == 0:
            print("")
            return

        for i in range(self.__size):
            print("#" * self.__size)
