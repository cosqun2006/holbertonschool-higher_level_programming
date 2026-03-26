#!/usr/bin/python3
"""BaseGeometry modulu üçün sənədləşdirmə"""
from wsgiref.validate import validator

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """Düzbucaqlını en və hündürlüklə inisializasiya edir.

        Args:
            width (int): Düzbucaqlının eni.
            height (int): Düzbucaqlının hündürlüyü.
        """
        self.integer-validator("width",width)
        self.__width = width
        self.integer-validator("height",height)
        self.__height = height
