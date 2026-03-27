#!/usr/bin/python3
"""
Bu modul faylın sonuna mətn əlavə edən funksiyanı ehtiva edir
"""


def append_write(filename="", text=""):
    """
    Mətni UTF8 formatında faylın sonuna əlavə edir və simvol sayını qaytarır
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
