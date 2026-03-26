#!/usr/bin/python3
"""Obyektin dəqiq sinif yoxlanılması modulu"""


def is_same_class(obj, a_class):
    """
    Obyektin verilmiş sinfin dəqiq nümunəsi olub olmadığını yoxlayır.
    """
    return type(obj) is a_class
