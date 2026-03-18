#!/usr/bin/python3
"""
Bu modul mətnin formatlaşdırılması üçün funksiyanı saxlayır.
Simvollardan (. ? :) sonra 2 yeni sətir əlavə edir.
"""


def text_indentation(text):
    """
    Mətni çap edir və '.', '?' və ':' simvollarından sonra
    2 yeni sətir əlavə edir.

    Args:
        text (str): Formatlanacaq mətn.

    Raises:
        TypeError: Əgər text string deyilsə.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    special_chars = [".", "?", ":"]
    i = 0
    text = text.strip(" ")

    while i < len(text):
        print(text[i], end="")
        if text[i] in special_chars:
            print("\n")
            if i + 1 < len(text) and text[i + 1] == " ":
                while i + 1 < len(text) and text[i + 1] == " ":
                    i += 1
        i += 1
