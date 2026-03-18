#!/usr/bin/python3
"""
Bu modulda `add_integer` funksiyası yerləşir.
Funksiya iki rəqəmi toplayır.
"""


def add_integer(a, b=98):
    """
    İki tam ədədi (və ya float) toplayan funksiya.

    Arqumentlər:
        a: birinci ədəd (int və ya float olmalıdır)
        b: ikinci ədəd (int və ya float olmalıdır, default 98)

    Returns:
        a + b-nin tam ədəd nəticəsi.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
