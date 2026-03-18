#!/usr/bin/python3
"""
Bu modul 'print_square' funksiyasını saxlayır.
Modul sənədləşdirməsi boş olmamalı və mütləq burada olmalıdır.
"""


def print_square(size):
    """
    Bu funksiya '#' işarəsi ilə kvadrat çap edir.

    Args:
        size (int): Kvadratın bir tərəfinin uzunluğu.

    Raises:
        TypeError: Əgər size integer deyilsə.
        ValueError: Əgər size 0-dan kiçikdirsə.
    """
    if not isinstance(size, int):
        if isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
