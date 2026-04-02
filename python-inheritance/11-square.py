#!/usr/bin/python3
"""Square modul sənədləşməsi."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square sinif sənədləşməsi."""

    def __init__(self, size):
        """İnisializasiya metodu.
        Args:
            size (int): Kvadratın tərəfi.
        """
        # Əvvəlcə validasiya edirik
        self.integer_validator("size", size)
        # Valideyn sinfin (Rectangle) init-ni çağırırıq
        super().__init__(size, size)
        # Şəxsi (private) atributu saxlayırıq
        self.__size = size

    def area(self):
        """Sahəni hesablayan metod."""
        return self.__size ** 2

    def __str__(self):
        """Kvadratın string təmsili."""
        return "[Square] {}/{}".format(self.__size, self.__size)
