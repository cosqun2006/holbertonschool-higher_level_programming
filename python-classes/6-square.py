#!/usr/bin/python3
"""Kvadratı və onun mövqeyini müəyyən edən Square klassı."""


class Square:
    """Kvadrat fiqurunu təmsil edən klass."""

    def __init__(self, size=0, position=(0, 0)):
        """Kvadratı size və position ilə başladır."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Size dəyərini qaytarır."""
        return self.__size

    @size.setter
    def size(self, value):
        """Size üçün validation aparır."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Position dəyərini qaytarır."""
        return self.__size_position

    @position.setter
    def position(self, value):
        """Position-un 2 müsbət tam ədəddən ibarət tuple olmasını yoxlayır."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size_position = value

    def area(self):
        """Sahəni qaytarır."""
        return self.__size ** 2

    def my_print(self):
        """Kvadratı position-u nəzərə alaraq '#' ilə çap edir."""
        if self.__size == 0:
            print("")
            return

        # Şaquli boşluqlar (Y oxu) - position[1] qədər boş sətir
        if self.__size_position[1] > 0:
            for _ in range(self.__size_position[1]):
                print("")

        # Kvadratın özünün çapı
        for _ in range(self.__size):
            # Üfüqi boşluqlar (X oxu) - position[0] qədər boşluq
            print(" " * self.__size_position[0] + "#" * self.__size)
