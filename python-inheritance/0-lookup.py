#!/usr/bin/python3
"""
Bu modul obyektin atribut və metodlarını tapmaq üçün funksiyanı ehtiva edir.
"""


def lookup(obj):
    """
    Obyektin mövcud atribut və metodlarının siyahısını qaytarır.

    Args:
        obj: Yoxlanılacaq obyekt.

    Returns:
        list: Atribut və metodların adlarından ibarət siyahı.
    """
    return dir(obj)
